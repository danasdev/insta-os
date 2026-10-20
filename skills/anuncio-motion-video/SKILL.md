---
name: "anuncio-motion-video"
description: "Use quando pedirem um vídeo, reel, anúncio ou publi em motion graphics: de produto (estilo SaaS launch) ou institucional da empresa (texto cinético na batida de uma música). Define estilo e pegada, escreve roteiro (com locução para ElevenLabs quando houver) e renderiza MP4 16:9 e 9:16 para o Instagram."
---

# Anúncio em motion graphics

Leia antes a skill `marca`. Quando o pedido vier do `calendario-semanal`, entregue também a versão 9:16 com legenda, alt text e hashtags, e volte para o calendário.

## Dois modos

| | Produto | Institucional (empresa) |
|---|---|---|
| Pergunta que responde | "O que esse produto faz por mim?" | "Quem é essa empresa e por que confiar?" |
| Estrutura | gancho → produto → demo de UI → diferencial → ação → oferta → assinatura | história em atos: caos → forma → trabalho (portfólio) → números → processo → logo → CTA |
| Áudio | trilha sintetizada no BPM + narração | música real editada nos acentos, sem narração (o texto carrega a história) ou com narração curta |
| Visual | UI em 3D, cursor, zoom | tipografia cinética, cenas reais P&B, carrossel 3D do portfólio, logo de estilhaços |

O modo produto segue as seções abaixo. O modo institucional segue `references/institucional.md` (leia inteiro antes de começar), reaproveitando o render e o QA daqui.

Produz vídeos de divulgação de produto no estilo "product launch" de SaaS: texto cinético com blur, interfaces em perspectiva 3D, cursor clicando, zoom de câmera nas telas, transições com zoom/blur/flash, trilha sintetizada no grid do BPM e narração encaixada frase por frase. Entrega MP4 1920×1080 e/ou 1080×1920.

Não é geração de vídeo realista: tudo é HTML/CSS/JS renderizado quadro a quadro + áudio sintetizado/mixado em Python.

## Motor (sempre começar por aqui)

A pasta `engine/` na raiz do plugin tem tudo:

| Arquivo | O que é |
|---|---|
| `engine/exemplo-produto/index.html` | Anúncio completo de exemplo (marca fictícia "Nimbus", ~41s): `seek(t)` determinística, 7 cenas, transições, câmera, cursor, layout vertical via `body.portrait`. Ponto de partida. |
| `engine/render.py` | Renderiza quadros com Playwright (30 fps). `PAGE=caminho/index.html` (ou `URL=http://...`), `ORIENT=portrait` → 1080×1920. Aceita intervalo de quadros para rodar em paralelo. |
| `engine/music.py` | Trilha sintetizada, efeitos de UI, transições e mixagem com ducking: `python3 music.py <pasta_frases> <saida.wav>`. |
| `engine/tts.py` | Narração provisória local em PT-BR (Kokoro; instruções na seção 8). |

Copie o exemplo para uma pasta de trabalho do projeto e adapte. Para ver o estilo, renderize alguns stills do exemplo (`python3 engine/render.py stills 6 18 38`).

## Fluxo

Crie a lista de tarefas logo no início: briefing → identidade visual → pegada → roteiro (aprovação) → roteiro ElevenLabs → build → áudio → render → QA → entrega.

### 1. Briefing

Pergunte só o que não dá para descobrir sozinho (AskUserQuestion, até 4 perguntas por vez). Cubra:

1. **Produto e empresa**: nome, link do site/app, o que faz. Se for produto da própria marca, use a assinatura de vídeo do perfil.
2. **Quem define o conteúdo**:
   - o usuário diz o que apresentar (features, mensagem, CTA), ou
   - o agente extrai do site e escreve o roteiro inteiro (padrão quando o usuário não especifica).
3. **Pegada / segmento**: tech (padrão) ou outro ramo (ver tabela da seção 3).
4. **Formato e duração**: 16:9, 9:16 ou ambos; padrão ~35–45s.
5. **Referência de estilo**: um MP4 do usuário ou o exemplo do motor (padrão).
6. **Locução**: ElevenLabs (recomendado para versão final; o agente gera o roteiro com entonações), locutor humano, ou voz provisória local.

Se o usuário não estiver presente, assuma os padrões, diga quais assumiu e siga.

### 2. Identidade visual da empresa

