---
name: configurar
description: Configura o insta-os para uma marca — entrevista o usuário, lê o site e o Instagram, monta o perfil da marca (tom, visual, públicos, portfólio, contas) e entrega uma versão personalizada do plugin pronta para instalar. Use na primeira vez, quando disserem "configurar o insta-os", "configurar minha marca", "atualizar o perfil da marca", ou quando outra skill não encontrar o perfil.
---

# Configurar o insta-os

Objetivo: sair com um **perfil da marca** completo (formato em `marca/references/perfil-modelo.md`) e, quando possível, uma **cópia do plugin personalizada** com esse perfil embutido.

## 1. Descobrir sozinho antes de perguntar

Peça só o essencial para começar: nome da marca, site e @ do Instagram. Depois:
- WebFetch no site: o que a marca faz, para quem, serviços, preços públicos, cidade, tom dos textos.
- Visual: se houver navegador disponível (navegador embutido do app ou Claude no Chrome), leia cores (variáveis CSS, `getComputedStyle`), fontes e logo da página. Se o usuário tiver um manual de marca ou design system, peça o link e leia.
- Instagram público: bio, frequência, formatos que já usa (pela página pública ou busca; sem login).
- Metricool (se conectado): `getBrandSettings` para achar a conta, o @ ligado e o fuso.

## 2. Perguntar o que não dá para descobrir

Use AskUserQuestion, em no máximo duas rodadas de até 4 perguntas:
1. Públicos (2–3) e região de prospecção.
2. Portfólio: quais projetos são de **clientes reais** (e se autorizaram divulgação), quais são **produtos próprios**, **conceito**, e quais **não podem aparecer**.
3. Ritmo de postagem que conseguem sustentar e quem aprova.
4. Conexões que já têm ou querem: Metricool, GitHub (repositório público de mídia), pipeline de leads, ElevenLabs.
5. Fatos confirmados de cada case (antes, entrega, resultados liberados).
6. Pronúncia do nome da marca e de produtos (para locução).

## 3. Montar o perfil

Preencha todas as seções do modelo com o que descobriu e com as respostas. Mostre ao usuário um resumo (identidade, tom, visual, públicos, portfólio por status) e peça confirmação. Nada de inventar: o que faltar fica `[confirmar]`.

## 4. Conexões (opcionais)

- **Metricool**: se não estiver conectado, procure o conector no registro (palavras-chave "metricool", "social media") e sugira conectar; peça para ligar o Instagram dentro do Metricool. Registre brandId e fuso no perfil.
- **Repositório público de mídia**: o Metricool só aceita mídia por URL pública. Peça ao usuário para criar um repositório **público** vazio no GitHub (ex.: `minhamarca-midia`) e ligar o GitHub ao Claude; anexe-o com `add_repo` (access `push`), clone, crie um README com a organização das pastas (`AAAA/MM-DD-<peca>/`) e registre `dono/repo` no perfil. Sem isso, a mídia é anexada à mão no Metricool.
- **Pipeline de leads**: publique `templates/pipeline-leads.html` (raiz do plugin) como artifact com as capacidades `db` e `user`, troque as cores em `:root` pelas da marca e registre o link no perfil. Sem artifacts, use uma planilha com as mesmas colunas (ver `prospeccao-ativa/references/abordagem.md`).
- **Tarefa semanal**: ofereça criar uma tarefa agendada (ex.: segunda 8h45) que roda `relatorio-semanal` + `calendario-semanal` e deixa tudo aguardando aprovação. Coloque no prompt da tarefa os fatos fixos do perfil.

## 5. Entregar

- **App do Claude (Cowork/claude.ai):** copie o plugin para uma pasta de trabalho, grave o perfil em `skills/marca/references/perfil.md`, ajuste `name` em `.claude-plugin/plugin.json` para `insta-os-<marca>` e empacote: `zip -r insta-os-<marca>.plugin . -x "*.DS_Store"`. Envie o arquivo para o usuário instalar (e desinstalar a versão genérica, para não duplicar skills).
- **Claude Code / repositório:** grave `.insta-os/perfil.md` na raiz do projeto.
- Em qualquer caso, envie também o perfil como arquivo para o usuário guardar.

Para atualizar depois: leia o perfil atual, mude só o que o usuário pedir e entregue de novo.
