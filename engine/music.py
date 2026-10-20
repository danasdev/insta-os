import numpy as np, wave, json, sys
from scipy.signal import butter, sosfilt, sosfilt_zi, fftconvolve, sawtooth, resample_poly

SR = 44100
DUR = 41.0
N = int(SR * DUR)
BPM = 100
BEAT = 60 / BPM          # 0.6 s
BAR = 4 * BEAT           # 2.4 s
rng = np.random.default_rng(11)
T = np.arange(N) / SR

def mtof(m): return 440 * 2 ** ((m - 69) / 12)
def bufs(): return np.zeros(N), np.zeros(N)

def place(L, R, sig, t0, g=1.0, pan=0.0):
    i = int(round(t0 * SR))
    if i >= N or i + len(sig) <= 0: return
    a = max(0, -i); i = max(0, i); j = min(N, i + len(sig) - a)
    s = sig[a:a + (j - i)] * g
    gl = np.cos((pan + 1) * np.pi / 4); gr = np.sin((pan + 1) * np.pi / 4)
    L[i:j] += s * gl * 1.414; R[i:j] += s * gr * 1.414

def sos(kind, f, order=2):
    return butter(order, f, btype=kind, fs=SR, output='sos')

def filt(x, kind, f, order=2): return sosfilt(sos(kind, f, order), x)

def sweep_lp(x, cut_fn, block=1024):
    """time-varying low-pass (block-wise biquad with state carry)"""
    y = np.zeros_like(x); zi = None
    for s in range(0, len(x), block):
        f = float(np.clip(cut_fn(s / SR), 60, SR / 2.2))
        so = sos('low', f)
        if zi is None: zi = sosfilt_zi(so) * 0
        y[s:s + block], zi = sosfilt(so, x[s:s + block], zi=zi)
    return y

def adsr(n, a, d, s, r, sus_len):
    e = np.zeros(n); na, nd, nr = int(a*SR), int(d*SR), int(r*SR); ns = int(sus_len*SR)
    seg = np.concatenate([np.linspace(0, 1, max(na,1)), np.linspace(1, s, max(nd,1)),
                          np.full(max(ns - na - nd, 0), s), np.linspace(s, 0, max(nr,1))])
    e[:min(n, len(seg))] = seg[:n]
    return e

def make_ir(sec=2.6, decay=2.2, seed=3):
    r = np.random.default_rng(seed); n = int(sec*SR); t = np.arange(n)/SR
    env = np.exp(-t * (6.9 / decay))
    l = r.normal(size=n) * env; rr = r.normal(size=n) * env
    l = filt(l, 'low', 6500); rr = filt(rr, 'low', 6500)
    l[:int(.012*SR)] *= np.linspace(0, 1, int(.012*SR)); rr[:int(.017*SR)] *= np.linspace(0, 1, int(.017*SR))
    return l / np.sqrt((l**2).sum()), rr / np.sqrt((rr**2).sum())
IR = make_ir()
def reverb(L, R, wet):
    m = (L + R) / 2
    return L + wet * fftconvolve(m, IR[0])[:N], R + wet * fftconvolve(m, IR[1])[:N]

# ------------------------------------------------------------------ arrangement
CUTS = [4.8, 9.6, 18.0, 22.8, 30.0, 33.6]
END_BAR_T = 33.6
CHORDS = [[53,57,60,64],[57,60,64,67],[55,59,60,64],[55,59,62,67]]   # Fmaj7 Am7 Cmaj7 G
ROOTS  = [41, 45, 48, 43]
NBARS = int(END_BAR_T / BAR)  # 14 bars of groove, then the outro chord

