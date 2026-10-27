# insta-os

**O sistema operacional de Instagram para o Claude.** Pauta da semana, reels em motion graphics, carrosséis de case e educativos, stories, prospecção de clientes, indicações e relatório, tudo no tom e no visual da sua marca, com agendamento no Metricool e um playbook técnico de algoritmo, ganchos e psicologia por trás de cada peça.

[English version](README.en.md)

> Feito pela [Entropy](https://entropydev.com.br), estúdio digital de São Luís (MA), para gerenciar o nosso próprio Instagram. Agora é aberto.

---

## O que ele faz

| Skill | Para quê |
|---|---|
| `configurar` | Entrevista você, lê seu site e seu Instagram e monta o **perfil da marca** (tom, visual, públicos, portfólio, contas). Entrega uma versão do plugin já personalizada. |
| `marca` | Carrega o perfil e as regras que todas as outras skills seguem. |
| `playbook-instagram` | Base técnica: como o algoritmo distribui cada formato, ganchos e retenção, 16 princípios de psicologia com a pesquisa por trás, carrossel e design, stories, legenda e busca, captação, métricas e metas. Separa o que é **oficial** (Meta/Mosseri) do que é **medido** por terceiros. |
| `calendario-semanal` | Monta a pauta da semana (ex.: 1 reel, 1 carrossel de prova, 1 educativo + stories) nos melhores horários da sua conta, produz as peças e agenda no Metricool **depois da sua aprovação**. |
| `anuncio-motion-video` | Reels e anúncios em motion graphics renderizados quadro a quadro, 9:16 primeiro (~20s + corte de 15s): modo produto (UI em 3D, cursor, zoom) e modo institucional (texto cinético na batida da música, carrossel 3D de projetos). Pegadas por segmento com presets de trilha, biblioteca de padrões de cena, rascunho rápido para aprovação, QA automático de área segura e roteiro com entonações para ElevenLabs. |
| `case-de-projeto` | Projeto entregue → carrossel de case, legenda, stories e pedido de depoimento, sem expor dados do cliente. |
| `post-educativo` | Carrosséis que ensinam o seu cliente ideal e geram salvamentos. |
| `stories` | Sequências de bastidor, enquete, caixinha e chamada, com o texto exato de cada figurinha. |
| `prospeccao-ativa` | Encontra empresas da sua região com presença digital fraca, faz um diagnóstico de cada uma e escreve uma abordagem personalizada. **Você** envia. |
| `indicacoes` | Pede indicação no momento certo e registra os indicados. |
| `vendedor` | Trabalha o funil depois da prospecção: o que fazer hoje, cadência de follow-up, mensagem certa por etapa, objeções, proposta e fechamento. **Você** envia. |
| `analista` | Dá nota a cada post com dados do Metricool, audita o perfil (inclusive o visual da grade), acompanha concorrentes e levanta formatos em alta no nicho, para adaptar e não copiar. |
| `relatorio-semanal` | Métricas do Metricool + painel → 3 decisões para a próxima semana. |

Junto vêm o **motor de vídeo** (`engine/`, com um anúncio completo de exemplo) e um **painel** pronto de vendas e conteúdo (`templates/painel.html`, com as abas Hoje, Funil, Leads, Conteúdo e Mercado).

## Como funciona no dia a dia

```
toda segunda (tarefa agendada) ─► relatório da semana ─► pauta ─► peças prontas
                                                                   │
                         você aprova ◄─────────────────────────────┘
                              │
          artes ─► repositório público de mídia ─► Metricool ─► Instagram
```

Ou é só pedir: *"monta a pauta da semana"*, *"faz um case do projeto X"*, *"prospecta 10 lojas de roupa em Teresina"*, *"como foi o insta essa semana?"*.

**Nada é publicado, agendado ou enviado sem o seu "sim".** Mensagens de prospecção e de indicação são sempre enviadas por você.

## Instalação

**Claude Code**
```
/plugin install insta-os --marketplace danasdev/insta-os
```
(Versões mais antigas: `/plugin marketplace add danasdev/insta-os` e depois `/plugin install insta-os@insta-os`.)

**App do Claude (desktop/web)**
Baixe [`dist/insta-os.plugin`](dist/insta-os.plugin) e abra o arquivo numa conversa com o Claude para instalar.

Depois, numa conversa: **"configurar minha marca"**.

## Requisitos

**Obrigatório**
- Claude com suporte a plugins/skills (app do Claude ou Claude Code).
- Pesquisa na web ligada.

**Para cada parte funcionar no automático**

| Parte | Precisa de |
|---|---|
| Agendar posts e puxar métricas | Conector **Metricool** + conta **profissional** do Instagram ligada nele |
| Mídia indo sozinha para o Metricool | Um **repositório público no GitHub** só para mídia (o Metricool exige URL pública). Sem ele, você anexa a mídia à mão |
| Prints de sites e sistemas | **Navegador embutido** do app desktop ou **Claude no Chrome** |
| Carrosséis e artes | Tipo de artifact **Design** do Claude; sem ele, HTML exportado em PNG |
| Painel (leads, funil, notas dos posts, tendências) | **Artifacts com banco de dados** do Claude; alternativa: planilha |
| Rotina semanal | **Tarefas agendadas** do Claude |

**Vídeo em motion**
- Python 3, ffmpeg, Playwright/Chromium, numpy e scipy (a sessão em nuvem do Claude já tem).
- ~20–25 min de render para um vídeo de 50s nas duas orientações.
- Narração: ElevenLabs (opcional) ou voz local provisória (Kokoro).
- Música comercial exige licença; o motor gera trilha própria.

**Não precisa** de servidor, banco de dados próprio nem API paga além do Metricool (tem plano grátis) e, se quiser, ElevenLabs.

## Estrutura

```
.claude-plugin/        manifesto e marketplace
skills/                as 13 skills
engine/                motor de vídeo (render, música, voz) + exemplo-produto/
templates/             painel de vendas e conteúdo (artifact com banco de dados)
exemplos/              perfil de marca de exemplo (marca fictícia)
dist/                  insta-os.plugin para o app do Claude
```

## Privacidade e boas práticas embutidas

- Não inventa número, depoimento nem case; o que falta fica marcado `[confirmar]`.
- Não digita senha nem cria conta; em áreas com login, você entra e o Claude só captura.
- Borra faturamento, vendas e nomes de clientes finais nos prints.
- Respeita o limite de 5 hashtags, o rótulo de conteúdo com IA e a regra de originalidade do Instagram (2026).
- Prospecção só com dados públicos de empresas, em lotes pequenos e com saída educada.

## Contribuindo

Issues e pull requests são bem-vindos, principalmente: novos públicos e temas educativos, templates de vídeo, traduções e dados atualizados para o playbook (com fonte).

## Licença

MIT © [Entropy](https://entropydev.com.br). Quer que a gente configure o insta-os (ou monte o site e o sistema) para a sua empresa? Chama a gente: [entropydev.com.br](https://entropydev.com.br) · [@entropytech_](https://instagram.com/entropytech_).
