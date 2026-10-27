---
name: "anuncio-motion-video"
description: "Use quando pedirem um vídeo, reel, anúncio ou publi em motion graphics: de produto (estilo SaaS launch) ou institucional da empresa (texto cinético na batida de uma música). Define estilo e pegada, escolhe padrões de cena de referência, escreve roteiro (com locução para ElevenLabs quando houver), faz um rascunho rápido para aprovação e renderiza MP4 9:16 (e 16:9 quando pedido) para o Instagram."
---

# Anúncio em motion graphics

Leia antes a skill `marca`. Quando o pedido vier do `calendario-semanal`, entregue a versão 9:16 com legenda, alt text e hashtags, e volte para o calendário.

Tudo é HTML/CSS/JS renderizado quadro a quadro (`seek(t)` determinística) mais áudio sintetizado/mixado em Python. Não é geração de vídeo realista.

## Padrões desta skill (valem para os dois modos)

1. **9:16 primeiro.** O reel é a entrega principal: projete e aprove em 1080×1920; a 16:9 é derivada e opcional (site, YouTube, LinkedIn).
2. **Área segura desde o roteiro.** Nada importante nos 250px de cima e de baixo nem nos ~120px da direita. O QA mede isso automaticamente (`references/qa.md`).
3. **Duração de reel: ~20s por padrão** (alcance: 7–15s para motion, segundo o `playbook-instagram`). Entregue também o corte de 15s. A versão completa de ~40s só quando pedirem, ou para site/LinkedIn.
4. **Gancho em até 3s.** Quadro 1 já com texto grande e movimento; a primeira informação nova antes dos 3s. Siga `playbook-instagram/references/ganchos-e-retencao.md` e `psicologia.md`; o vídeo corta logo após a recompensa, com o CTA sobreposto nos últimos 2s.
5. **Rascunho antes do render final.** Render 540p/15fps para aprovar movimento e ritmo (minutos), só então o render completo. Veja `references/render.md`.
6. **Padrões de cena de referência.** Escolha 2–4 padrões em `references/cenas-jitter.md` e `references/referencias-video.md` (texto esticado, transição por stretch, pilha de cards, revelação de produto…) e anote-os na coluna "padrão" do roteiro. São referência de movimento; nunca copie layout, marca, texto ou assets de terceiros.

## Dois modos

| | Produto | Institucional (empresa) |
|---|---|---|
| Pergunta que responde | "O que esse produto faz por mim?" | "Quem é essa empresa e por que confiar?" |
| Estrutura | gancho → produto → demo de UI → diferencial → ação → oferta → assinatura | história em atos: caos → forma → trabalho (portfólio) → números → processo → logo → CTA |
| Áudio | trilha sintetizada no BPM + narração | música editada nos acentos, sem narração (o texto carrega a história) ou com narração curta |
| Visual | UI em 3D, cursor, zoom | tipografia cinética, cenas reais P&B, carrossel 3D do portfólio, logo de estilhaços |
| Guia | `references/produto.md` | `references/institucional.md` (leia inteiro antes de começar) |

## Fluxo

Crie a lista de tarefas logo no início: briefing → identidade visual → pegada → referências de cena → roteiro (aprovação) → roteiro ElevenLabs → build → áudio → rascunho (aprovação) → render final → QA → entrega.

1. **Briefing, identidade visual, roteiro, build e áudio:** siga o guia do modo (`produto.md` ou `institucional.md`). Pergunte só o que não dá para descobrir sozinho; sem o usuário presente, assuma os padrões, diga quais assumiu e siga.
2. **Pegada** (ritmo, música, transições, acabamento por segmento): `references/pegadas.md`. Os presets em `scripts/presets.json` aplicam BPM, acordes e baixo no `music.py` com `scripts/apply_preset.py` (`--list` mostra os segmentos).
3. **Referências de cena e estilo:** `references/cenas-jitter.md` (padrões de movimento) e `references/referencias-video.md` (três vídeos de referência analisados quadro a quadro: regras de estilo, padrões com tempo e receitas JS). Se o usuário mandar um MP4 de referência, descreva o estilo com contact sheets (receita em `produto.md`, seção "Referência do usuário"). Referência é só estilo.
4. **Rascunho → aprovação → render final → montagem:** `references/render.md` (inclui `scripts/render.py`, parametrizado, que funciona com qualquer `index.html`).
5. **QA:** `references/qa.md` (contact sheets, varredura de texto fora da tela e de área segura, áudio).
6. **Entrega:** `SendUserFile` com os MP4 (`display: render`); nomes `<produto>_anuncio_9x16.mp4` e `_16x9.mp4`. Em poucas linhas: o que mostra, o que foi assumido, o que é mockup/aproximado (logo, telas, dados de exemplo) e o próximo passo natural (corte de 15s, versão 16:9, trocar locução). Legenda: gancho na primeira linha, 1 CTA, 3–5 hashtags, alt text. Se a locução final ainda não existe, entregue junto o roteiro ElevenLabs.

## Motor

A pasta `engine/` na raiz do plugin tem o ponto de partida. Copie para uma pasta de trabalho do projeto (ex.: `/home/claude/<projeto>-video/`) e adapte.

| Arquivo | O que é |
|---|---|
| `engine/exemplo-produto/index.html` | Anúncio completo de exemplo (marca fictícia "Nimbus", ~41s): `seek(t)`, 7 cenas, transições, câmera, cursor, layout vertical via `body.portrait`. Para ver o estilo, renderize alguns stills dele |
| `engine/render.py` | Render original (`PAGE=`/`URL=`); prefira `scripts/render.py` desta skill |
| `engine/music.py` | Trilha, efeitos de UI, transições e mixagem com ducking |
| `engine/tts.py` | Narração provisória local em PT-BR (Kokoro) |

**Sem o motor** (pasta `engine/` ausente): não pare. Use `scripts/render.py` e `scripts/qa_sweep.js` desta skill; construa o HTML do zero com a arquitetura descrita em `produto.md` (seção "Build da animação"); gere a trilha com os pacotes já instalados (numpy/scipy) seguindo as constantes de `produto.md` ("Áudio") e avise o usuário de que partiu do zero.

## Armadilhas conhecidas

- Rede: só GitHub e poucos hosts saem do container; npm/PyPI/HF podem falhar. Planeje com o que já existe (ffmpeg, Playwright/Chromium, numpy, scipy, onnxruntime, fontes do sistema).
- Não use `will-change` em elementos com zoom (rasteriza borrado). Evite empilhar vários blurs grandes no mesmo quadro.
- Em vídeos de produtos da própria marca, mantenha a assinatura e a marca d'água do perfil; para clientes externos, pergunte. No 9:16, a marca d'água fica abaixo de 250px (ou marque com `data-qa-ignore`).
- Música comercial (faixas de artistas): uso comercial precisa de licença ou de áudio da biblioteca do Instagram (aplicável no agendamento pelo Metricool); entregue sempre também uma versão com trilha própria sintetizada.
- MP4 até ~60MB para envio pelo chat (acima disso, aumente o CRF para 26–29).