# ---- pad (detuned saws, opening filter, side-chain pump)
padL, padR = bufs()
for b in range(NBARS):
    t0 = b * BAR; ch = CHORDS[b % 4]
    n = int((BAR + 1.2) * SR); tt = np.arange(n) / SR
    env = adsr(n, .35, .2, .85, 1.0, BAR + .1)
    for k, m in enumerate(ch):
        f = mtof(m)
        for dt, pan in [(-0.11, -.6), (0, 0), (0.11, .6)]:
            ff = f * 2 ** (dt * 7 / 1200 * 9)
            x = sawtooth(2 * np.pi * ff * tt + rng.uniform(0, 6.28)) * env * .05
            place(padL, padR, x, t0, 1, pan)
def pad_cut(t):
    if t < 4.8: return 350 + 1400 * (t / 4.8) ** 2
    if t > 30.0 and t < 33.6: return 2600 + 1800 * (t - 30) / 3.6
    return 2400
padL = sweep_lp(padL, pad_cut); padR = sweep_lp(padR, pad_cut)

# ---- outro chord (C add9) + soft sub
outL, outR = bufs()
n = int(7.4 * SR); tt = np.arange(n) / SR
env = np.minimum(1, tt / .08) * np.exp(-tt / 3.2)
for m in [36, 48, 55, 60, 62, 64, 67, 72]:
    for dt, pan in [(-0.1, -.5), (0.1, .5)]:
        f = mtof(m) * 2 ** (dt / 12 * .5)
        x = (sawtooth(2*np.pi*f*tt) * .4 + np.sin(2*np.pi*f*tt)) * env * (.05 if m > 40 else .12)
        place(outL, outR, x, END_BAR_T, 1, pan)
outL = filt(outL, 'low', 2600); outR = filt(outR, 'low', 2600)

# ---- bass (sine + a touch of saturation), syncopated
bassL, bassR = bufs()
def bass_note(m, dur):
    n = int((dur + .1) * SR); tt = np.arange(n) / SR; f = mtof(m)
    e = np.minimum(1, tt / .008) * np.exp(-tt / (dur * .9)); e[-int(.1*SR):] *= np.linspace(1, 0, int(.1*SR))
    return np.tanh(1.6 * np.sin(2 * np.pi * f * tt)) * e * .32
for b in range(2, NBARS):
    r = ROOTS[b % 4]; t0 = b * BAR
    for pos, d, oct in [(0, .5, 0), (1.5, .3, 0), (2, .5, 0), (3.5, .25, 12)]:
        place(bassL, bassR, bass_note(r + oct, d), t0 + pos * BEAT)

# ---- drums
drL, drR = bufs()
def kick():
    n = int(.45 * SR); tt = np.arange(n) / SR
    f = 46 + 90 * np.exp(-tt / .045); ph = 2 * np.pi * np.cumsum(f) / SR
    x = np.sin(ph) * np.exp(-tt / .22) + .25 * filt(rng.normal(size=n), 'band', [1500, 5000]) * np.exp(-tt / .004)
    return x * .55
def clap():
    n = int(.35 * SR); x = np.zeros(n); tt = np.arange(n) / SR
    for k, o in enumerate([0, .011, .022]):
        i = int(o * SR); m = n - i
        x[i:] += rng.normal(size=m) * np.exp(-np.arange(m) / SR / (.008 if k < 2 else .09))
    return filt(x, 'band', [900, 3800]) * .14
def hat(open_=False):
    n = int((.16 if open_ else .05) * SR); tt = np.arange(n) / SR
    return filt(filt(rng.normal(size=n), 'high', 7000), 'low', 12500) * np.exp(-tt / (.05 if open_ else .012)) * .055
def shaker():
    n = int(.06 * SR); tt = np.arange(n) / SR
    return filt(rng.normal(size=n), 'band', [5000, 11000]) * np.sin(np.pi * tt / tt[-1]) ** 2 * .035
