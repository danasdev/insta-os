# Vídeos de referência (estilo, animação, ritmo)

Três vídeos de terceiros guardados para consulta de **estilo e movimento**. Nunca copie marca, texto, telas, personagens ou trilha deles; reproduza o *tipo* de movimento com o motor HTML, nas cores e fontes da marca do vídeo.

| Nome | Original | O que é | Por que olhar |
|---|---|---|---|
| `saas` | youtube.com/watch?v=J6A7JcbkWvM | Lançamento de SaaS (plataforma de gestão de resíduos), 73s, 16:9 | O melhor exemplo de **demo de produto contínua**: só 7 cortes secos em 73s; tudo vira transição de forma, zoom ou câmera |
| `showreel` | youtube.com/watch?v=N8Shh0mo8vw | Showreel de estúdio de motion, 46s | **Montagem rápida e editorial**: 67 cortes (média 0,7s), creme + violeta + acento verde, tipografia de revista |
| `sizzle` | youtube.com/watch?v=r0y_C24-e5Y | Sizzle reel de agência, 83s | **Institucional na batida**: troca de palavra por tempo, logo em 15 estilos em 10s, 3D de vidro, partículas |

Os vídeos não vêm no plugin (são de terceiros). A análise abaixo basta para usar os padrões; para ver um movimento, assista no link ou peça ao usuário para anexar o MP4 e gere folhas de contato com o tempo em cada quadro (2 quadros/s, 15s por folha):

```bash
F=$(fc-list | grep -i dejavusans.ttf | head -1 | cut -d: -f1)
ffmpeg -v error -ss 0 -t 15 -i saas.mp4 -vf "fps=2,scale=384:-2,drawtext=fontfile=$F:text='%{pts\:hms\:0}':x=4:y=4:fontsize=16:fontcolor=yellow:box=1:boxcolor=black@0.6,tile=6x5" -frames:v 1 saas_s0.jpg
```

Para um movimento em detalhe, uma folha a 10 fps só do trecho:

```bash
ffmpeg -v error -ss 46 -t 3 -i saas.mp4 -vf "fps=10,scale=384:-2,tile=6x5" -frames:v 1 trecho.jpg
```

## O que os três têm em comum (regras de estilo)

1. **Uma cor só, mais neutros.** Violeta + preto + lavanda/branco (SaaS e sizzle); creme + violeta com um acento pontual (showreel). A cor de destaque vai em **uma palavra** por frase ("Waste**Protection**", "everything you ***need***", "Built around **You**"). Numa marca monocromática, o destaque vai em cinza claro ou na cor do cliente.
2. **Contraste de escala.** Texto pequeno e centralizado com muito ar, cortado por palavras gigantes que estouram o quadro (rolando na horizontal ou cortadas na borda). Os dois tamanhos alternam a cada 1–3s.
3. **Nada fica parado.** Mesmo telas "paradas" derivam (drift lento de 2–4%, parallax de ícones). Texto estático por mais de ~1,5s não aparece.
4. **Transição por forma, não por corte.** Uma forma cresce até cobrir o quadro e vira o fundo da cena seguinte (estrela de 4 pontas, círculo, anel, card que vira tela cheia). No SaaS isso substitui quase todos os cortes.
5. **UI sempre clara e limpa contra fundo de cor**, com contornos/callouts destacando o elemento de que a fala trata, e elementos "saltando" da tela (cards de KPI que saem do dashboard).
6. **Ritmo.** Demo de produto: trechos longos e contínuos (6–10s) guiados por cursor e câmera. Institucional/showreel: troca a cada batida ou meia batida (0,3–0,7s), acelerando no clímax (logo em vários estilos) e parando seco antes do CTA.
7. **Final em três tempos:** CTA curto ("Get started", "Visit site.com" com o domínio na cor de destaque) → fundo preto, ícone do logo desenha → wordmark sai de dentro do ícone. Fecha em silêncio ou com um "tum".
8. **Áudio alto.** As três trilhas estão masterizadas entre −9 e −7 dB RMS (a nossa mixagem padrão é −16). Antes de entregar, meça a loudness integrada (`ffmpeg -i mix.wav -af loudnorm=print_format=summary -f null -`) e mire em ~−14 LUFS, com o limiter evitando clipping, para o vídeo não soar fraco ao lado dos outros no feed.

