---
name: calendario-semanal
description: Monta a pauta semanal do Instagram da marca (3 posts de feed + stories), produz as peças e agenda no Metricool após aprovação. Use quando pedirem "pauta da semana", "calendário do insta", "o que postar essa semana", "planejar os posts", ou na tarefa agendada de segunda-feira.
---

# Calendário semanal

Ritmo: o do perfil da marca (padrão: **3 posts por semana** — 1 reel, 1 carrossel de prova, 1 educativo — + stories em 3 dias). O usuário aprova tudo antes de agendar.

Leia antes a skill `marca` (e o perfil da marca) e, da skill `playbook-instagram`, `algoritmo.md` e `metricas.md`.

## 1. Levantar o contexto (silencioso)

1. **Metricool** (se conectado): leia o schema de cada ferramenta antes de chamar.
   - `getBrandSettings` (use o brandId e o fuso registrados no perfil; confira se o @ ligado é o do perfil).
   - `getScheduledPosts` das últimas 4 semanas e das próximas 2: o que já saiu e o que já está agendado (não repetir projeto nem tema).
   - `getBestTimeToPostByNetwork` (Instagram) para escolher horários.
   - Se o Metricool não estiver conectado, diga em uma linha que a pauta sai sem horários otimizados e sem agendamento, e siga.
2. **Último relatório** (skill `relatorio-semanal`): se houver um desta conversa ou o usuário colar, use as 3 decisões dele.
3. **Tendências** (aba Mercado do painel, coleção `tendencias` com status `ideia` ou `na-pauta`, via `ArtifactData`): encaixe pelo menos uma por semana, adaptando formato e gancho, nunca copiando. Ao pautar, mude o status para `na-pauta`; depois de publicada, `feito`.
4. **Novidades**: pergunte em uma pergunta curta (AskUserQuestion) se há projeto recém-entregue, lançamento ou evento na semana. Se ninguém responder (tarefa agendada), siga com o portfólio.

## 2. Montar a pauta

Distribuição padrão (ajuste aos melhores horários do Metricool):

| Dia | Peça | Pilar | Skill |
|---|---|---|---|
| Terça | Reel motion | Trabalho ou Marca | `anuncio-motion-video` |
| Quinta | Carrossel de prova (case ou produto) | Trabalho | `case-de-projeto` |
| Sábado ou domingo | Carrossel educativo | Ensina | `post-educativo` |
| Seg a sex | Stories (3–5 telas/dia em 3 dias, no mínimo) | Bastidor / Chamada | `stories` |

Regras:
- Gire o portfólio: o mesmo projeto não aparece em duas peças de feed na mesma semana nem em semanas seguidas.
- Educativo conversa com um dos 3 públicos (sistema, varejo, premium); alterne o público a cada semana.
- Um reel motion completo é caro (render de ~20 min). Se já existir um reel recente não publicado, ou um vídeo pronto (ex.: o institucional), prefira cortes dele (15s, 9:16) e diga isso.
- **Varie a cor predominante da grade:** pelo menos 1 post claro a cada 3–4 escuros, e nunca 3 capas iguais seguidas.
- Toda peça tem um CTA; uma por semana tem CTA direto para contato ("chama no direct com a palavra SITE").

Mostre a pauta como tabela (dia | horário | formato | tema | gancho | CTA) e espere aprovação. Se o usuário não estiver presente, prepare tudo e deixe aguardando aprovação, sem agendar.

## 3. Produzir

Para cada item aprovado, rode a skill correspondente. Entregue cada peça assim que ficar pronta (não espere todas), com legenda, alt text e hashtags.

## 4. Agendar no Metricool

Só depois do "pode agendar" do usuário para aquelas peças.

Regras da ferramenta `createScheduledPost` (confira o schema antes da primeira chamada da sessão):
- `blogId` = brandId do perfil; `date` em ISO com o offset do fuso do perfil; dentro de `info`: `publicationDate: {dateTime, timezone: <fuso do perfil>}`, `providers: [{network: "instagram"}]` e `instagramData` com `type` (`POST` para foto/carrossel, `REEL`, `STORY`).
- **Instagram exige mídia** (imagem/carrossel para POST, vídeo para REEL). A mídia entra em `media` como **URL pública** (ou link do Google Drive/Dropbox ligado na conta do Metricool). Links de artifact do Claude são privados: nunca use.
  - Use o repositório público de mídia do perfil (passo a passo no README do plugin): suba as artes aprovadas em `AAAA/MM-DD-<peca>/` e use `https://raw.githubusercontent.com/<dono>/<repo>/main/<caminho>` em `media`.
  - Sem URL pública: entregue as artes ao usuário para ele anexar no Metricool, e só agende quando houver mídia.
- Use `mediaAltText` (uma por imagem), `firstCommentText` para a instrução de palavra-chave, `collaborators` em case com cliente, `isAiGenerated: true` quando houver conteúdo gerado por IA, `showReelOnFeed: true` nos reels.
- `autoPublish: true` publica sozinho no horário; `false` manda notificação no app do Metricool para o usuário publicar na mão (útil para reels com música da biblioteca do Instagram).
- `draft: true` cria rascunho sem agendar.
- Depois de agendar, confirme com `getScheduledPosts` e devolva o `plannerUrl` de cada post. Para mudar, `updateScheduledPost` com o conteúdo completo; nunca apague agendamentos sem pedido explícito.

## 5. Fechar

Resumo curto: o que foi agendado, o que ficou pendente (mídia para anexar, aprovação de cliente para um case) e o próximo passo (ex.: "sexta eu gero o relatório").