KICKS = []
for b in range(2, NBARS):
    t0 = b * BAR
    for beat in (0, 2):
        place(drL, drR, kick(), t0 + beat * BEAT); KICKS.append(t0 + beat * BEAT)
    if b % 2 == 1:
        place(drL, drR, kick() * .5, t0 + 3.5 * BEAT); KICKS.append(t0 + 3.5 * BEAT)
    for beat in (1, 3):
        place(drL, drR, clap(), t0 + beat * BEAT, 1, .05)
    for e8 in range(8):
        if e8 % 2 == 1: place(drL, drR, hat(e8 == 7 and b % 4 == 3), t0 + e8 * BEAT / 2, 1, .35)
    if t0 >= 22.8 - 1e-6:
        for s16 in range(16):
            place(drL, drR, shaker() * (1 if s16 % 2 else .6), t0 + s16 * BEAT / 4, 1, -.4)
# snare-ish fill into the outro
for k in range(8):
    place(drL, drR, clap() * (.3 + .1 * k), 32.4 + k * BEAT / 4, 1, 0)

# side-chain envelope from kicks
sc = np.ones(N)
for k in KICKS:
    i = int(k * SR); n = int(.42 * SR); j = min(N, i + n)
    sc[i:j] = np.minimum(sc[i:j], 1 - .45 * np.exp(-np.arange(j - i) / SR / .13))

# ---- pluck arp (with ping-pong delay)
arL, arR = bufs()
def pluck(m, g):
    n = int(.6 * SR); tt = np.arange(n) / SR; f = mtof(m)
    x = (np.sin(2*np.pi*f*tt) + .35*np.sin(2*np.pi*2*f*tt) + .12*np.sin(2*np.pi*3*f*tt)) * np.exp(-tt / .16)
    x[:int(.003*SR)] *= np.linspace(0, 1, int(.003*SR))
    return x * g
PAT = [0, 1, 2, 3, 2, 1, 3, 2]
for b in range(NBARS):
    ch = CHORDS[b % 4]; t0 = b * BAR
    for e8 in range(8):
        g = .06 if b < 2 else .085
        if 30.0 <= t0 + e8 * BEAT / 2 < 33.6: g *= 1.15
        place(arL, arR, pluck(ch[PAT[e8]] + 12, g), t0 + e8 * BEAT / 2, 1, -.25 if e8 % 2 else .25)
arL = filt(arL, 'low', 3800); arR = filt(arR, 'low', 3800)
d = int(BEAT * .75 * SR)  # dotted-8th delay
dl, dr = np.zeros(N), np.zeros(N)
srcL, srcR = arL.copy(), arR.copy()
for k in range(1, 5):
    g = .38 ** k; sh = d * k
    if k % 2: dl[sh:] += srcR[:-sh] * g; dr[sh:] += srcL[:-sh] * g
    else: dl[sh:] += srcL[:-sh] * g; dr[sh:] += srcR[:-sh] * g
arL += filt(dl, 'low', 2500); arR += filt(dr, 'low', 2500)

# ---- bells on theme switches and the logo
blL, blR = bufs()
def bell(m, dur=2.2, g=.12):
    n = int(dur * SR); tt = np.arange(n) / SR; f = mtof(m)
    x = (np.sin(2*np.pi*f*tt) + .5*np.sin(2*np.pi*f*2.76*tt)*np.exp(-tt/.3) + .25*np.sin(2*np.pi*f*5.4*tt)*np.exp(-tt/.12)) * np.exp(-tt / .7)
    x[:int(.002*SR)] *= np.linspace(0, 1, int(.002*SR))
    return x * g
for t0, m in [(18.0, 76), (19.2, 79), (20.4, 84)]: place(blL, blR, bell(m), t0, 1, .2)
for k, m in enumerate([72, 76, 79, 84]): place(blL, blR, bell(m, 3, .1), END_BAR_T + .02 + k * BEAT / 2, 1, -.3 + .2 * k)

