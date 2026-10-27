# Padrões de cena (referência: Jitter templates)

Biblioteca de **padrões de movimento de cena** pra usar como pauta no roteiro. Fonte: https://jitter.video/templates/ (30 templates listados na página, de "300+" na biblioteca). Serve como referência de movimento e ritmo, nunca como material para copiar.

## Regras de uso

- **Só movimento.** Reproduza o padrão (o que se move, como, em que ritmo) com o motor HTML da skill. Não copie layout, marca, textos, fotos ou assets dos templates; templates de comunidade têm autores. Nada de logo ou nome de terceiros no vídeo.
- **Escolha 2–4 padrões por vídeo** e anote-os na coluna "padrão" do roteiro. Mais que isso vira vitrine de efeitos.
- **Cada padrão cai numa batida.** Entrada no acento, saída na batida seguinte.
- **9:16 e área segura:** os dois templates cuja proporção confirmei são 4:5; recomponha qualquer padrão para 1080×1920, fora dos 250px de cima e de baixo.

## O que dá para obter do Jitter (e o que não dá)

- As páginas dão nome, categoria, duração, proporção e uma frase de descrição. **Não há arquivo de vídeo para baixar**: o preview é desenhado em canvas.
- Os frames foram vistos por captura de tela no navegador embutido (~1 quadro por segundo, o que perde o detalhe de movimentos de 2s). Por isso a coluna **Status** separa **observado** (vi frames) de **inferido** (só nome/descrição; confirmar antes de basear uma cena inteira nele).
- Para ver keyframes, easing e camadas de verdade: o botão "Remix for free" abre o template no editor do Jitter. Isso exige conta; o agente **não cria conta nem faz login**. O usuário pode abrir, e passar capturas ou os valores de duração/easing que quiser replicar.
- Se o usuário baixar MP4 de cenas e anexar, use a receita de contact sheets de `produto.md` (seção "Referência do usuário") para descrever o movimento quadro a quadro.

## Catálogo

| Template (Jitter) | Categoria | Dados confirmados | Padrão de movimento | Como fazer no motor | Status |
|---|---|---|---|---|---|
| Snappy Text Stretch | Video titles | 2s, 4:5 | Título bold em 2 linhas, data e URL pequena, no estilo de anúncio de festival de cinema; o movimento (texto esticado que "encaixa" num estalo) vem do nome e da descrição | `stretchSnap` (abaixo) por linha, 1 acento por linha | layout observado; movimento inferido |
| Image Stretch Transition | Jitter AI | descrição: "warps and pulls visuals into the next scene" | A imagem A é esticada na vertical enquanto a B entra empurrando por baixo; a borda inferior vira uma faixa espalhada na troca | `imageStretch` (abaixo), ~0,45s no corte | observado |
| The Track: Product Reveal | Social media / Ads | 7s, 4:5, "kinetic motion, strong pace" | Abre claro com contornos concêntricos finos e o logo; corta para o produto sobre fundo saturado com marcadores de registro nos cantos; título em tipografia larga (extended) entra por cima | stroke SVG (`stroke-dashoffset`) para os contornos; quadradinhos de registro com fade em sequência; título com `mask` | observado |
| The Stack: Testimonial | Social media | descrição: cita as falas como pilha de cards, uma por vez | Foto de fundo e um card de citação por cima; pela descrição, cada novo card entra e o anterior recua na pilha | `stackCards` (abaixo); útil para `case-de-projeto` (depoimento do cliente) | observado (1 quadro) + descrição |
| The Stack: Livestream | Social media | — | Mesma pilha de cards aplicada a comentários/avisos de live | `stackCards` | inferido |
| The Stack: Sale | Social media | — | Pilha de cards de oferta/preço | `stackCards` + contador de preço | inferido |
| Card Flip | Jitter AI | — | Card vira em Y revelando a outra face | `rotateY(0→180°)` com `backface-visibility:hidden` e `perspective` no pai | inferido |
| Orbit: Cards (comunidade) | Community | — | Cards orbitando em anel | já existe no carrossel 3D de `institucional.md` | inferido |
| Orbit: Social Media Showreel | Social media | — | Showreel de telas girando em órbita | idem; um card por acento | inferido |
| Interactive Gallery (comunidade) | Community | — | Galeria em que um item cresce e os demais recuam | grade com `scale`/`translate` por item, foco rolando a cada acento | inferido |
| Photo Gallery (comunidade) | Community | — | Fotos entrando em grade/colagem | idem | inferido |
| The Edit: Nested Images | Social media | — | Imagem dentro de moldura menor que se abre até preencher o quadro | `overflow:hidden` no pai; pai cresce enquanto o filho faz escala inversa | inferido |
| The Edit: Split Reveal | Social media | — | Dois painéis abrem pelo meio revelando a imagem | dois `clip-path` / `translateX` simétricos | inferido |
| Blend Modes: Double Exposure | Social media | — | Duas imagens sobrepostas com modo de mistura | `mix-blend-mode: screen`/`lighten`; atenção ao custo de render | inferido |
| Blur: Swirl | Social media | — | Rotação com desfoque que assenta | `rotate()` + `blur()` decrescentes com ease-out | inferido |
| Blurry Text Spin | Video titles | — | Texto gira (eixo Y/Z) desfocado e foca | `rotateY` + `blur` ligados ao mesmo progresso | inferido |
| Morph: Inflating Text | Video titles | — | Texto "infla": cresce com overshoot e afasta as letras | `scale` com `easeOutBack` + `letter-spacing` crescente | inferido |
| Stretched Type Repeater | Jitter AI | — | Palavra repetida em linhas esticadas verticalmente, com defasagem | N linhas com `scaleY` e atraso fixo por linha | inferido |
| Countdown: Bold | Text | — | Números grandes trocando a cada tempo | número gigante com `punch` a cada batida; bom para a cena "Números" do institucional | inferido |
| Ripple Effect | Jitter AI | — | Ondas concêntricas expandindo | círculos com `stroke` e opacidade decrescente; o ripple do cursor já faz isso | inferido |
| Dithering Effect | Jitter AI | — | Imagem em pontilhado (dithering) que se resolve | canvas com matriz de Bayer e limiar animado; bom para o ato "Caos" P&B | inferido |
| View Cart Button: Split | UI elements | — | Botão pill que se divide em dois | largura animada de dois filhos de um flex | inferido |
| Gradient Background / Loop | Backgrounds / Jitter AI | — | Gradiente procedural em loop | `radial-gradient` com centros em função de `t` | inferido |
| Vector Animation | Backgrounds | — | Traços vetoriais desenhando-se | `stroke-dashoffset` | inferido |
| The Crust: Animated Menu | Social media | — | Cardápio animado item a item | lista entrando por `mask`, um item por batida | inferido |
| The Track: Session Complete | Social media | — | Tela de conclusão/resumo de sessão | contador + anel de progresso (SVG) | inferido |
| Holo (comunidade) | Community | — | Superfície holográfica/irisada | gradiente cônico com `mix-blend-mode` | inferido |
| Project Teaser / Share Your Work (comunidade) | Community | — | Teaser de projeto, vitrine de trabalho | sequência de telas com `imageStretch` entre elas | inferido |