Extraia do site, não invente:
- WebFetch para textos, proposta de valor, features, preços, CTAs.
- Navegador embutido (ou Chrome) para o visual. Rode JS que leia `getComputedStyle(body)`, as variáveis CSS de `:root` (cores, raio, sombras, easing), as fontes de `h1`/`body` e o logo (`img`/`svg`; para PNG, use `fetch` + `FileReader` para obter o data URL). Tire um screenshot da home.
- Telas atrás de login: **nunca crie conta nem digite senha**. Recrie a interface como mockup a partir do que o site descreve e avise o usuário.
- Se o logo não puder ser extraído com fidelidade, redesenhe em SVG aproximado e avise; peça o arquivo oficial.
- Fontes: Inter e Inter Display já vêm no sistema. npm/PyPI costumam estar bloqueados; use fontes do sistema (`fc-list`) com fallback parecido e avise.

Base escura padrão (quando a marca é monocromática ou não tem identidade definida): fundo `#0a0a0a` com grid sutil e glow radial, texto `#f5f5f5`, cinzas `#8a8a8a`/`#262626`, Inter Display nos títulos (tracking -0.035em), rótulos em caixa alta com letter-spacing .34em, botões pill brancos, marca d'água com o nome da marca no canto superior esquerdo.

### 3. Pegada do vídeo

O motor e a estrutura continuam os mesmos (base tech); o que muda é ritmo, música, transições e acabamento. Ajuste estes parâmetros:

| Segmento | BPM / música | Cortes e transições | Visual | Voz |
|---|---|---|---|---|
| **Tech / SaaS (base)** | 100 BPM, Fmaj7–Am7–Cmaj7–G, synths limpos, kick + palmas suaves | zoom-through, reveal, whip, push, fade escuro no logo; flash curto | escuro monocromático, UI em 3D, cursor | confiante, moderna |
| Alimentício / delivery | 105–115 BPM, maior, plucks quentes, ukulele/marimba sintetizada, percussão leve | cortes mais rápidos, pops com escala elástica (overshoot), menos blur | fundo claro ou quente, fotos/ilustrações do produto, cantos bem arredondados | calorosa, sorridente |
| Saúde / bem-estar | 80–90 BPM, pads longos, sem bateria pesada | fades e blur lentos, sem whip | claro, verdes/azuis suaves, muito respiro | calma, acolhedora |
| Finanças / fintech | 95–100 BPM, menor com resolução maior, sub discreto | precisos, push e zoom curtos, números em contador | escuro ou navy, dados e gráficos | séria, segura |
| Educação | 100–110 BPM, maior, leve e otimista | reveal e slide, destaques em marca-texto | claro, cores vivas controladas | didática, animada |
| Moda / beleza | 90–100 BPM, groove elegante | cortes no tempo, máscaras e wipes, tipografia serifada grande | editorial, alto contraste | sofisticada, pausada |
| Imobiliário / corporativo B2B | 85–95 BPM, piano + pad | movimentos lentos de câmera, fades | sóbrio, fotos amplas | institucional |
| Games / entretenimento | 120–128 BPM, energia alta | glitch, shake, flashes fortes | saturado, neon | empolgada |

Para pegadas fora da base, altere `BPM`, `CHORDS`/`ROOTS`, timbres e a bateria em `music.py`, e os estilos `TR`, curvas e intensidade de blur no template.

### 4. Referência do usuário (se mandar MP4)

```bash
ffprobe -v error -show_entries format=duration:stream=width,height,r_frame_rate -of default=nw=1 ref.mp4
ffmpeg -v error -i ref.mp4 -vf "fps=1,scale=384:-1,tile=6x6" -frames:v 1 sheet1.jpg   # 36s por folha; repita com -ss
```

Olhe as folhas e descreva o estilo em uma lista curta (paleta, tipografia, tipos de transição, câmera, ritmo de cortes). O vídeo de referência é só estilo: nunca replique marca, textos ou cenas de terceiros.

### 5. Roteiro (aprovar antes de construir)

Estrutura padrão (~40s, 100 BPM, cortes nas batidas):

| Cena | Batidas | Conteúdo |
|---|---|---|
| 1. Gancho | 8 | Frase-problema em texto cinético (ex.: "Construir um site não precisa ser complicado" com a palavra riscada e trocada) |
| 2. Produto | 8 | Apresenta o produto e o primeiro recurso visual |
| 3. Demo principal | 12–14 | Interface com cursor e zoom de câmera em 2–3 ações |
| 4. Diferencial | 8 | 3 frases curtas sincronizadas com trocas visuais |
| 5. Ação / resultado | 12 | Publicar, enviar, pagar: o momento "pronto" |
| 6. Oferta | 6 | Preço, plano ou prova social |
| 7. Assinatura | 12 | Logo, tagline, CTA, URL, assinatura do perfil |

Regras:
- Português falado rende ~2,5 palavras/s. Cada fala precisa caber na cena com ~0,4s de folga.
- Use somente fatos do site ou do usuário (preço, recursos). Dados de exemplo dentro de mockups (nomes de cliente fictícios, valores de planos de exemplo) devem ser declarados ao usuário na entrega.
- Mostre o roteiro como tabela (cena | tempo | visual | fala) e espere aprovação quando o usuário estiver presente.

