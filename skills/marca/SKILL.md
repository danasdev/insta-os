---
name: marca
description: Carrega o perfil da marca (tom de voz, visual, pilares, públicos, portfólio, contas e regras) que todas as skills do insta-os usam. Use antes de escrever legenda, post, carrossel, story, reel, mensagem de prospecção ou de indicação, ou quando pedirem algo "no estilo da marca".
---

# Marca (base do insta-os)

Todas as skills do plugin partem do **perfil da marca**. O conhecimento técnico de Instagram está na skill `playbook-instagram`; leia o arquivo de referência dela que corresponde à tarefa.

## Onde está o perfil

Procure nesta ordem e use o primeiro que existir:
1. `references/perfil.md` desta skill (versão personalizada do plugin, gerada pela skill `configurar`).
2. `.insta-os/perfil.md` na pasta de trabalho ou no repositório aberto.
3. Um perfil colado pelo usuário na conversa ou guardado num projeto/documento que ele indicar.

Se nenhum existir, ou se ainda estiver com os campos do modelo (`[preencher]`), rode a skill `configurar` antes de produzir qualquer peça. O formato do perfil está em `references/perfil-modelo.md`; um exemplo preenchido (marca fictícia) está em `exemplos/perfil-exemplo.md` na raiz do plugin.

Leia o perfil inteiro na primeira tarefa da conversa. Se o perfil apontar um design system ou manual de marca, leia também: ele vence o perfil em questões visuais.

## Regras que valem para todo o plugin

1. **Nada sai sem aprovação.** Publicar, agendar, subir mídia num repositório público, enviar DM, e-mail ou WhatsApp exige um "sim" explícito do usuário para aquele item.
2. **Fatos só de fonte real.** Números da empresa, resultados de cliente, depoimentos e preços vêm do usuário, do site ou do cliente. Nunca invente métrica, depoimento ou case. Sem dado, pergunte ou marque `[confirmar]`.
3. **Portfólio por status.** O perfil classifica cada projeto: *cliente real* (com ou sem autorização de divulgação), *produto próprio*, *projeto conceito* ou *proibido*. Projeto conceito nunca aparece como trabalho feito para aquela empresa; proibido não aparece em nenhuma peça; case de cliente só com autorização registrada.
4. **Dados de clientes.** Nunca mostre faturamento, vendas, nomes ou contatos reais de clientes do cliente. Em prints de sistemas, borre ou substitua por exemplos **na imagem**; se precisar trocar texto na tela antes do print, avise antes, nunca clique, preencha ou salve nada e recarregue a página depois.
5. **Áreas com login.** Nunca digite senha nem crie conta. O usuário faz o login no navegador; você só captura.
6. **Formato Instagram:** feed e carrossel 1080×1350 (4:5); reels e stories 1080×1920 com área segura (detalhes no playbook).
7. **Conteúdo com IA:** cenas ou imagens geradas por IA levam o rótulo de IA do Instagram (`isAiGenerated: true` no agendamento).
8. **Locução:** marcas pela pronúncia registrada no perfil. Roteiros para ElevenLabs têm só as falas com as tags de entonação, sem numeração.

## Como as skills se encaixam

```
configurar ──► perfil da marca ──► (todas as skills)

calendario-semanal ──► anuncio-motion-video (reel)
        │          ──► case-de-projeto (carrossel de prova)
        │          ──► post-educativo (carrossel educativo)
        │          ──► stories
        ▼
   Metricool (agenda, após aprovação; mídia via repositório público)
        ▼
relatorio-semanal ──► ajusta a próxima pauta

prospeccao-ativa ──► pipeline de leads ◄── indicacoes
case-de-projeto  ──► pede depoimento e indicação ao cliente
```