## Quais usar primeiro

1. **Snappy Text Stretch** no gancho (texto grande de 4–8 palavras, quadro 1 já em movimento).
2. **Image Stretch Transition** como corte whip no 9:16 (troca de cena no acento).
3. **The Stack: Testimonial** no `case-de-projeto` (depoimento e resultado do cliente).
4. **The Track: Product Reveal** para revelar o produto (contornos + título largo).
5. **Countdown: Bold** na cena de números do institucional.
6. **Dithering Effect** como textura P&B no ato Caos.

## Receitas (compatíveis com `seek(t)`)

Funções puras: o estado sai só de `t`. Se o template já tem `P(t,start,dur,ease)`, use-o no lugar de `prog`.

```js
const clamp = (x, a = 0, b = 1) => Math.min(b, Math.max(a, x));
const prog = (t, start, dur) => clamp((t - start) / dur);
const easeOutExpo = x => (x >= 1 ? 1 : 1 - Math.pow(2, -10 * x));
const easeOutBack = (x, s = 1.7) => 1 + (s + 1) * Math.pow(x - 1, 3) + s * Math.pow(x - 1, 2);

// Texto que entra esticado e encaixa no acento
function stretchSnap(el, t, start, dur = 0.35) {
  const p = prog(t, start, dur), e = easeOutExpo(p);
  el.style.transformOrigin = '50% 100%';
  el.style.transform = `scale(${0.82 + 0.18 * e},${3.2 - 2.2 * e})`;
  el.style.filter = `blur(${(1 - e) * 14}px)`;
  el.style.opacity = clamp(p * 4);
}

// Troca de cena por stretch: A estica e some na 1ª metade, B entra esticada na 2ª
function imageStretch(a, b, t, start, dur = 0.45) {
  const p = prog(t, start, dur);
  const out = clamp(p * 2), inn = clamp(p * 2 - 1);
  const eo = out * out * out, ei = 1 - Math.pow(1 - inn, 3);
  a.style.transform = `scaleY(${1 + 5 * eo})`;
  a.style.filter = `blur(${eo * 18}px)`;
  a.style.opacity = p < 0.5 ? 1 : 0;
  b.style.transform = `scaleY(${1 + 5 * (1 - ei)})`;
  b.style.filter = `blur(${(1 - ei) * 18}px)`;
  b.style.opacity = p < 0.5 ? 0 : 1;
}

// Pilha de cards: cada novo entra por baixo; os anteriores recuam
function stackCards(cards, t, start, every = 1.2, dur = 0.5) {
  cards.forEach((c, i) => {
    const enter = prog(t, start + i * every, dur), e = easeOutBack(enter, 1.2);
    let depth = 0;
    for (let j = i + 1; j < cards.length; j++) depth += easeOutExpo(prog(t, start + j * every, dur));
    c.style.opacity = enter > 0 ? clamp(1 - depth * 0.28) : 0;
    c.style.transform = `translateY(${(1 - e) * 260 - depth * 28}px) scale(${Math.pow(0.94, depth)})`;
    c.style.zIndex = i;
  });
}
```

Notas: `stretchSnap` e `imageStretch` usam `filter: blur`; não empilhe vários blurs grandes no mesmo quadro (custo de render). Em `imageStretch`, esconda o ponto de corte no pico do blur; alinhe `start` a uma batida de modo que o meio (`start + dur/2`) caia no acento.
