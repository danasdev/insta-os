---
name: prospeccao-ativa
description: Encontra empresas da região e dos segmentos-alvo da marca com presença digital fraca, faz um diagnóstico do site e do Instagram de cada uma, escreve a mensagem de abordagem personalizada e registra tudo no pipeline de leads. Use quando pedirem "prospectar", "achar clientes", "lista de leads", "abordar empresas de X em Y", "follow-up dos leads".
---

# Prospecção ativa

Leia antes a skill `marca` e `playbook-instagram/references/psicologia.md` e `captacao.md`. Os modelos de mensagem e o formato dos leads estão em `references/abordagem.md`.

**Limites fixos:**
- Só empresas. Use apenas dados públicos do negócio (site, Instagram comercial, Google Maps, canais de contato divulgados pela própria empresa). Não procure nem registre dados pessoais de funcionários, sócios ou clientes além do nome e cargo que a empresa publica no próprio canal comercial.
- Você nunca envia mensagem. Você prepara; o usuário revisa e envia.
- Ritmo saudável: lotes de 10 empresas; no máximo 2 follow-ups por lead; sempre deixe uma saída educada ("se não fizer sentido agora, sem problema").

## 1. Definir o lote

Se o usuário não disser, pergunte em uma rodada (AskUserQuestion): segmento (um dos públicos do perfil), cidade(s) da região de prospecção e quantidade (padrão 10). Leia o pipeline antes (`ArtifactData` `list`, coleção `leads`, no pipeline do perfil) para não repetir empresas já cadastradas.

## 2. Encontrar empresas

- WebSearch por combinações de segmento + cidade ("loja de calçados femininos Teresina", "clínica de estética Natal", "distribuidora Fortaleza").
- Fique com quem tem sinal de que pode pagar e de que precisa: negócio ativo (posta, tem avaliações), mas com site ausente, lento, quebrado, sem versão mobile, sem catálogo/checkout, ou operação claramente manual (pedidos só por WhatsApp/direct, "orçamento por mensagem", planilhas citadas).
- Descarte quem já tem site forte e recente, grandes redes nacionais e franquias (decisão fora da região).

## 3. Diagnóstico (por empresa)

- WebFetch no site (se houver): proposta clara? catálogo? checkout? funciona no celular? velocidade aparente, links quebrados, formulário, WhatsApp, SEO básico (título, descrição).
- Instagram público (pela busca/página pública, sem login): frequência, bio, link na bio, se vende pelo direct.
- Escreva 2–3 oportunidades concretas e verificáveis, no tom de quem quer ajudar ("o site não abre no celular", "o catálogo está só nos destaques"). Nada de crítica agressiva.
- Classifique o encaixe: **A** (dor clara e porte compatível), **B** (provável), **C** (fraco: não abordar agora).

## 4. Mensagem

Para cada lead A ou B, escreva a primeira mensagem seguindo `references/abordagem.md`: personalizada com uma observação real, curta (até ~450 caracteres no direct), um valor oferecido (ex.: diagnóstico gratuito de 15 min, ou um print com a sugestão), uma pergunta fácil de responder. Varie a abertura entre leads; nada de texto idêntico em massa.

Indique o canal: direct do Instagram comercial, WhatsApp comercial divulgado, ou e-mail de contato do site.

## 5. Registrar no pipeline

Grave cada lead A/B no pipeline do perfil com `ArtifactData` `batch` (uma aprovação para o lote), coleção `leads`, `doc_id` em kebab-case do nome da empresa + cidade (ex.: `loja-aurora-teresina`), campos do formato em `references/abordagem.md`, etapa `mapeado`, origem `prospeccao`, próximo passo "enviar abordagem" com a data de hoje. Para um lead que já existe, leia antes e use `update` com `if_version`.

## 6. Entregar

Tabela do lote (empresa | cidade | encaixe | oportunidade principal | canal) e, abaixo, as mensagens prontas para copiar. Lembre o usuário de mudar a etapa para "abordado" no painel depois de enviar (ou peça para você atualizar).

## Follow-up (quando pedirem ou na rotina semanal)

1. `ArtifactData` `query` em `leads` com etapa `abordado` e `proximoData` ≤ hoje.
2. Para cada um, um follow-up curto que acrescente algo novo (um print com a sugestão aplicada, um case parecido do portfólio, um post educativo relevante), nunca "e aí, viu minha mensagem?".
3. Depois do 2º follow-up sem resposta, sugira mover para `perdido` com nota; não insista.
4. Atualize `proximoPasso`/`proximoData` só com a confirmação do usuário de que enviou.
