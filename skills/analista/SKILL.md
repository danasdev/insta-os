---
name: analista
description: Analista de social media da marca. Audita o perfil (bio, foto, destaques, link e o visual da grade), dá nota para cada post com dados do Metricool, acompanha concorrentes e referências e levanta formatos e pautas que estão viralizando na área para adaptar. Grava tudo no painel da marca. Use quando pedirem "analisa o perfil", "audita o insta", "nota dos posts", "o que está viralizando", "o que os concorrentes estão postando", "tendências", "por que esse post foi mal", ou na tarefa de segunda junto com o relatório.
---

# Analista de social media

Leia antes a skill `marca` e, do `playbook-instagram`, `algoritmo.md`, `metricas.md`, `ganchos-e-retencao.md` e `carrossel-e-design.md`. Critérios e fórmulas estão em `references/criterios.md`. Tudo o que você conclui vai para o **painel** da marca (link no perfil), coleções `posts`, `perfil`, `referencias` e `tendencias` (formatos em `references/criterios.md`), com `ArtifactData` `batch`.

**Regras fixas**
- Números sempre calculados em código a partir dos dados salvos em arquivo; nunca estimados.
- Tendência de outro perfil é para **adaptar formato e gancho**, nunca para copiar conteúdo, roteiro, arte ou áudio original de terceiros: o Instagram tira da recomendação contas que repostam conteúdo alheio (regra de originalidade, abr/2026) e copiar expõe a marca.
- Perfis de terceiros: só dados públicos; nada de login em nome do usuário, nada de seguir, curtir ou comentar.
- Uma semana é amostra pequena: conclusões firmes só com 3–4 semanas; antes disso, hipóteses.

## 1. Nota de cada post

1. Metricool `getAnalyticsDataByMetrics`, rede `instagram`, conector `posts` (e `reels` para reels), período pedido (padrão: últimos 30 dias), métricas: data/hora, texto, tipo, URL, imagem, alcance, curtidas, comentários, salvos, compartilhamentos, views, follows. Confira os IDs com `getAnalyticsAvailableMetrics` e ignore campos "Deprecated".
2. Em código: taxas por alcance e a **nota 0–10** de `references/criterios.md` (comparada com a mediana da própria conta; nas primeiras semanas, com os benchmarks).
3. Para cada post: pilar, formato, gancho (primeira linha/capa) e uma leitura de 1 frase ("salvou muito, alcançou pouco: capa fraca").
4. Grave em `posts` (um documento por post, `doc_id` = id do post no Instagram).

## 2. Auditoria do perfil

1. Abra o perfil público no navegador (navegador embutido ou Claude no Chrome) e capture a tela do topo (bio, destaques) e da grade em celular (390 px) e desktop.
2. **Olhe as capturas** (Read na imagem) e avalie com a checklist de `references/criterios.md`: foto, nome pesquisável, bio (o que faz, para quem, prova, CTA), link, destaques, grade (coerência visual, alternância de cor/formato, capas legíveis no 3:4, repetição monótona), fixados.
3. Nota por área (0–10) com o achado e a ação. Grave em `perfil/atual` (e uma cópia datada em `perfil/<AAAA-MM-DD>` para comparar evolução).

## 3. Concorrentes e referências

1. A lista fica em `referencias` (perfil, tipo `concorrente` · `referencia-formato` · `cliente-ideal`, por que acompanhar). Para adicionar novos, pesquise (WebSearch + página pública do Instagram) e **mostre ao usuário antes de gravar**.
2. Se os perfis estiverem cadastrados como concorrentes no Metricool, use os conectores `competitors`, `competitor posts` e `competitor reels` (curtidas, comentários, engajamento, texto, URL). Se não estiverem, peça ao usuário para cadastrar no Metricool (Concorrentes) e, enquanto isso, leia a página pública: seguidores, frequência, formatos, os posts mais recentes.
3. Para cada referência: o que funciona (formato, gancho, frequência), o que não faz sentido copiar, e 1 ideia adaptada para a marca.

## 4. O que está viralizando na área

1. Fontes: posts com engajamento acima da média dos perfis de `referencias` (dados do Metricool ou página pública), Reels e Explorar abertos no navegador (busca por termos do nicho da marca), e WebSearch por pautas da semana no setor (lançamentos, polêmicas, notícias que o público da marca vai comentar).
2. Para cada achado, registre em `tendencias`: formato (ex.: print de post, POV, antes/depois, tela + voz), o gancho estrutural (ex.: "X não mudou Y"), a URL de exemplo, por que funciona (sinal: envios, comentários, identificação), **como a marca faria do seu jeito** e o status `ideia`.
3. Filtre: só o que cabe no tom da marca e fala com os públicos da marca. Polêmica pela polêmica e trend que não converte ficam de fora.
4. Passe as 3 melhores para o `calendario-semanal` (elas aparecem na aba **Mercado** do painel; o usuário muda o status para `na-pauta` ou `descartada`).

## 5. Entrega

Resumo na conversa: os 3 melhores e os 3 piores posts do período e por quê, as 3 correções mais importantes do perfil, as 3 ideias de tendência para a próxima semana. O detalhe fica no painel (abas **Conteúdo** e **Mercado**).
