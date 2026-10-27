# Modo institucional (vídeo da empresa)

Vídeo sem narração (ou com narração curta), editado em cima de uma música, com texto cinético, cenas reais P&B, carrossel 3D do portfólio e logo formado de estilhaços. Entrega 9:16 primeiro; 16:9 se pedido. Render, rascunho e QA são os de `render.md` e `qa.md`.

> **Exemplo de referência (vídeo institucional real de um estúdio digital, outubro de 2026):** ~51s, 4 cenas reais em P&B geradas por IA, carrossel 3D dos 9 produtos, logo de estilhaços, música real editada nos acentos. Os exemplos abaixo vêm dele, mas o método vale para qualquer empresa. Para reel, o corte padrão é de ~20s (ou 15s); a versão de ~50s serve para site e YouTube.

## Briefing específico

Pergunte (AskUserQuestion), além do briefing geral:
1. Tipo de empresa e o que mostrar: números, portfólio, processo, equipe.
2. Música: o usuário manda o arquivo, ou trilha própria sintetizada. Com música comercial, entregue as duas versões e avise sobre licença (uso comercial precisa de licença ou de áudio da biblioteca do Instagram, aplicável no agendamento pelo Metricool).
3. Narração ou não. Sem narração é o padrão de "anúncio de elite": o texto precisa ter foco e ritmo, nunca cara de slide.
4. Cenas reais: o usuário pode gerar clipes P&B curtos numa IA de vídeo; ofereça os prompts (ex.: por cima do ombro do programador, dedos no teclado até o Enter, reflexo do código nos óculos, mão rascunhando wireframes).
5. Links do portfólio (sites para o carrossel). 9 produtos é a quantidade ideal para o carrossel em anel.
6. Padrões de cena de referência (`cenas-jitter.md`): escolha quais entram nos atos (ex.: stretch de texto no gancho, countdown nos números).

## Estrutura em atos (exemplo de estúdio digital)

| Ato | Conteúdo | Música |
|---|---|---|
| Caos | "TODA IDEIA / COMEÇA NO / CAOS." + palavras soltas (RASCUNHOS, CONVERSAS, POSSIBILIDADES), estilhaços se mexendo, grão | intro com paradas (stop-time): cada palavra num acento |
| Forma | "NOSSO TRABALHO / É DAR / FORMA." os estilhaços convergem | última parada antes da banda entrar |
| Nascimento | "DO CAOS, / NASCE" → logo forma na entrada da banda; o grão some ("tudo se clareando") | drop |
| Prova | cena real (óculos com código) → carrossel de produtos | groove |
| Números / processo | 05 / ∞ / 01, túnel de painéis, ENTENDER → DESENHAR → CONSTRUIR → EVOLUIR | groove até as paradas finais |
| Assinatura | logo forma no **penúltimo** acento; o **último** acento traz "VAMOS TIRAR / ISSO DO PAPEL." + site e @ | final da música |

Regras de reel: o quadro 1 já tem texto grande e movimento (o ato "Caos" abre assim); nada importante na área segura (250px em cima e embaixo, 120px à direita); o CTA final sobrepõe os últimos 2s. Nome da marca na primeira aparição: ~2,7s no máximo; mais que isso cansa.

## Editar uma música nos acentos

1. Converta para WAV 44,1 kHz e analise em numpy: envelope RMS em janelas de 10ms, fluxo de onset, BPM por autocorrelação (ex.: uma faixa de 83 BPM tem batida de 0,7229s e compasso de 2,8916s).
2. Liste os **acentos** (hits) e as **paradas** (trechos de silêncio entre hits, típicos de stop-time). Monte a linha do tempo do vídeo em cima deles: cada troca de palavra/cena cai num acento.
3. Para encurtar ou alongar, corte sempre em **múltiplos de compasso** (ou de meio compasso quando o padrão de acordes se repete a cada meio compasso), para os acentos seguintes continuarem caindo nos mesmos lugares. Prefira tirar tempo do vídeo (encurtar uma cena) a repetir trecho da música: repetição soa como erro.
4. Para saltar até o final da música, emende **dentro de um silêncio que exista nas duas partes** (parada A ↔ parada B). Meça os onsets com resolução de 2,5ms nas duas partes e alinhe a re-entrada da banda: um erro de ~70ms já soa como tropeço. Faça crossfade de ~30ms dentro do silêncio.
5. Depois de qualquer mudança, verifique por correlação cruzada que o final ficou exatamente onde a imagem espera (logo e CTA).
6. Diga ao usuário o tempo exato de cada emenda para ele conferir de ouvido.

