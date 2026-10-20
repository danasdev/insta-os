# Motor de vídeo

Animação em HTML/CSS/JS com `seek(t)` determinística, renderizada quadro a quadro com Playwright e montada com ffmpeg.

```bash
pip install playwright numpy scipy   # se ainda não tiver; ffmpeg e Chromium também
python3 render.py stills 6 18 38                         # confere quadros-chave do exemplo
python3 render.py full 0 620 & python3 render.py full 620 1230 &   # render em paralelo (30 fps)
ORIENT=portrait python3 render.py full                   # versão 9:16 (pasta frames_p/)
python3 music.py <pasta_com_l0.wav_l1.wav...> mix.wav    # trilha + narração com ducking
ffmpeg -framerate 30 -i frames/f%05d.jpg -i mix.wav -c:v libx264 -crf 18 -pix_fmt yuv420p -c:a aac -shortest anuncio.mp4
```

- `PAGE=caminho/para/index.html` escolhe outro template; `URL=http://127.0.0.1:8765/index.html` quando o template usa `mask-image` ou `fetch` (sirva a pasta com `python3 -m http.server 8765`).
- `exemplo-produto/` é um anúncio completo de uma marca fictícia ("Nimbus"). Copie e adapte.
- `tts.py` gera narração provisória local em PT-BR (Kokoro); veja a skill `anuncio-motion-video` para baixar o modelo.
- O passo a passo completo (roteiro, pegada por segmento, edição na batida, QA) está nas skills `anuncio-motion-video` e `playbook-instagram`.
