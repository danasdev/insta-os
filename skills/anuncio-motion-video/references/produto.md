# Modo produto (anúncio estilo SaaS launch)

Texto cinético com blur, interfaces em perspectiva 3D, cursor clicando, zoom de câmera nas telas, transições com zoom/blur/flash, trilha sintetizada no grid do BPM e narração encaixada frase por frase. Entrega MP4 1080×1920 (principal) e, se pedido, 1920×1080.

## 1. Briefing

Pergunte só o que não dá para descobrir sozinho (AskUserQuestion, até 4 perguntas por vez). Cubra:

1. **Produto e empresa**: nome, link do site/app, o que faz. Se for produto da própria marca, use a assinatura de vídeo do perfil.
2. **Quem define o conteúdo**: o usuário diz o que apresentar (features, mensagem, CTA), ou o agente extrai do site e escreve o roteiro inteiro (padrão quando o usuário não especifica).
3. **Pegada / segmento**: tech (padrão) ou outro ramo (`pegadas.md`).
4. **Formato e duração**: 9:16 (padrão) e, se quiser, 16:9. Padrão ~20s + corte de 15s; versão completa ~40s só se pedirem.
5. **Referências**: um MP4 do usuário, o exemplo do motor (`engine/exemplo-produto`), e/ou padrões de cena de `cenas-jitter.md`.
6. **Locução**: ElevenLabs (recomendado para versão final; o agente gera o roteiro com entonações), locutor humano, ou voz provisória local.

Se o usuário não estiver presente, assuma os padrões, diga quais assumiu e siga.

## 2. Identidade visual da empresa

Extraia do site, não invente:
- WebFetch para textos, proposta de valor, features, preços, CTAs.
- Navegador embutido (ou Chrome) para o visual. Rode JS que leia `getComputedStyle(body)`, as variáveis CSS de `:root` (cores, raio, sombras, easing), as fontes de `h1`/`body` e o logo (`img`/`svg`; para PNG, use `fetch` + `FileReader` para obter o data URL). Tire um screenshot da home.
- Telas atrás de login: **nunca crie conta nem digite senha**. Recrie a interface como mockup a partir do que o site descreve e avise o usuário.
- Se o logo não puder ser extraído com fidelidade, redesenhe em SVG aproximado e avise; peça o arquivo oficial.
- Fontes: Inter e Inter Display já vêm no sistema. npm/PyPI costumam estar bloqueados; use fontes do sistema (`fc-list`) com fallback parecido e avise.

Base escura padrão ( quando a marca é monocromática ou não tem identidade definida): fundo `#0a0a0a` com grid sutil e glow radial, texto `#f5f5f5`, cinzas `#8a8a8a`/`#262626`, Inter Display nos títulos (tracking -0.035em), rótulos em caixa alta com letter-spacing .34em, botões pill brancos, marca d'água com o nome da marca no canto superior esquerdo (no 9:16, abaixo de 250px).

## 3. Referência do usuário (se mandar MP4)

```bash
ffprobe -v error -show_entries format=duration:stream=width,height,r_frame_rate -of default=nw=1 ref.mp4
ffmpeg -v error -i ref.mp4 -vf "fps=1,scale=384:-1,tile=6x6" -frames:v 1 sheet1.jpg   # 36s por folha; repita com -ss
```

Olhe as folhas e descreva o estilo em uma lista curta (paleta, tipografia, tipos de transição, câmera, ritmo de cortes). O vídeo de referência é só estilo: nunca replique marca, textos ou cenas de terceiros.

## 4. Roteiro (aprovar antes de construir)

### Padrão de reel (~20s, 100 BPM, 33 batidas, cortes nas batidas)

| Cena | Batidas | Tempo | Conteúdo |
|---|---|---|---|
| 1. Gancho | 4 | 0–2,4s | Quadro 1 já com texto grande em movimento (4–8 palavras); frase-problema ou resultado primeiro |
| 2. Produto | 4 | 2,4–4,8s | Apresenta o produto; a primeira informação nova cai antes dos 3s |
| 3. Demo principal | 12 | 4,8–12s | Interface com cursor e zoom em **uma** ação (primeira virada ≈ 30% da duração) |
| 4. Diferencial | 6 | 12–15,6s | 2–3 frases curtas sincronizadas com trocas visuais (segunda virada ≈ 65%) |
| 5. Resultado + oferta | 4 | 15,6–18s | O momento "pronto" e preço/plano/prova social em uma tela |
| 6. Assinatura | 3 | 18–19,8s | Logo, URL; CTA sobreposto nos últimos 2s; assinatura do perfil. Corte logo após a recompensa |