# ---- transition FX: soft swells, airy whooshes, sub drops
fxL, fxR = bufs()
def swell(dur):
    n = int(dur * SR); tt = np.arange(n) / SR; k = tt / dur
    x = rng.normal(size=n); y = np.zeros(n); blk = 2048; zi = None
    for s in range(0, n, blk):
        f = 400 + 5200 * (s / n) ** 2; so = sos('band', [f * .7, f * 1.3])
        if zi is None: zi = sosfilt_zi(so) * 0
        y[s:s+blk], zi = sosfilt(so, x[s:s+blk], zi=zi)
    return y * k ** 2.2 * .5
def whoosh(dur=.7):
    n = int(dur * SR); tt = np.arange(n) / SR; k = tt / dur
    x = rng.normal(size=n); y = np.zeros(n); blk = 1024; zi = None
    for s in range(0, n, blk):
        kk = s / n; f = 500 + 2200 * np.sin(np.pi * kk); so = sos('band', [f * .6, f * 1.5])
        if zi is None: zi = sosfilt_zi(so) * 0
        y[s:s+blk], zi = sosfilt(so, x[s:s+blk], zi=zi)
    return y * np.sin(np.pi * k) ** 2 * .45
def subdrop():
    n = int(1.6 * SR); tt = np.arange(n) / SR
    f = 38 + 30 * np.exp(-tt / .25); ph = 2 * np.pi * np.cumsum(f) / SR
    return np.sin(ph) * np.exp(-tt / .6) * np.minimum(1, tt / .01) * .5
for c, style in zip(CUTS, ['zoom', 'reveal', 'whip', 'zoom', 'push', 'dark']):
    place(fxL, fxR, whoosh(.75 if style != 'whip' else .55), c - .42, .9, -.3 if style == 'whip' else 0)
for c in [4.8, 22.8, 33.6]:
    place(fxL, fxR, swell(2.4 if c != 33.6 else 3.6), c - (2.4 if c != 33.6 else 3.6), .7)
for c in [4.8, 9.6, 22.8, 33.6]:
    place(fxL, fxR, subdrop(), c, .8 if c == 33.6 else .55)

# ---- UI sound effects (soft)
uiL, uiR = bufs()
def tok(f=1100, g=.18):
    n = int(.08 * SR); tt = np.arange(n) / SR
    x = np.sin(2*np.pi*f*tt) * np.exp(-tt/.012) + .5*np.sin(2*np.pi*f*.5*tt)*np.exp(-tt/.02)
    x += .15 * filt(rng.normal(size=n), 'band', [2000, 6000]) * np.exp(-tt/.003)
    return x * g
def key():
    n = int(.035 * SR); tt = np.arange(n) / SR
    return filt(rng.normal(size=n), 'band', [1800, 5200]) * np.exp(-tt / .006) * .05 * rng.uniform(.6, 1.1)
for c in [7.36, 11.22, 13.52, 14.83, 25.9]: place(uiL, uiR, tok(), c, 1, .1)
for k in range(24): place(uiL, uiR, key(), 11.78 + k * (1.68 / 24) + rng.uniform(-.015, .015), 1, -.1)
for k in range(46): place(uiL, uiR, key() * .8, 26.8 + k * (1.8 / 46) + rng.uniform(-.01, .01), 1, -.2)
place(uiL, uiR, pluck(88, .08), 13.55, 1, .3)           # colour swatch "blip"
place(uiL, uiR, whoosh(.45) * .5, 14.85, 1, -.2)          # drag
place(uiL, uiR, bell(79, 1.8, .1), 26.5, 1, 0)           # published
place(uiL, uiR, bell(84, 1.8, .08), 26.62, 1, .2)
for k in range(12):                                       # price counter
    tt = 30.24 + (1 - (1 - k / 12) ** 2) * 1.27
    place(uiL, uiR, tok(1400 + 40 * k, .07), tt, 1, 0)