## Padrões por vídeo (com tempo para conferir na folha)

### SaaS launch (`saas`)

| Tempo | Padrão | Como fazer no motor |
|---|---|---|
| 0–3s | **Typewriter com cursor em bloco**, texto pequeno; a última palavra entra em cor de destaque com fade | `typeCaret` (abaixo) |
| 3–6s | Faixa de **onda de partículas** no rodapé; letras espalhadas pela tela **convergem** e formam "Powered by AI" | onda: canvas com pontos em `sin(x·k + t·w)`; letras: `scatterAssemble` |
| 6,5–9,5s | **Palavra gigante rolando** na horizontal (maior que o quadro), gradiente branco→violeta | `marquee` (abaixo); no 9:16, duas linhas empilhadas |
| 10–12,5s | Nome do produto no centro, **anel escuro** expandindo, **ícones em tiles flutuando** em parallax | anel: `radial-gradient` com raio em função de t; tiles: 8–12 divs com drift e profundidade |
| 13–15s | Dashboard claro sobe com título em 2 linhas (2ª em cor); **contornos destacando** elementos | retângulo com `outline` animando de 0 a 100% de opacidade sobre o elemento |
| 15–24s | Janela entra pelo canto, **câmera segue o cursor** entre páginas (navegação real), sem corte | já existe (`camAt` + `TRACKS`) |
| 24,5–27,5s | **Cards de KPI saltam da tela** (o card sai do dashboard, cresce e ganha contorno) enquanto o resto desfoca | `pullOut` (abaixo) |
| 28–29,5s | Várias telas em **leque isométrico**; o fundo vira escuro | `rotateX(55deg) rotateZ(-30deg)` com `translateZ` por tela |
| 30–35s | Mapa escuro, **rota se desenhando**, pulso de luz no destino, cards de informação | SVG `stroke-dashoffset` + círculo com escala/opacidade pulsando |
| 35–38s | Mapa encolhe para um card; frase **palavra por palavra em posições espalhadas** que depois se alinham ao centro | `scatterAssemble` por palavra |
| 38–39s | Nome da feature gigante e cortado (só "Arlo" ocupando o quadro) | `font-size` > largura do quadro, `overflow:hidden` |
| 40–46s | Caixa de prompt de IA; perguntas digitadas uma após a outra, as anteriores **sobem e somem em pilha** | `typeCaret` + `stackCards` (de `cenas-jitter.md`) invertido |
| 46–48s | **Estrela de 4 pontas** cresce e cobre a tela (transição); depois vira **linha de onda** tracejada | SVG path da estrela com `scale` de 0 → 40; onda: path animado |
| 49,5–51,5s | Palavra gigante atrás, **celular sobe** na frente com notificações empilhando | celular em div com `translateY`; notificações com `stackCards` |
| 52–54s | UI em esqueleto (blocos sem texto) com **cursores nomeados** ("Operator 1/2") | divs cinza + cursores com etiqueta |
| 54–58,5s | Quadrados arredondados **viram fotos** e formam um mosaico; uma foto cresce com etiqueta pill | `border-radius` e `background-image` com fade; grid com `scale` no foco |
| 58,5–61s | Mosaico encolhe num ícone → estrela → estrela cobre a tela com a frase de efeito | sequência de `scale` com troca de forma no ponto mínimo |
| 61–63s | **Nuvem de tags** (pills com features) em fileiras com desfoque de profundidade, rolando | 3–4 fileiras com velocidades diferentes; `blur` maior nas de trás |
| 64–71,5s | "Get started" sobre o contorno do logo → horizonte de planeta com brilho → URL com o domínio em cor → preto, ícone desenha, wordmark sai do ícone | `stroke-dashoffset` no ícone; wordmark com `clip-path` abrindo da esquerda |

