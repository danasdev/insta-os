---
name: case-de-projeto
description: Transforma um projeto entregue pela marca em conteúdo para o Instagram — carrossel de case (problema, processo, solução, resultado), legenda, stories e o pedido de depoimento e indicação ao cliente. Use quando disserem "entregamos o projeto X", "faz um case do site Y", "divulgar esse projeto", ou quando o calendário pedir o carrossel de case.
---

# Case de projeto

Leia antes a skill `marca` e, da skill `playbook-instagram`, `carrossel-e-design.md`, `psicologia.md` e `legenda-e-busca.md`. Os fatos confirmados de cada case ficam no perfil da marca.

## 1. Material (antes de desenhar)

Junte o que for real; não invente:
- Projeto, link, segmento do cliente, cidade.
- **Autorização**: pergunte se o cliente liberou a divulgação (e se pode marcar o @ dele). Sem liberação, não produza o post; ofereça uma versão sem nome do cliente.
- Problema de antes (como o cliente vendia/operava), o que a marca fez, prazo, tecnologia (só se ajudar quem lê).
- Resultado: só números que o cliente liberou. Prefira quantidades e percentuais a valores em reais. Sem número, use resultados verdadeiros de operação ("de zero métricas para todas as vendas registradas", "primeiras vendas pelo site", "o sistema de indicação já gera comissão").
- Prints: capture o site com o navegador (desktop 1440 e celular 390; esconda banners de cookie via JS, sem clicar). Área logada: o usuário faz o login; você só captura, e borra na imagem qualquer dado real (faturamento, vendas, nomes de clientes finais).

Pergunte em uma rodada (AskUserQuestion) o que faltar.

## 2. Roteiro do carrossel (7–9 telas, 1080×1350)

| Tela | Conteúdo |
|---|---|
| 1 Capa | Gancho com o resultado ou a dor (formato: "<Cliente> vendia só pelo direct.", com o fato confirmado) + print do site em mockup + eyebrow "CASE · <SEGMENTO>" |
| 2 Antes | O problema em 1–2 frases |
| 3 Desafio | O que precisava acontecer |
| 4–6 Solução | Uma decisão por tela, cada uma com print ou detalhe (home, produto, checkout, painel, versão mobile) |
| 7 Resultado | Fatos/números confirmados |
| 8 Depoimento | Só se houver depoimento real do cliente (citação em `grain`) |
| 9 CTA | "Seu projeto é o próximo. Chama no direct." + @ e site da marca |

Mostre o roteiro em tabela e espere aprovação quando o usuário estiver presente.

## 3. Design

- Crie as telas no tipo de artifact **Design** (quando listado), seguindo o visual do perfil da marca (cores, tipografia, regras de forma), com numeração "0k / 0n" pequena e um único destaque por tela.
- Os prints mantêm a identidade do cliente; a moldura e o texto são da marca.
- Sem Design disponível: monte as telas em HTML 1080×1350 e exporte PNG com Playwright.
- Confira legibilidade no celular: títulos ≥ 64px, texto ≥ 30px na tela de 1080.

## 4. Legenda e extras

- Legenda no padrão da marca (gancho, corpo curto, 1 CTA, até 5 hashtags com segmento + cidade), alt text por tela.
- **Post em colaboração**: convide o cliente como colaborador (`collaborators` no agendamento do Metricool). O post aparece no perfil dos dois e soma as audiências; avise o usuário que o cliente precisa aceitar o convite no app.
- Sequência de stories do case (skill `stories`): bastidor do projeto, "arrasta pra ver o case", caixinha "qual projeto você quer tirar do papel?".
- Opcional: reel de 15s do case com a skill `anuncio-motion-video` (carrossel de prints + nome + CTA).

## 5. Depoimento e indicação

Rascunhe para o usuário enviar ao cliente (nunca envie você):
1. Pedido de depoimento curto, com 2 perguntas guiadas ("O que mudou depois do site?" / "Indicaria a gente para quem?").
2. Pedido de indicação no mesmo fio, só se o cliente estiver satisfeito: passe para a skill `indicacoes`.

## 6. Entrega

Envie as telas (PNG) e a legenda; diga o que está pendente (autorização, depoimento, número a confirmar). Se o calendário chamou, volte para ele para agendar.