Sem música do usuário: gere a trilha sintetizada no BPM da pegada (`pegadas.md`) e marque as paradas e acentos no `music.py`.

## Texto cinético sem narração

- Tipos de entrada: `mask` (sobe por máscara), `punch` (escala + blur), `whip` (desliza com blur), `chaos` (embaralha caracteres parcialmente, com aberração cromática), `resolve` (embaralha e assenta em cromado), `stretch` (estica no eixo e encaixa; `cenas-jitter.md`). Varie por intenção, não por acaso.
- Hierarquia: uma palavra-chave grande por vez (120–250px), apoio em fonte mono pequena. Palavras de impacto em cromado.
- "CAOS." legível: embaralhe só ~28% dos caracteres e congele legível no acento.
- Sem sobreposição: cada palavra sai antes da próxima ocupar o mesmo espaço.
- Sobre cenas reais: escureça com um scrim radial e reduza os estilhaços para o texto ler.
- Texto que sai da tela é bug recorrente: rode a varredura de `qa.md` nas duas orientações; meça a largura só depois de carregar as fontes.

## Cenas reais (clipes de IA)

- Converta para sequência de JPG em P&B: `ffmpeg -i clip.mp4 -vf "hue=s=0,eq=contrast=1.18,scale=1280:-1" f%03d.jpg`, uma pasta por orientação (para 9:16, recorte o centro).
- Pré-carregue os quadros e desenhe num `<canvas>` por cima da cena, quadro = `floor((t − início)·30)`; o render espera `window.clipsReady`.
- Use cada clipe uma vez, 2–3s, entrando num acento.

## Carrossel 3D de produtos (abertura estilo "roda")

1. O primeiro site aparece sozinho, de frente, no centro.
2. Nos dois acentos seguintes, os outros saem dele e se encaixam numa **roda única e organizada**: anel de N cards (`rotateY(k·360/N) translateZ(R)`), com o anel inclinado (`rotateX(−56°) rotateZ(−14°)`), cards virados para a câmera (billboard: desfaça a rotação do anel em cada card) e menores (≈0,6×); a roda gira devagar. Rótulo "NOSSOS PRODUTOS" no centro.
3. A câmera mergulha **nessa mesma roda** até o card 0 (inclinação → 0, billboard → 0, raio cheio). Nunca troque para outro carrossel.
4. A cada acento (aqui, a cada 2 batidas), o anel gira um card; o da frente ganha cor e rola o print, os outros ficam em P&B. Índice "0k / 09", nome em cromado e categoria.
5. Prints dos sites: navegador embutido, viewport 800×500 com `zoom` 0,5555, esconda banners de cookie via JS (sem clicar), empilhe com `ffmpeg vstack`. Site atrás de login: não entre; peça prints ao usuário.

## Final

- Logo forma no penúltimo acento e fica sozinho no silêncio; o último acento traz o CTA e os dados (site, @). URL e @ sempre conferidos com o perfil e com o usuário.
- Grão de filme some depois que a marca nasce.

## Render longo

~1.530 quadros × 2 orientações levam ~20–25 min com 2 CPUs (4 processos por orientação). Sempre aprove um rascunho antes (`render.md`), rode o final em segundo plano e, ao mudar só um trecho, re-renderize só a faixa de quadros afetada. Se a linha do tempo mudar de duração, apague as pastas de quadros antes (quadros velhos sobrando entram no MP4).