### Showreel de estúdio (`showreel`)

| Tempo | Padrão | Como fazer no motor |
|---|---|---|
| 0–1,5s | Palavra gigante cortada deslizando; depois a mesma palavra centralizada com **flash de luz colorida** atrás | `marquee` + `radial-gradient` que explode e some em 0,3s |
| 2–3,5s | **Layout editorial**: rótulo pequeno, número grande, fios finos, blocos de texto miúdo | grid tipo revista; fios com `scaleX` de 0 → 1 |
| 4–6s | Vídeos em **cards verticais arredondados** entrando em fila; **número rolando** (odômetro) | `odometer` (abaixo) |
| 6,5–8,5s | Montagem de telas **inclinadas** com palavra gigante atrás | leque isométrico do SaaS, mais rápido |
| 8,5–11,5s | Prompt de IA ("O que você quer criar?") com palavras em cor e borda em gradiente; pill "Inicializando…" | `typeCaret`; borda: `background: linear-gradient` + `mask` |
| 12–15s | **Manifesto digitado** em parágrafo grande que rola, com uma palavra manuscrita no meio | `typeCaret` + fonte script só naquela palavra |
| 15–17s | Título alinhado à esquerda; **conversa de celular** responde ("A gente resolve") | balões entrando com `easeOutBack` |
| 17,5–20s | Pixels/quadradinhos em **glitch**; domínio com letras trocadas por pontos que pulam | grade de quadrados com opacidade aleatória *semeada* (determinística) |
| 20,5–21,5s | Logo girando; **fundo inverte preto↔branco** no acento | troca de `--bg`/`--fg` num quadro |
| 22–23s | **Paleta de cores** se abrindo em amostras | 5 cards com `translateX` escalonado |
| 23,5s | Lista vertical de palavras, só a do meio preenchida (as outras em contorno) | `-webkit-text-stroke` nas de fora |
| 24–26s | Texturas P&B e imagens aéreas com **palavras bem espaçadas** atravessando o quadro | `justify-content: space-between` numa linha |
| 30–32s | **Preço/número rolando** e "99,9%" gigante com números fantasma em contorno atrás; cantoneira vermelha | `odometer` + cópia em contorno com escala maior |
| 33–35s | **Abas horizontais** passando com um **cursor de mão grande** (ilustrado) clicando | fileira com `translateX` por batida; cursor SVG com `scale` no clique |
| 37,5–38,5s | Texto em **gradiente dourado** em fundo quente; avatar estoura com a frase | `background-clip:text` |
| 42–46s | CTA pill com contorno em fundo creme e **dip lento para preto** | overlay preto com opacidade 0 → 1 em ~2s |

### Sizzle de agência (`sizzle`)