### 6. Roteiro para ElevenLabs (entonações)

Entregue sempre três blocos, prontos para copiar:

1. **Com tags v3**: só as falas, uma por linha, **sem números, travessões de índice ou rótulos** (o ElevenLabs lê e transcreve tudo que estiver no texto), ex.:
```
[thoughtful] Construir um site... não precisa ser [slight pause] complicado.
[warm, upbeat] Com a Êidon, você começa por seções prontas.
```
   Tags em inglês entre colchetes: `[warm]`, `[confident]`, `[playful]`, `[smooth]`, `[impressed, smiling]`, `[calm, building up]`, `[proud, clear]`, `[inspiring, closing]`. Reticências criam pausas.
2. **Sem tags** (para Multilingual v2, que leria os colchetes), também só as falas.
3. **Tabela de direção** (# | intenção | como falar) separada dos blocos acima; é a única parte numerada e serve também para locutor humano.

Pronúncia:
- Nome de marca escrito como se fala em PT-BR, conforme a pronúncia do perfil (ex.: "Nimbus" lido como "Nímbus" → escreva `Nímbus`). Pergunte quando houver dúvida.
- Números por extenso ("vinte e nove reais"), nunca "R$ 29".
- Siglas soletradas se a voz errar ("agá-tê-eme-ele").

Oriente o usuário a gerar **uma frase por arquivo** (nomeie os arquivos na ordem) ou um arquivo único com pausas de ~0,5s entre frases, a filtrar vozes do Brasil e a testar 2–3 vozes com a frase 01.

### 7. Build da animação

Copie `engine/exemplo-produto/index.html` para `index.html` e adapte. Arquitetura:

- `seek(t)` posiciona tudo de forma determinística; nada de CSS transitions/animations. Cada cena é uma função `sN(t)`.
- Linha do tempo: `NEWC` contém os cortes reais no grid musical (múltiplos de 0,6s a 100 BPM). `M(i,t)` remapeia o tempo "autorado" de cada cena para o grid; em cena nova, prefira escrever direto no tempo global (como `s5`).
- Helpers: `kin(sel,t,start)` (texto palavra a palavra com blur), `fade`, `P(t,start,dur,ease)`, `camAt(keyframes,t)` para câmera, `mix()` para cores.
- Transições em `TR` por corte: `zoom`, `reveal`, `whip`, `push`, `dark`; o flash (`#flash`) entra nos cortes com zoom.
- Câmera dentro de UI: keyframes `[t, escala, focoX, focoY]` em coordenadas locais da janela; o foco é levado ao centro da tela.
- Cursor: `TRACKS` com waypoints que podem mirar seletores (`sel`), assim o cursor acompanha elementos que se movem ou têm zoom; `clicks` geram ripple.
- Mockups de UI com conteúdo realista (nada de lorem ipsum).
- Vertical: `body.portrait` no CSS reposiciona tudo; câmera mais forte no portrait (`PORT ? .68*cs^1.5 : cs`); coordenadas fixas do cursor convertidas em `resolve()`. Títulos quebram em 2 linhas (largura ~940px).
- Sincronize: cada clique ou ação visual cai na palavra correspondente da narração; trocas de estado (ex.: temas) caem em batidas.

### 8. Áudio

`music.py` (edite as constantes do projeto): `BPM`, `CHORDS`, `ROOTS`, `CUTS`, `END_BAR_T`, a lista de cortes para whoosh/swell/subdrop, os tempos de efeitos de UI (cliques, digitação, sucesso, contador) e `VO_T` (início de cada frase). Ele já faz:
- pad com filtro abrindo na intro, bateria entrando no 2º corte, arpejo com delay, sinos nas trocas, acorde final no logo;
- efeitos de UI suaves (cliques "tok", teclas baixas);
- ducking de ~6 dB da música sob a voz e limiter suave; níveis finais ~-16 dB RMS sem clipping.

Narração provisória local (só para guia; avise que soa sintética):
```bash
mkdir -p ~/tts && cd ~/tts
R=https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0
curl -sSL -o kokoro.onnx $R/kokoro-v1.0.onnx; curl -sSL -o voices.bin $R/voices-v1.0.bin
curl -sSL -o piper.tgz https://github.com/rhasspy/piper/releases/download/2023.11.14-2/piper_linux_x86_64.tar.gz && tar xzf piper.tgz && chmod +x piper/espeak-ng
git clone -q --depth 1 https://github.com/thewh1teagle/kokoro-onnx src   # vocab em src/src/kokoro_onnx/config.json
python3 tts.py frases.json pm_alex saida_alex 1.0   # vozes PT-BR: pm_alex, pm_santa, pf_dora
```
(PyPI costuma estar bloqueado; o `onnxruntime` já instalado basta.)

Narração do usuário (arquivo único): detecte as pausas, mapeie trechos → frases pelo padrão de pausas e durações, e corte com 50ms antes / 140ms depois e fades curtos.
```bash
ffmpeg -i vo.mp3 -af silencedetect=noise=-40dB:d=0.25 -f null - 2>&1 | grep silence_
```
Confirme o mapeamento por âncoras (frases com pausas internas características) e, na entrega, peça ao usuário para avisar se alguma frase caiu errada.

Quando só o áudio mudar, remonte sem re-renderizar: `ffmpeg -i video.mp4 -i mix.wav -map 0:v -map 1:a -c:v copy -c:a aac -b:a 224k -shortest out.mp4`.

### 9. Render

```bash
python3 render.py stills 3.0 7.5 11.5 ...            # stills nos momentos-chave
python3 render.py full 0 615 & python3 render.py full 615 1230 &   # em paralelo
ORIENT=portrait python3 render.py full                 # vertical (frames_p/)
ffmpeg -framerate 30 -i frames/f%05d.jpg -i mix.wav -c:v libx264 -preset slow -crf 17 -pix_fmt yuv420p -c:a aac -b:a 224k -shortest -movflags +faststart final_16x9.mp4
```
Rode o render em segundo plano e espere com um loop sobre `pgrep` (sleep simples é bloqueado). ~1230 quadros levam ~3–5 min por orientação.

### 10. QA (antes de entregar)

- Contact sheets rotuladas com o tempo, incluindo **momentos de transição** (corte ±0,15s) e o meio de cada zoom de câmera. Procure:
  - filhos de containers sem `position:absolute` virando blocos empilhados (foi o bug do card Hero: use `.v>div{position:absolute}`);
  - texto cortado ou sobreposto quando a câmera aproxima (no vertical, esconda o título da cena quando a câmera desce);
  - elementos cortados na borda no layout vertical;
  - cursor fora do alvo.
- Áudio: RMS por cena, pico < 0,99, zero amostras clipadas, voz ~8–12 dB acima da música durante a fala; espectrograma (`showspectrumpic`) para ver agudos ásperos.
- Texto fora da tela: rode a varredura de `references/institucional.md` (seção "Texto que sai da tela") nas duas orientações; o ajuste automático de tamanho só vale depois que as fontes carregarem (`document.fonts.load` de cada família antes de medir).
- Você não consegue ouvir: diga isso, aponte os pontos de emenda da música com o tempo exato e peça ao usuário para conferir.

### 11. Entrega

- `SendUserFile` com os MP4 (`display: render`); nomes como `<produto>_anuncio_16x9.mp4` e `_9x16.mp4`.
- Em poucas linhas: o que mostra, o que foi assumido, o que é mockup/aproximado (logo, telas, dados de exemplo) e o próximo passo natural (versão vertical, corte de 15s, trocar locução).
- Se a locução final ainda não existe, entregue junto o roteiro ElevenLabs da seção 6.

## Para o Instagram

Antes do roteiro, leia `playbook-instagram/references/ganchos-e-retencao.md` e `psicologia.md`: o quadro 1 e os 3 primeiros segundos seguem aquelas regras, e o fim corta logo após a recompensa.

- Entregue sempre a 9:16 (1080×1920) para reels; a 16:9 é opcional (site, YouTube, LinkedIn).
- Área segura do reel: nada importante nos 250px de cima e de baixo nem nos ~120px da direita.
- Corte de 15s: gancho (3s) + melhor trecho visual (9s) + assinatura com CTA (3s), cortado nas batidas.
- Capa do reel: um quadro de impacto com o título na fonte de títulos da marca (exporte o frame em JPG 1080×1920).
- MP4 até ~60MB para envio pelo chat (acima disso, aumente o CRF para 26–29).
- Legenda: gancho na primeira linha, 1 CTA, 3–5 hashtags, alt text.
- Música comercial (ex.: faixas de artistas): avise que uso comercial precisa de licença ou de áudio da biblioteca do Instagram; entregue sempre também uma versão com trilha própria sintetizada.

## Armadilhas conhecidas

- Rede: só GitHub e poucos hosts saem do container; npm/PyPI/HF podem falhar. Planeje com o que já existe (ffmpeg, Playwright/Chromium, numpy, scipy, onnxruntime, fontes do sistema).
- `<a download>`, autoplay com som etc. não importam aqui: o produto é o MP4.
- Não use `will-change` em elementos com zoom (rasteriza borrado).
- Blur grande em camadas fullscreen deixa o render mais lento, mas é aceitável; evite empilhar vários blurs no mesmo quadro.
- Em vídeos de produtos da própria marca, mantenha a assinatura e a marca d'água do perfil; para clientes externos, pergunte.