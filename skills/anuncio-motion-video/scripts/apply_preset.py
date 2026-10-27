#!/usr/bin/env python3
"""Aplica um preset de pegada (BPM, acordes, baixo) no music.py do motor (engine/music.py).

Uso:
  python3 apply_preset.py <music.py> <segmento> [--presets presets.json]
  python3 apply_preset.py --list

Só reescreve as linhas `BPM = ...`, `CHORDS = ...` e `ROOTS = ...`. Os demais
campos do preset (som, transições, blur, visual, voz) são impressos para você
levar ao template e ao roteiro. As constantes que dependem da duração
(DUR, CUTS, END_BAR_T, VO_T, tempos de UI) continuam por sua conta.
"""
import argparse, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))

ap = argparse.ArgumentParser()
ap.add_argument("music", nargs="?")
ap.add_argument("segmento", nargs="?")
ap.add_argument("--presets", default=os.path.join(HERE, "presets.json"))
ap.add_argument("--list", action="store_true")
a = ap.parse_args()

presets = {k: v for k, v in json.load(open(a.presets, encoding="utf-8")).items() if not k.startswith("_")}
if a.list or not (a.music and a.segmento):
    print("segmentos:", ", ".join(presets))
    sys.exit(0 if a.list else 2)
if a.segmento not in presets:
    sys.exit(f"segmento '{a.segmento}' não existe. Opções: {', '.join(presets)}")

p = presets[a.segmento]
src = open(a.music, encoding="utf-8").read()

def sub(name, value, text):
    pat = re.compile(rf"^{name}\s*=\s*.*$", re.M)
    if not pat.search(text):
        sys.exit(f"não achei a linha '{name} = ...' em {a.music}")
    line = f"{name} = {value}"
    if name == "CHORDS":
        line += f"   # {p['acordes_nome']}"
    return pat.sub(lambda m: line, text, count=1)

src = sub("BPM", p["bpm"], src)
src = sub("CHORDS", json.dumps(p["chords"]).replace(" ", ""), src)
src = sub("ROOTS", json.dumps(p["roots"]).replace(" ", ""), src)
open(a.music, "w", encoding="utf-8").write(src)

beat = 60 / p["bpm"]
print(f"preset '{a.segmento}' aplicado em {a.music}")
print(f"  BPM {p['bpm']}  (batida {beat:.4f}s, compasso {4*beat:.4f}s)")
print("  CORTES: recalcule CUTS/END_BAR_T como múltiplos de", round(beat, 4), "s")
for k in ("som", "transicoes", "flash", "blur", "visual", "voz"):
    print(f"  {k}: {p[k]}")