| Tempo | Padrão | Como fazer no motor |
|---|---|---|
| 0–4s | Gradiente violeta em malha; "Oi, somos…" pequeno → nome **digitado gigante** → **encolhe para dentro de um pill branco** | `typeCaret` + `pillSnap` (abaixo) |
| 4,5–7s | Palavra **selecionada** (caixa de seleção de texto) e barras em gradiente surgindo dos lados | div de seleção com `scaleX` atrás da palavra |
| 7,5–10,5s | **Anel de partículas explodindo** em fundo escuro, com palavras no centro | canvas com partículas em posição `f(t, seed)` (sem aleatório por quadro) |
| 10,5–11,5s | Palavra em **anel 3D** girando (cilindro de texto) | N cópias com `rotateY(i·360/N) translateZ(r)` no pai girando |
| 12–15,5s | "Criamos motion para" + **uma palavra trocando por batida** (Eventos / Explicativos / Trailers / Social) | `wordSwap` (abaixo) |
| 15,5–17,5s | "tudo que você *quer*" → "*precisa*": troca só a palavra de destaque, em itálico e cor | `wordSwap` com 2 itens |
| 18–22s | Logo em **anéis concêntricos** girando; ícone do app com **órbitas de avatares** com crachá | anéis SVG; avatares em `rotate(θ) translate(r) rotate(-θ)` |
| 22–23s | Título grande em cinza com **faixa de desfoque passando** sobre ele | `backdrop-filter: blur` numa faixa que atravessa |
| 25–26s | Um **ponto cresce e vira a letra "o"** da frase | círculo com `scale`, depois troca para o texto no mesmo lugar |
| 26–29s | **Piso em grade 3D escuro**, telas flutuando inclinadas, esfera de vidro, moldura brilhante | grade: `linear-gradient` repetido com `rotateX(70deg)` |
| 29–30,5s | Linhas curvas ligando avatares (rede); **etiquetas tortas** como adesivos | SVG path + pills com `rotate(-12..12deg)` |
| 33,5–35s | Documentos em leque → **pastas se multiplicando** até cobrir o quadro | grade que dobra a cada batida (`scale` do pai diminui) |
| 35–37s | **Linha do tempo com etapas** preenchendo e checks marcando | barra com `scaleX` + checks com `easeOutBack` |
| 42–45s | Diagrama de fluxo: nós ligados, pill "Enviando" → "Enviado" | troca de rótulo no acento |
| 49–59s | **Logo em ~15 estilos/materiais**, um por batida (cromado, vidro, contorno, adesivo, giz, inflado…) | `logoMontage` (abaixo): o mesmo SVG com filtros/fundos diferentes por batida |
| 62–66s | Feixes de luz; **cards de vidro 3D** girando com ícones; mosaico de fotos em círculos; frase dentro de pill com anéis | `backdrop-filter`, `rotateY` lento |
| 70–76s | "agora com IA" + brilho; **frase com imagens no meio do texto** ("Conteúdo [img] novo") | spans inline com imagem arredondada que cresce de 0 |
| 77–78s | **Túnel de hiperespaço** (zoom-through) | raios em `conic-gradient` + `scale` crescente |
| 78,5–83s | Anel de partículas + wordmark escrevendo; **URL dentro de um pill** com borda brilhante | `clip-path` no wordmark; pill com `box-shadow` animado |

## Quais usar primeiro (marca tech, escura)

1. **Typewriter com cursor em bloco** no gancho (combina com marcas de tecnologia e fonte mono).
2. **Palavra gigante rolando ou cortada** entre cenas (fonte de títulos da marca, no 9:16 em duas linhas).
3. **Cards que saltam da tela** nas demos de produto (dashboard, cardápio, painel).
4. **Troca de palavra por batida** no institucional ("A gente faz: sites / sistemas / dashboards / IA").
5. **Logo em vários estilos por batida** no clímax do institucional (5–8 estilos, monocromáticos).
6. **Transição por forma** cobrindo a tela (círculo ou uma letra do logo) no lugar de cortes secos.
7. **Final em três tempos**: CTA → ícone desenha → wordmark sai do ícone.

## Receitas (compatíveis com `seek(t)`)

Mesmas funções base de `cenas-jitter.md` (`clamp`, `prog`, `easeOutExpo`, `easeOutBack`). Nada de `Math.random()` dentro de `seek`: use `rand(i)` semeado, senão cada quadro sai diferente.

