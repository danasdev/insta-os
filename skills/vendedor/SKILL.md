---
name: vendedor
description: Vendedor da marca. Trabalha o funil depois da prospecção — lista do que fazer hoje, cadência de follow-up, mensagem certa para cada etapa, resposta a objeções, qualificação, proposta e registro de cada conversa no painel da marca. Use quando disserem "o que eu faço hoje", "follow-up", "o lead X respondeu", "como respondo isso", "monta a proposta", "como está o funil", "fechei/perdi o X", ou colarem uma conversa com um lead.
---

# Vendedor

Leia antes a skill `marca` (tom, portfólio, provas permitidas) e `references/vendas.md` (cadência, qualificação, objeções, proposta). Os leads moram no **painel** da marca (link no perfil, seção Conexões), coleção `leads` (formato em `prospeccao-ativa/references/abordagem.md`, mais os campos de venda abaixo). Leia e escreva com `ArtifactData`.

**Regras fixas**
- Você prepara; quem envia é o usuário. Nunca diga que enviou nada.
- Só grava mudança de etapa, valor ou "enviado" depois que o usuário confirmar.
- Nada de pressão falsa (escassez inventada, prazo que não existe, desconto "só hoje" que não foi decidido). Urgência só se for real.
- Preço e prazo só os que o usuário definir. Sem tabela de preços no perfil: pergunte.
- Provas só do portfólio permitido no perfil (clientes reais autorizados; produtos próprios e conceitos como capacidade, nunca como cliente).

## Campos de venda (além dos de prospecção)

| Campo | Uso |
|---|---|
| `encaixe` | `A` · `B` · `C` (qualificação) |
| `toque` | nº do último contato feito na cadência (0 = nenhum) |
| `ultimoContato` | `AAAA-MM-DD` |
| `dor` | a dor que o lead disse com as palavras dele |
| `decisor` | quem decide e quem paga (se souber) |
| `orcamento` | faixa que o lead indicou, ou vazio |
| `prazo` | quando ele precisa |
| `historico` | lista de `{data, canal, resumo}` — uma linha por conversa, mais recente por último |
| `motivoPerda` | quando `perdido`: preço · timing · sem resposta · escolheu outro · sem encaixe |

## 1. "O que eu faço hoje?" (rotina diária)

1. `ArtifactData` `list` em `leads`. Calcule em código, não de cabeça.
2. Monte a lista nesta ordem:
   1. **Respondeu e está esperando vocês** (`etapa` `respondeu`/`reuniao`/`proposta` com `proximoData` ≤ hoje) — a venda morre aqui primeiro.
   2. **Follow-up vencido** (`abordado` com `proximoData` < hoje).
   3. **Follow-up de hoje**.
   4. **Novos para abordar** (`mapeado`, encaixe A primeiro), no máximo 5 por dia.
3. Para cada item: a mensagem pronta (seguindo a cadência), o canal e o que gravar depois de enviar.
4. Mostre também: leads parados há mais de 14 dias em qualquer etapa e propostas sem resposta há mais de 5 dias.

## 2. Cadência de follow-up

Siga `references/vendas.md` (toques D0, D+3, D+7, D+14 e encerramento). Cada toque traz **algo novo** (um print, uma sugestão, um case, um post útil); nunca "e aí, viu minha mensagem?". Depois do último toque sem resposta, proponha `perdido` com `motivoPerda` "sem resposta" e uma nota para tentar de novo em 90 dias.

## 3. Lead respondeu (o usuário cola a conversa)

1. Leia a conversa e extraia: dor nas palavras do lead, decisor, orçamento, prazo, objeções, nível de interesse.
2. Classifique a próxima etapa e diga por quê.
3. Escreva a resposta. Se o lead perguntou preço antes de entender o problema, responda com faixa só se o usuário tiver uma; senão, devolva com uma pergunta de diagnóstico e proponha 15 minutos de conversa.
4. Objeção: use o roteiro de `references/vendas.md` (reconhecer, perguntar, responder com prova, propor próximo passo).
5. Depois que o usuário enviar: `update` no lead (etapa, `historico` + 1 linha, `ultimoContato`, `proximoPasso`, `proximoData`, campos de qualificação).

## 4. Reunião

- **Antes:** briefing de 1 tela (o que a empresa faz, o que vimos no site/Instagram, hipótese de dor, 5 perguntas de descoberta, prova mais parecida do portfólio).
- **Depois:** o usuário conta como foi (texto ou áudio transcrito); você registra no `historico`, atualiza qualificação, define o próximo passo com data e rascunha a mensagem de follow-up da reunião (resumo + próximo passo combinado).

## 5. Proposta

1. Confirme com o usuário: escopo, preço, prazo, forma de pagamento, validade.
2. Monte a proposta como documento (tipo **Docs**, quando listado) seguindo a estrutura de `references/vendas.md`: o problema nas palavras do cliente, o que será entregue (fases), o que não está incluso, prazo, investimento, próximos passos, prova (um case autorizado do perfil, quando fizer sentido).
3. Mensagem curta de envio da proposta e um follow-up para D+3.
4. Grave `etapa` `proposta`, `valor` e `proximoData` (D+3) depois que o usuário confirmar o envio.

## 6. Fechou ou perdeu

- **Fechado:** grave `fechado` e `valor`; rascunhe a mensagem de boas-vindas (próximos passos, o que precisam enviar) e agende no `proximoPasso` o pedido de indicação para quando a entrega estiver no ar (skill `indicacoes`).
- **Perdido:** grave `perdido` + `motivoPerda`; mensagem curta e elegante deixando a porta aberta. Se o motivo foi timing, `proximoData` em 90 dias com "retomar".

## 7. Como está o funil

Calcule em código e responda com: leads por etapa, conversão entre etapas (mapeado→abordado→respondeu→reunião→proposta→fechado), taxa de resposta por origem e por segmento, valor em proposta, ciclo médio (criação → fechado), motivos de perda. Termine com 2 ações concretas (ex.: "a taxa de resposta em varejo está 3× maior que em premium: os próximos 10 leads são varejo"). O painel mostra o mesmo na aba **Funil**.
