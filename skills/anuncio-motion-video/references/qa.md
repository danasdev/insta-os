# QA antes de entregar

Rode no rascunho e de novo no render final, nas duas orientações quando houver 16:9.

## 1. Varredura automática (texto e área segura)

`scripts/qa_sweep.js` percorre a animação de 0,1 em 0,1s e aponta texto que sai da tela e, no 9:16, texto que invade a área segura do reel (250px em cima e embaixo, 120px à direita).

```python
from pathlib import Path
from playwright.sync_api import sync_playwright
js = Path("scripts/qa_sweep.js").read_text()
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={"width": 1080, "height": 1920})
    pg.goto(Path("index.html").resolve().as_uri())
    pg.evaluate("document.fonts.ready")
    # espere as fontes de cada família ANTES de medir, senão a fonte reserva (mais estreita) engana a medida:
    pg.evaluate("Promise.all([document.fonts.load(\"100px 'SuaFonteDeTitulo'\"), document.fonts.load(\"700 100px 'Inter'\")])")
    pg.evaluate(js)
    print(pg.evaluate("qaSweep({step:0.1})"))
```

Cada ocorrência vem com `from`/`to` (segundos), `kind` (`offscreen` ou `safe`), o texto e o retângulo. Corrija e rode de novo até zerar. Exceções legítimas (palavra que desliza de fora de propósito, marca d'água, legenda queimada) recebem `data-qa-ignore` no elemento; só podem estourar durante a entrada e a saída.

Ajustes comuns:
- A largura disponível depende da posição: centralizado = `2·min(x, W−x) − 2·margem`; alinhado à esquerda = `W − x − margem`. Divida por ~1,09 para caber o zoom da animação.
- O ajuste automático de tamanho de fonte só vale depois que as fontes carregarem; o render espera essa flag.

## 2. Contact sheets

Monte folhas rotuladas com o tempo, incluindo **momentos de transição** (corte ±0,15s) e o meio de cada zoom de câmera, e olhe:
- filhos de containers sem `position:absolute` virando blocos empilhados (bug do card Hero: use `.v>div{position:absolute}`);
- texto cortado ou sobreposto quando a câmera aproxima (no vertical, esconda o título da cena quando a câmera desce);
- elementos cortados na borda no layout vertical;
- cursor fora do alvo;
- quadro 1: já tem texto grande e movimento? (nada de logo, tela preta ou intro).

## 3. Áudio

- RMS por cena, pico < 0,99, zero amostras clipadas, voz ~8–12 dB acima da música durante a fala (música −18 a −22 dB sob a voz); níveis finais ~-16 dB RMS.
- Espectrograma (`showspectrumpic`) para ver agudos ásperos.
- Você não consegue ouvir: diga isso, aponte os pontos de emenda da música com o tempo exato e peça ao usuário para conferir.

## 4. Entrega

Só entregue com a varredura zerada (ou com cada exceção explicada), as contact sheets sem defeito e o áudio medido. Na mensagem final, liste o que foi assumido e o que é mockup.
