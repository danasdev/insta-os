# Render: rascunho → aprovação → final

Um render completo leva ~3–5 min por orientação no modo produto e 20–25 min no institucional. Por isso, o movimento e o ritmo se aprovam num **rascunho** antes.

## 1. Stills nos momentos-chave

```bash
python3 scripts/render.py stills 0 1.2 3.0 7.5 11.5 --html index.html   # vertical por padrão → stills_p/
```

Olhe quadro 1, a virada de cada cena, o meio de cada zoom e o último quadro. Corrija layout aqui, antes de renderizar qualquer sequência.

## 2. Rascunho (aprovação do movimento)

```bash
python3 scripts/render.py full --draft --html index.html                # 540x960, 15 fps → frames_draft_p/
ffmpeg -framerate 15 -i frames_draft_p/f%05d.jpg -i mix.wav -c:v libx264 -preset veryfast -crf 26 -pix_fmt yuv420p -c:a aac -b:a 160k -shortest draft_9x16.mp4
```

Mostre o rascunho ao usuário com `SendUserFile`. Diga que é rascunho (baixa resolução, 15 fps) e peça aprovação de ritmo, textos e cortes. Mude o que for preciso e refaça só o rascunho. Sem o usuário presente, rode o QA (`qa.md`) no rascunho e siga para o final.

## 3. Render final

```bash
# em paralelo, por faixas de quadros (30 fps; 20s = 600 quadros)
python3 scripts/render.py full --html index.html --start 0   --end 300 &
python3 scripts/render.py full --html index.html --start 300 --end 600 &
# horizontal, se pedido (1920x1080 → frames/)
python3 scripts/render.py full --html index.html --orient landscape
ffmpeg -framerate 30 -i frames_p/f%05d.jpg -i mix.wav -c:v libx264 -preset slow -crf 17 -pix_fmt yuv420p -c:a aac -b:a 224k -shortest -movflags +faststart final_9x16.mp4
```

- Rode em segundo plano (`run_in_background`) e espere com um loop sobre `pgrep` (sleep simples é bloqueado).
- Se a duração da animação mudou, **apague as pastas de quadros antes**: quadros velhos sobrando entram no MP4.
- Ao mudar só um trecho, re-renderize só a faixa de quadros afetada (`--start`/`--end`).
- Com clipes de vídeo pré-carregados, o render espera `window.clipsReady` (o `render.py` faz isso sozinho).
- Se a trilha mudou e a imagem não, remonte sem re-renderizar: `ffmpeg -i video.mp4 -i mix.wav -map 0:v -map 1:a -c:v copy -c:a aac -b:a 224k -shortest out.mp4`.

## 4. Cortes e capa

- **Corte de 15s:** gancho (3s) + melhor trecho visual (9s) + assinatura com CTA (3s), cortado nas batidas. Prefira renderizar a faixa de quadros em vez de cortar o MP4 final no meio de uma batida.
- **Capa do reel:** um quadro de impacto com o título na fonte de títulos da marca; exporte o frame em JPG 1080×1920 com `render.py stills`.
- **Tamanho:** MP4 até ~60MB para envio pelo chat; acima disso, CRF 26–29.

## Sem o motor

`scripts/render.py` não depende do `engine/`: só precisa de um `index.html` com `seek(t)` e `DURATION`. Se o `index.html` for construído do zero, siga a arquitetura de `produto.md` ("Build da animação") e teste com `render.py info` antes de renderizar.