Corte de 15s: gancho (3s) + melhor trecho visual (9s) + assinatura com CTA (3s), cortado nas batidas.

### Versão completa (~40s, 100 BPM)

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
- Mostre o roteiro como tabela (cena | tempo | visual | **padrão de cena** | fala) e espere aprovação quando o usuário estiver presente.
- Legenda queimada com todas as falas: muita gente assiste sem som (`ganchos-e-retencao.md`).

## 5. Roteiro para ElevenLabs (entonações)

Entregue sempre três blocos, prontos para copiar:

1. **Com tags v3**: só as falas, uma por linha, **sem números, travessões de índice ou rótulos** (o ElevenLabs lê e transcreve tudo que estiver no texto), ex.:
```
[thoughtful] Construir um site... não precisa ser [slight pause] complicado.
[warm, upbeat] Com o Nímbus, você começa por seções prontas.
```
   Tags em inglês entre colchetes: `[warm]`, `[confident]`, `[playful]`, `[smooth]`, `[impressed, smiling]`, `[calm, building up]`, `[proud, clear]`, `[inspiring, closing]`. Reticências criam pausas.
2. **Sem tags** (para Multilingual v2, que leria os colchetes), também só as falas.
3. **Tabela de direção** (# | intenção | como falar) separada dos blocos acima; é a única parte numerada e serve também para locutor humano.

Pronúncia:
- Nome de marca escrito como se fala em PT-BR, conforme a pronúncia do perfil (ex.: "Nimbus" lido como "Nímbus" → escreva `Nímbus`). Pergunte quando houver dúvida.
- Números por extenso ("vinte e nove reais"), nunca "R$ 29".
- Siglas soletradas se a voz errar ("agá-tê-eme-ele").

Oriente o usuário a gerar **uma frase por arquivo** (nomeie os arquivos na ordem) ou um arquivo único com pausas de ~0,5s entre frases, a filtrar vozes do Brasil e a testar 2–3 vozes com a frase 01.

## 6. Build da animação

Copie `engine/exemplo-produto/index.html` para `index.html` e adapte. Arquitetura:

- `seek(t)` posiciona tudo de forma determinística; nada de CSS transitions/animations. Cada cena é uma função `sN(t)`. Exponha `DURATION` (segundos).
- Linha do tempo: `NEWC` contém os cortes reais no grid musical (múltiplos de 0,6s a 100 BPM). `M(i,t)` remapeia o tempo "autorado" de cada cena para o grid; em cena nova, prefira escrever direto no tempo global (como `s5`).
- Helpers: `kin(sel,t,start)` (texto palavra a palavra com blur), `fade`, `P(t,start,dur,ease)`, `camAt(keyframes,t)` para câmera, `mix()` para cores.
- Transições em `TR` por corte: `zoom`, `reveal`, `whip`, `push`, `dark`; o flash (`#flash`) entra nos cortes com zoom. Padrões extras (stretch, pilha, flip) em `cenas-jitter.md`.
- Câmera dentro de UI: keyframes `[t, escala, focoX, focoY]` em coordenadas locais da janela; o foco é levado ao centro da tela.
- Cursor: `TRACKS` com waypoints que podem mirar seletores (`sel`), assim o cursor acompanha elementos que se movem ou têm zoom; `clicks` geram ripple.
- Mockups de UI com conteúdo realista (nada de lorem ipsum).
- **9:16 como alvo principal**: `body.portrait` no CSS reposiciona tudo; câmera mais forte no portrait (`PORT ? .68*cs^1.5 : cs`); coordenadas fixas do cursor convertidas em `resolve()`. Títulos quebram em 2 linhas (largura ~940px). Escreva o layout vertical primeiro e derive o horizontal.
- Sincronize: cada clique ou ação visual cai na palavra correspondente da narração; trocas de estado (ex.: temas) caem em batidas.
- Marque com `data-qa-ignore` o que deve ficar fora da varredura de QA (ex.: elementos que entram de fora de propósito).

## 7. Áudio

`music.py` (edite as constantes do projeto): `DUR`, `BPM`, `CHORDS`, `ROOTS`, `CUTS`, `END_BAR_T`, a lista de cortes para whoosh/swell/subdrop, os tempos de efeitos de UI (cliques, digitação, sucesso, contador) e `VO_T` (início de cada frase). Para uma versão de ~20s, recalcule `DUR`, `CUTS`, `END_BAR_T` (`NBARS` deriva dele) e os tempos de UI/sinos a partir das batidas do roteiro; `BPM`, `CHORDS` e `ROOTS` vêm do preset (`scripts/apply_preset.py`). Ele já faz:
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
