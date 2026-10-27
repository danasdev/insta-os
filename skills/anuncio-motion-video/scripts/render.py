#!/usr/bin/env python3
"""Renderiza um index.html com seek(t) e DURATION em quadros JPG (Playwright/Chromium).

Exemplos:
  python3 render.py stills 0 1.2 3.0 7.5 --html index.html          # stills nos momentos-chave
  python3 render.py full --draft                                     # rascunho 540p/15fps (aprovação)
  python3 render.py full --start 0 --end 300 & python3 render.py full --start 300 --end 600   # em paralelo
  python3 render.py full --orient landscape                          # 1920x1080
  python3 render.py info                                             # só mostra DURATION e erros do console

Padrão: vertical 1080x1920 (9:16 primeiro), 30 fps, pasta frames_p/ (ou frames/ no horizontal).
--draft renderiza a 0,5x (device scale factor) e 15 fps em frames_draft_p/ — o layout continua
o de 1080x1920, só o arquivo sai menor e ~4x mais rápido.
Se a página definir window.clipsReady (clipes de vídeo pré-carregados), o render espera por ela.
Depois de mudar a duração da animação, apague a pasta de quadros antes: sobra de quadros velhos entra no MP4.
"""
import argparse, os, sys
from pathlib import Path
from playwright.sync_api import sync_playwright

ap = argparse.ArgumentParser()
ap.add_argument("mode", choices=["stills", "full", "info"])
ap.add_argument("times", nargs="*", type=float, help="stills: tempos em segundos")
ap.add_argument("--html", default="index.html")
ap.add_argument("--orient", choices=["portrait", "landscape"], default=os.environ.get("ORIENT", "portrait"))
ap.add_argument("--draft", action="store_true", help="0,5x e 15 fps, para aprovar movimento e ritmo")
ap.add_argument("--fps", type=int, default=None)
ap.add_argument("--start", type=int, default=0, help="primeiro quadro (no fps escolhido)")
ap.add_argument("--end", type=int, default=None, help="quadro final (exclusivo)")
ap.add_argument("--quality", type=int, default=None)
ap.add_argument("--out", default=None, help="pasta de saída")
a = ap.parse_args()

portrait = a.orient == "portrait"
W, H = (1080, 1920) if portrait else (1920, 1080)
fps = a.fps or (15 if a.draft else 30)
quality = a.quality or (70 if a.draft else 93)
scale = 0.5 if a.draft else 1
suffix = "_p" if portrait else ""
out = a.out or (("frames_draft" if a.draft else "frames") + suffix if a.mode == "full" else "stills" + suffix)

html = Path(a.html).resolve()
if not html.exists():
    sys.exit(f"não achei {html}")

with sync_playwright() as p:
    b = p.chromium.launch(args=["--force-device-scale-factor=1"])
    ctx = b.new_context(viewport={"width": W, "height": H}, device_scale_factor=scale)
    pg = ctx.new_page()
    msgs = []
    pg.on("console", lambda m: msgs.append(m.text))
    pg.on("pageerror", lambda e: msgs.append("ERR " + str(e)))
    pg.goto(html.as_uri())
    pg.evaluate("document.fonts.ready")
    if pg.evaluate("typeof window.clipsReady !== 'undefined'"):
        pg.wait_for_function("window.clipsReady === true", timeout=120000)
    pg.wait_for_timeout(500)

    D = pg.evaluate("DURATION")
    if a.mode == "info":
        print(f"DURATION={D}s  viewport={W}x{H}  fps={fps}  quadros={int(D*fps)}")
    elif a.mode == "stills":
        os.makedirs(out, exist_ok=True)
        for t in a.times:
            pg.evaluate(f"seek({t})")
            pg.screenshot(path=f"{out}/t{t:06.2f}.jpg", type="jpeg", quality=85)
        print(f"{len(a.times)} stills em {out}/")
    else:
        os.makedirs(out, exist_ok=True)
        n = int(D * fps)
        z = min(a.end if a.end is not None else n, n)
        for i in range(a.start, z):
            pg.evaluate(f"seek({i / fps})")
            pg.screenshot(path=f"{out}/f{i:05d}.jpg", type="jpeg", quality=quality)
        print(f"quadros {a.start}..{z - 1} de {n} em {out}/ ({fps} fps)")
    if msgs:
        print("\n".join(msgs[:10]))
    b.close()