```js
const rand = i => { const x = Math.sin(i * 127.1 + 311.7) * 43758.5453; return x - Math.floor(x); };

// Typewriter com cursor em bloco: cps = caracteres por segundo; o cursor pisca a 2 Hz depois de terminar
function typeCaret(el, text, t, start, cps = 18, caret = '█') {
  const n = Math.max(0, Math.min(text.length, Math.floor((t - start) * cps)));
  const done = n >= text.length, blink = done ? (Math.floor((t - start) * 4) % 2 === 0) : true;
  el.textContent = text.slice(0, n) + (t >= start && blink ? caret : '');
}

// Letras espalhadas que convergem para o lugar (cada span já está na posição final)
function scatterAssemble(spans, t, start, dur = 0.8, spread = 600) {
  spans.forEach((s, i) => {
    const p = easeOutExpo(prog(t, start + i * 0.02, dur));
    const dx = (rand(i) - 0.5) * spread * (1 - p), dy = (rand(i + 99) - 0.5) * spread * 0.6 * (1 - p);
    s.style.transform = `translate(${dx}px,${dy}px) rotate(${(rand(i + 7) - 0.5) * 60 * (1 - p)}deg)`;
    s.style.opacity = clamp(p * 3);
  });
}

// Palavra gigante rolando na horizontal (pxPorSeg negativo = para a esquerda)
function marquee(el, t, start, pxPorSeg = -900, x0 = 200) {
  el.style.transform = `translateX(${x0 + (t - start) * pxPorSeg}px)`;
}

// Card que sai da tela: sobe, cresce e ganha contorno; o fundo desfoca
function pullOut(card, fundo, t, start, dur = 0.6, z = 1.25) {
  const e = easeOutBack(prog(t, start, dur), 1.3);
  card.style.transform = `translateY(${-30 * e}px) scale(${1 + (z - 1) * e})`;
  card.style.boxShadow = `0 ${30 * e}px ${60 * e}px rgba(0,0,0,${0.35 * e}), 0 0 0 ${2 * e}px rgba(255,255,255,${0.8 * e})`;
  fundo.style.filter = `blur(${6 * prog(t, start, dur)}px)`;
}

// Uma palavra trocando a cada batida (beat = 60/BPM); a nova entra de baixo, a velha sai para cima
function wordSwap(slot, palavras, t, start, beat, dur = 0.25) {
  const k = Math.floor((t - start) / beat), i = clamp(k, 0, palavras.length - 1);
  const p = easeOutExpo(prog(t, start + i * beat, dur));
  slot.textContent = t < start ? '' : palavras[i];
  slot.style.transform = `translateY(${(1 - p) * 60}%)`;
  slot.style.opacity = p;
  slot.style.filter = `blur(${(1 - p) * 8}px)`;
}

// Texto gigante que encolhe para dentro de um pill
function pillSnap(txt, pill, t, start, dur = 0.5, de = 3.2) {
  const e = easeOutExpo(prog(t, start, dur));
  txt.style.transform = `scale(${de + (1 - de) * e})`;
  pill.style.opacity = e;
  pill.style.transform = `scale(${0.9 + 0.1 * e})`;
}

// Número rolando (odômetro) até o valor final
function odometer(el, t, start, fim, dur = 1.2, casas = 0, prefixo = '', sufixo = '') {
  const v = fim * easeOutExpo(prog(t, start, dur));
  el.textContent = prefixo + v.toLocaleString('pt-BR', { minimumFractionDigits: casas, maximumFractionDigits: casas }) + sufixo;
}

// Logo em vários estilos, um por batida: `estilos` é uma lista de classes CSS (cromado, contorno, vidro…)
function logoMontage(el, estilos, t, start, beat) {
  const i = Math.floor((t - start) / beat);
  el.className = 'logo ' + (i >= 0 && i < estilos.length ? estilos[i] : '');
  el.style.transform = `scale(${1 + 0.06 * (1 - prog(t, start + Math.max(0, i) * beat, 0.15))})`;
}
```

Notas:
- Os vídeos de referência são 16:9. Ao trazer um padrão para o 9:16, empilhe a palavra gigante em 2 linhas, aproxime mais a câmera nas telas e respeite a área segura (`qa.md`).
- Partículas e anéis de partículas: desenhe num `<canvas>` com posição em função de `t` e de `rand(i)`. Mais de ~2.000 pontos por quadro deixa o render lento.
- `backdrop-filter` e vários `blur` grandes no mesmo quadro custam caro no render; use em uma camada por vez.
