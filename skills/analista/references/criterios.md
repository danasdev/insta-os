# Critérios do analista

## Nota do post (0–10)

Calcule as taxas sobre o **alcance** do próprio post:

| Componente | Taxa | Peso |
|---|---|---|
| Distribuição | compartilhamentos ÷ alcance | 30% |
| Valor | salvos ÷ alcance | 25% |
| Conversa | comentários ÷ alcance | 15% |
| Aceitação | curtidas ÷ alcance | 10% |
| Conversão | follows ÷ alcance | 10% |
| Alcance | alcance ÷ mediana de alcance da conta | 10% |

Cada componente vira 0–10 comparando com a **mediana da conta no mesmo formato** (nota 5 = mediana, 10 = 2× a mediana ou mais, 0 = zero), limitado a 10. Antes de existir histórico (menos de 8 posts no formato), compare com as referências de `playbook-instagram/references/metricas.md` (envios 1% = 7, salvos 2% = 7, curtidas por alcance 5% = 5). A nota final é a média ponderada, com 1 casa decimal. Mostre sempre as taxas ao lado da nota: a nota resume, as taxas explicam.

Leitura automática (escolha a que se aplica):
- alcance alto + salvos/envios baixos → "chegou longe, mas não entregou valor: gancho bom, conteúdo raso"
- salvos altos + alcance baixo → "conteúdo bom, capa fraca"
- envios altos → "mandável: repetir o formato"
- comentários altos → "gerou conversa: responder todos e virar post de continuação"
- follows altos → "converte em audiência: fixar ou usar como modelo"
- tudo baixo → "revisar gancho, horário e tema"

## Auditoria do perfil (cada item 0–10)

| Área | O que olhar |
|---|---|
| Foto | símbolo legível em 110 px, contraste, igual às outras redes |
| Nome pesquisável | o campo nome tem palavra-chave (ex.: "Marca · Sites e Sistemas") além da marca |
| Bio | linha 1: o que faz e para quem; linha 2: prova; linha 3: CTA com palavra-chave; até 150 caracteres |
| Link | leva a uma página que converte (site com WhatsApp/formulário), funciona no celular |
| Destaques | 3–6, capas consistentes, na ordem que vende: Cases · Serviços · Como funciona · Depoimentos · Contato |
| Fixados | 3 posts que explicam a marca: institucional, melhor case, melhor educativo |
| Grade | alternância de cor predominante (escuro/claro), alternância de formato, capas legíveis no corte 3:4, sem 3 posts iguais seguidos, identidade reconhecível de longe |
| Consistência | frequência das últimas 4 semanas vs. a meta do perfil |

## Formatos no painel

**`posts/<id do post>`**: `data` (ISO), `tipo` (POST · CAROUSEL · REEL), `url`, `imagem`, `texto` (primeiros 140 caracteres), `pilar`, `gancho`, `alcance`, `curtidas`, `comentarios`, `salvos`, `compart`, `views`, `follows`, `taxas` `{compart, salvos, coment, curtidas, follows}` (frações), `nota` (0–10), `leitura` (1 frase), `atualizadoEm`.

**`perfil/atual`** (e `perfil/<AAAA-MM-DD>`): `data`, `seguidores`, `posts30d`, `notaGeral`, `itens`: lista de `{area, nota, achado, acao}`.

**`referencias/<handle>`**: `handle`, `nome`, `tipo` (concorrente · referencia-formato · cliente-ideal), `seguidores` (texto, como aparece no perfil, com data), `porque`, `ultimaLeitura`.

**`tendencias/<slug>`**: `titulo`, `formato`, `gancho`, `exemplo` (URL), `fonte` (perfil ou site), `porqueFunciona`, `comoAdaptar`, `status` (ideia · na-pauta · feito · descartada), `criadoEm`.
