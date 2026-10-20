---
name: indicacoes
description: Cuida do programa de indicações da marca — escolhe o momento certo de pedir indicação a cada cliente, escreve o pedido e o texto que o cliente repassa, registra os indicados no pipeline e prepara o agradecimento. Use quando disserem "pedir indicação", "o cliente X indicou alguém", "programa de indicação", "quem pode indicar a gente", ou ao fim de um case.
---

# Indicações

Leia antes a skill `marca`. Pedido de indicação funciona quando o cliente acabou de sentir valor. Você prepara; quem envia é o usuário.

## 1. Momento certo

Peça indicação logo depois de um destes momentos (pergunte ao usuário qual aconteceu):
- entrega do projeto com elogio do cliente;
- primeiro resultado visível (primeira venda no site, painel usado pela equipe);
- depoimento recebido (fluxo da skill `case-de-projeto`);
- renovação ou novo projeto fechado.

Não peça em meio a problema aberto, atraso ou cobrança pendente.

## 2. O pedido

Escreva duas mensagens:
1. **Para o cliente** (WhatsApp, tom próximo): agradece de verdade, cita o resultado específico, pergunta se conhece 1 ou 2 pessoas com um desafio parecido. Facilite: "se quiser, te mando um textinho pronto pra repassar."
2. **Texto para o cliente repassar** (curto, em primeira pessoa do cliente): o que a marca fez por ele + contato (site, @ e WhatsApp do perfil).

Incentivo (desconto, comissão, brinde): só se o usuário definir; não invente.

## 3. Registrar

Quando o usuário trouxer um indicado:
- Grave no pipeline com `ArtifactData` (pipeline do perfil, coleção `leads`, formato em `prospeccao-ativa/references/abordagem.md`): origem `indicacao`, `indicadoPor` = cliente, etapa `mapeado`, próximo passo "primeiro contato citando <cliente>" para hoje ou amanhã.
- Escreva a primeira mensagem ao indicado citando quem indicou (só com a permissão do cliente para usar o nome dele).
- Só registre dados de contato que o cliente ou o próprio indicado passaram.

## 4. Fechar o ciclo

- Quando o indicado responder ou fechar, prepare um agradecimento ao cliente que indicou (e o incentivo, se existir).
- Uma vez por mês (ou quando pedirem), liste os clientes que ainda não foram convidados a indicar e os indicados parados no pipeline.