# ------------------------------------------------------------------ mix music bed
gain_sec = np.ones(N)
musL = (padL * sc * .9 + bassL * sc + drL + arL * .9 + blL + outL)
musR = (padR * sc * .9 + bassR * sc + drR + arR * .9 + blR + outR)
musL, musR = reverb(musL, musR, .22)
fxL, fxR = reverb(fxL, fxR, .35)
uiL, uiR = reverb(uiL, uiR, .12)
# fade in / out
fi = np.minimum(1, T / .4); fo = np.clip((DUR - T) / 1.2, 0, 1)
musL *= fi * fo; musR *= fi * fo

def norm_rms(L, R, db):
    r = np.sqrt(((L**2 + R**2) / 2).mean()); g = 10 ** (db / 20) / r
    return L * g, R * g
musL, musR = norm_rms(musL, musR, -21)

# ------------------------------------------------------------------ voice
def load_vo(path):
    w = wave.open(path); a = np.frombuffer(w.readframes(w.getnframes()), '<i2') / 32768; sr = w.getframerate()
    a = resample_poly(a, 147, 80) if sr == 24000 else a
    a = filt(a, 'high', 85)
    # gentle compression
    env = np.sqrt(np.convolve(a**2, np.ones(441)/441, 'same')) + 1e-6
    gr = np.minimum(1, (0.12 / env) ** 0.35); a = a * gr
    return a
VO_T = [0.5, 5.3, 10.3, 12.8, 14.0, 16.45, 18.3, 19.3, 20.65, 23.8, 26.7, 30.2, 35.0, 35.9]

def build(vodir, out):
    voL, voR = bufs(); t_prev_end = 0
    for i, t0 in enumerate(VO_T):
        a = load_vo(f'{vodir}/l{i}.wav')
        t0 = max(t0, t_prev_end + .08); t_prev_end = t0 + len(a) / SR
        place(voL, voR, a, t0, 1, 0)
        print(f'  vo{i:02d} {t0:5.2f}-{t_prev_end:5.2f}')
    small = np.zeros(N); room = fftconvolve(voL, IR[0][:int(.5*SR)] * np.exp(-np.arange(int(.5*SR))/SR/.08))[:N]
    voL = voL + .06 * room; voR = voR + .06 * room
    voL, voR = norm_rms(voL, voR, -20.5)
    # ducking from voice envelope
    env = np.sqrt(np.convolve((voL**2), np.ones(2205)/2205, 'same'))
    act = (env > 10 ** (-42/20)).astype(float)
    # smooth: fast attack, slow release
    sm = np.zeros(N); a_c = np.exp(-1/(SR*.06)); r_c = np.exp(-1/(SR*.45)); y = 0.
    for s in range(0, N, 64):
        v = act[s:s+64].max(); c = a_c if v > y else r_c; c = c ** 64; y = v + (y - v) * c; sm[s:s+64] = y
    duck = 1 - .5 * sm   # about -6 dB
    L = musL * duck + fxL * .55 + uiL * .9 + voL
    R = musR * duck + fxR * .55 + uiR * .9 + voR
    # master: gentle limiter + loudness
    pk = max(np.abs(L).max(), np.abs(R).max())
    L, R = norm_rms(L, R, -16)
    L = np.tanh(L * 1.1) / 1.1 * .93; R = np.tanh(R * 1.1) / 1.1 * .93
    st = np.stack([L, R], 1)
    w = wave.open(out, 'wb'); w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes((np.clip(st, -1, 1) * 32767).astype('<i2').tobytes()); w.close()
    print('wrote', out, 'peak', round(float(np.abs(st).max()), 3))

if __name__ == '__main__':
    # music-only stem too
    st = np.stack([musL + fxL*.55 + uiL*.9, musR + fxR*.55 + uiR*.9], 1); st = st / np.abs(st).max() * .9
    w = wave.open('music_only.wav', 'wb'); w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes((st * 32767).astype('<i2').tobytes()); w.close()
    build(sys.argv[1], sys.argv[2])
