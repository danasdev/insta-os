# Abordagem e formato dos leads

## Formato do documento no pipeline (coleção `leads`)

| Campo | Valores |
|---|---|
| `empresa` | nome comercial |
| `segmento` | `sistema` · `varejo` · `premium` · `outro` |
| `cidade`, `uf` | ex.: `Teresina`, `PI` |
| `origem` | `prospeccao` · `indicacao` |
| `indicadoPor` | nome do cliente que indicou (só em indicação) |
| `instagram`, `site` | @ comercial e domínio |
| `contato` | nome e cargo publicados pela empresa, ou o canal ("WhatsApp comercial") |
| `etapa` | `mapeado` → `abordado` → `respondeu` → `reuniao` → `proposta` → `fechado` / `perdido` |
| `proximoPasso` | texto curto ("enviar abordagem", "follow-up 1", "mandar proposta") |
| `proximoData` | `AAAA-MM-DD` |
| `valor` | número em reais (estimativa só se o usuário informar) |
| `diagnostico` | 2–3 oportunidades observadas |
| `mensagem` | texto da abordagem preparada |
| `notas` | livre (encaixe A/B, histórico) |
| `criadoEm`, `atualizadoEm` | ISO 8601 |

## Estrutura da primeira mensagem

1. Cumprimento + quem fala (nome do usuário, marca, cidade).
2. Uma observação real e específica sobre o negócio (elogio verdadeiro + oportunidade).
3. O que pode oferecer, sem custo e sem compromisso (diagnóstico rápido, print com sugestão).
4. Pergunta simples de responder.
5. Saída educada.

## Modelos (adaptar sempre; nunca enviar igual para todos)

`{nome}`, `{marca}`, `{cidade}` e `{case}` vêm do perfil da marca. `{case}` só pode ser um cliente real com divulgação autorizada.

**Varejo (vende pelo direct/WhatsApp)**
> Oi, tudo bem? Aqui é {nome}, da {marca}, de {cidade}. Vi o perfil de vocês e as peças novas estão lindas! Percebi que os pedidos rolam todos pelo direct; dá pra montar um catálogo com checkout que funciona no celular e tira esse peso da conversa. Posso te mandar um print de como ficaria com os produtos de vocês? Se não fizer sentido agora, sem problema.

**Empresa que precisa de sistema (operação manual)**
> Olá! Sou {nome}, da {marca}. Vi no site de vocês que os orçamentos são feitos por mensagem e planilha. A gente monta painéis que organizam isso e mostram em tempo real o que está entrando. Topa uma conversa de 15 minutos pra eu entender o processo de vocês e dizer se dá pra automatizar?

**Serviço premium (site aquém do serviço)**
> Oi! Aqui é {nome}, da {marca}. Acompanho o trabalho de vocês e o padrão é altíssimo. O site ainda não mostra esse nível (no celular ele quebra a galeria). A gente fez o projeto de {case}. Posso te mandar 2 ou 3 sugestões rápidas do que eu mudaria?

## Follow-ups

- **Follow-up 1 (D+3 a D+4):** traga algo novo: "Fiz um rascunho rápido de como ficaria a home de vocês [print]. Se quiser, te explico em 10 minutos."
- **Follow-up 2 (D+7 a D+10):** case parecido: "{case} tinha um problema parecido: [antes, em 1 frase]. A gente fez [entrega, em 1 frase]: [link do case]. Fico à disposição." (só fatos confirmados do perfil)
- Depois disso: encerrar com cordialidade e mover para `perdido`.

## E-mail (quando só houver e-mail de contato)

Assunto curto e específico ("Sugestão para o site da <empresa>"). Mesmo corpo da mensagem, com assinatura: nome, marca, site e @ do perfil, e uma linha final: "Se preferir não receber mensagens nossas, é só responder avisando."
