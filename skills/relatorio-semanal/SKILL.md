---
name: relatorio-semanal
description: Gera o relatório semanal do Instagram da marca com dados do Metricool (alcance, engajamento, salvamentos, seguidores, melhores posts e horários) e do painel, e transforma em 3 decisões para a pauta seguinte. Use quando pedirem "relatório do insta", "como foi a semana", "métricas", "o que funcionou", ou na tarefa agendada de segunda-feira.
---

# Relatório semanal

Leia antes a skill `marca` e `playbook-instagram/references/metricas.md` (KPIs, IDs de métricas do Metricool, diagnóstico).

## 1. Dados

**Metricool** (leia o schema de cada ferramenta antes de chamar):
- `getBrandSettings` para a conta da marca (brandId do perfil); `getAnalyticsAvailableMetrics` para saber os nomes exatos das métricas de Instagram disponíveis.
- `getAnalyticsDataByMetrics` para a semana passada (segunda a domingo, fuso do perfil) e a anterior, para comparar: seguidores, alcance, impressões, engajamento, salvamentos, compartilhamentos, visitas ao perfil, cliques no link, e métricas por post e por reel.
- Salve as respostas em arquivos e calcule em código (variação %, taxa de engajamento = interações ÷ alcance); não faça conta de cabeça.
- Sem Metricool conectado: diga isso e peça os números do Insights do Instagram (print ou texto).

**Painel** (`ArtifactData` `list` da coleção `leads` no painel registrado no perfil, ou a planilha de leads): leads novos na semana, por origem, mudanças de etapa, reuniões e propostas, follow-ups atrasados.

## 2. Análise

Rode antes a skill `analista` (nota de cada post da semana, gravada em `posts` no painel) e use as notas e leituras dela.

- Top 3 posts da semana por salvamentos + compartilhamentos (eles indicam valor real) e o pior; o que tinham em comum (formato, pilar, gancho, horário).
- Leia os dados de cada post com cuidado: uma semana tem poucos posts; fale de tendência só com 3–4 semanas de histórico.
- Conecte conteúdo e lead: algum lead veio de post/story? (pergunte ao usuário se não estiver nas notas).

## 3. Entrega

Publique ou atualize um artifact do tipo **Dashboard** chamado "Instagram <marca>" (quando o tipo estiver listado), com: cartões de seguidores, alcance, engajamento e leads da semana (com variação), gráfico das últimas semanas, tabela de posts e o funil do pipeline. Cada número mostra de onde veio. Sem o tipo, responda na conversa com uma tabela curta.

Feche sempre com **3 decisões** concretas para a próxima semana, que o `calendario-semanal` vai usar. Ex.:
1. Repetir o formato do carrossel de checklist (maior salvamento).
2. Mover o reel para quinta 19h (melhor horário do Metricool).
3. Fazer follow-up nos 4 leads atrasados.

## Tarefa agendada sugerida

Toda segunda às 8h45: rodar este relatório, depois o `calendario-semanal` da semana, e deixar tudo aguardando aprovação (nada agendado nem enviado sem o usuário).
