# Como o Instagram distribui conteúdo (2026)

Pesquisa de outubro de 2026. Marcação: **[oficial]** = dito pela Meta ou por Adam Mosseri; **[medido]** = estudo de terceiros (direcional, não regra).

## Não existe "um algoritmo"

[oficial] Feed, Reels, Stories e Explorar têm sistemas de ranking separados. Cada um responde à pergunta "qual a chance desta pessoa interagir com isto".

| Superfície | Quem vê | Sinais mais fortes |
|---|---|---|
| Feed | sobretudo seguidores | relação (DMs trocadas, comentários, buscar o perfil pelo nome), recência, curtidas por alcance |
| Reels | sobretudo NÃO seguidores | tempo assistido, envios por alcance (DM), curtidas por alcance |
| Stories | quase só seguidores | relação (quem você mais vê e responde) |
| Explorar | não seguidores | parecido com Reels; tópico consistente ajuda |

## Os 3 sinais confirmados (jan/2025, ainda válidos em 2026)

[oficial] Mosseri citou como os mais importantes:
1. **Tempo assistido** (watch time), incluindo rewatch. O que segura a pessoa é o que ganha o primeiro teste de audiência.
2. **Envios por alcance** (sends per reach): quantas pessoas que viram mandaram por DM. É o que mais leva o conteúdo para quem não segue. Frase dele: "faça algo que as pessoas queiram mandar para um amigo".
3. **Curtidas por alcance**: pesa mais na distribuição para quem já segue.

Por isso as métricas certas são sempre **por alcance** (taxa), nunca absolutas.

[medido] Salvamentos e envios aparecem com peso bem maior que curtidas nos estudos de terceiros (fala-se em 3–5×; sem fonte primária). Na prática: desenhe cada peça com um motivo explícito para **salvar** (referência, checklist) ou **enviar** (identificação, "manda pro seu sócio").

## Originalidade (abr/2026)

[oficial] Desde 30/04/2026, contas que repostam com frequência conteúdo que não criaram deixam de ser elegíveis a recomendações (já valia para Reels; passou a valer para fotos e carrosséis). Conta como original: o que você filmou, fotografou ou desenhou, ou material de terceiros com transformação real (texto, edição, narração). Não conta: só marca d'água, só mudar velocidade, print do post de outra pessoa.

Na prática:
- Nunca suba vídeo exportado com marca d'água de outra plataforma (CapCut, TikTok).
- Prints de sites de clientes dentro de uma arte desenhada pela marca são transformação (moldura, texto, narrativa). Print cru, não.
- Cenas geradas por IA: marque `isAiGenerated` no agendamento (o Instagram exige o rótulo para conteúdo gerado ou muito alterado por IA).

## Hashtags e busca

[oficial] Máximo de **5 hashtags** por post/reel (anunciado em dez/2025). Mosseri: poucas e específicas funcionam melhor que listas genéricas; hashtag ajuda a classificar o tema e a busca, não "dá alcance". Seguir hashtag não existe mais desde dez/2024.
[medido] Legenda, texto na tela, alt text e áudio carregam mais peso de descoberta que hashtag. Ver `legenda-e-busca.md`.

## Controle "Seu algoritmo"

[oficial] Em 2026 o usuário pode escolher tópicos que quer ver mais/menos (Reels em jan, Explorar em abr, Feed em jun). Consequência: **nicho claro e consistente** (sites, sistemas, IA para negócios) é classificado melhor do que um perfil que fala de tudo.

## Contas pequenas e testes

- [oficial] Reels de contas pequenas recebem teste inicial de distribuição como os das grandes; o que decide a expansão é o desempenho nesse teste.
- [oficial] **Trial Reels**: mostrados só a não seguidores por 24–72h; exigem conta profissional pública com 1.000+ seguidores; há limite de quantidade em 30 dias (abr/2026). Uso: testar duas versões do mesmo reel mudando só os 3 primeiros segundos.
- [oficial] Elegibilidade a recomendações: Configurações → Status da conta. Se algo violar as diretrizes de recomendação, o post só chega a seguidores. Confira ali quando o alcance despencar.
- [medido] Publicar por agendador (Metricool, via API oficial) não é penalizado; trate como mito.

## Formato: o que cada um faz melhor

| Formato | Papel | Dados |
|---|---|---|
| Reel | alcance com não seguidores, descoberta | [medido] maior parte das views vem de não seguidores em contas < 50 mil; 45–60s é a faixa de maior alcance; acima de 3 min o alcance para não seguidores cai muito |
| Carrossel | salvamento, prova, profundidade | [medido] maior taxa de engajamento entre formatos em 2025 (0,55% vs 0,52% reels, 0,37% imagem — Socialinsider); mais views médias por post que reels em contas de 1–100 mil seguidores |
| Imagem única | quase nunca | pior formato em engajamento |
| Stories | relacionamento e conversa com quem já segue | não gera alcance novo |

## Frequência e horário

[medido] Buffer (2 milhões de posts): sair de 1–2 para **3–5 posts/semana** mais que dobra o ganho de crescimento de seguidores e aumenta ~12% o alcance por post; 6–9/semana dá ~+18%. Semana sem post fica abaixo da linha de base da própria conta. A melhor frequência é a que se sustenta: 3/semana é um bom piso.
[oficial, sem data] Mosseri já sugeriu algo como 2 reels + 3–5 posts de feed por semana para quem quer crescer.

Horário:
- Use primeiro o `getBestTimeToPostByNetwork` do Metricool (é calculado para a audiência da conta e no fuso America/Fortaleza).
- [medido] Metricool 2026 (24 milhões de posts): reels têm mais engajamento entre 18h–21h; meia-noite tem menos concorrência; ~70% das views de um reel acontecem nos 3 primeiros dias (30% no 1º). Stories: 11h–14h. Alcance: meio da manhã/meio-dia em dias úteis.
- Para B2B (donos de empresa), teste janelas de 10h–12h e 18h–20h em dias úteis; fim de semana tende a menor alcance para esse público.

## Fatos de produto úteis (2026)

- Carrossel: até 20 itens; Edits (app da Meta) já cria e edita carrosséis (out/2026).
- Reels: gravação de até 3 min no app; uploads maiores existem, mas recomendação a não seguidores cai acima de 3 min.
- Grade do perfil mostra 3:4; post 4:5 é cortado em cima e embaixo na grade.
- Conteúdo salvo ficou pesquisável para o usuário (out/2026): mais um motivo para conteúdo "de consulta" (checklists, guias).
- Posts em colaboração (Collab): o mesmo post aparece no perfil dos dois e soma o público dos dois. É a alavanca mais forte para case com cliente.
