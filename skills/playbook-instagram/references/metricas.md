# Métricas, metas e diagnóstico

## O que olhar (sempre em taxa sobre alcance)

| Métrica | Fórmula | Diz o quê |
|---|---|---|
| Envios por alcance | envios ÷ alcance | potência de distribuição para não seguidores [oficial: sinal-chave]. [medido] 1–2% é forte, 3%+ é excepcional |
| Salvamentos por alcance | salvos ÷ alcance | valor de referência (carrossel/educativo) |
| Curtidas por alcance | curtidas ÷ alcance | aceitação por quem já segue |
| Taxa de pulo (reel) | Insights | gancho; meta < 35% |
| Tempo médio assistido ÷ duração | Insights | hold rate; meta 50% (< 15s) / 30% (30s+) |
| Alcance de não seguidores | Insights (% não seguidores) | descoberta |
| Visitas ao perfil e toques no link | Insights | intenção |
| Seguidores por post | campo "Follows" (IGPO29 no Metricool) | conversão em audiência |
| Leads do Instagram | pipeline | o que realmente importa |

## Benchmarks gerais (contexto, não meta) [medido, Socialinsider 2025/2026]

- Engajamento médio: 0,48% (queda de 24% no ano); carrossel 0,55%, reel 0,52%, imagem 0,37%.
- Views médias por post em contas de 1–5 mil seguidores: reels ~580, carrossel ~993, imagem ~417.
- Contas abaixo de 10 mil seguidores costumam ter engajamento acima da média; > 0,6% consistente já é desempenho acima da maioria.

## Metas sugeridas (revisar a cada 4 semanas)

Primeiro mês: estabelecer a linha de base da conta (média e mediana por formato). A partir daí, metas relativas:
- +10% de alcance médio por formato a cada mês.
- Envios por alcance ≥ 1% em reels.
- Salvamentos por alcance ≥ 2% em carrosséis educativos.
- ≥ 2 conversas (DM) qualificadas por semana vindas de conteúdo.

## Diagnóstico rápido

| Sintoma | Causa provável | Ação |
|---|---|---|
| Pulo alto | quadro 1 sem movimento/informação | testar 2 aberturas novas |
| Bom início, queda no meio | sem virada, ritmo lento | cortar 20%, adicionar quebra em 30% e 65% |
| Bom tempo, poucos envios | não é "mandável" | gancho de identificação ou utilidade para terceiros |
| Muito salvamento, pouco alcance | carrossel ótimo, capa fraca | testar capa nova no próximo do mesmo tema |
| Alcance só de seguidores | sem recomendação | checar Status da conta; originalidade; tema consistente |
| Engajamento sem lead | CTA fraco ou ausente | palavra-chave + oferta de entrada |

## Coleta no Metricool

- Use `getAnalyticsAvailableMetrics` (rede `instagram`, conectores `posts`, `reels`, `stories`, `evolution`) para os IDs exatos; IDs de posts: IGPO02 data/hora, IGPO03 texto, IGPO07 tipo, IGPO14 alcance, IGPO12 interações, IGPO13 curtidas, IGPO15 salvos, IGPO27 envios (shares), IGPO28 views, IGPO29 follows. Campos marcados "Deprecated" no retorno não devem ser usados.
- Salve as respostas em arquivo e calcule em código.
- Uma semana tem poucos posts: conclusões só com 3–4 semanas; na semana, aponte tendências como hipóteses.
