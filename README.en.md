# insta-os

**An Instagram operating system for Claude.** Weekly content plan, motion-graphics reels, case-study and educational carousels, stories, client prospecting, referrals and reporting — all in your brand's voice and look, scheduled through Metricool and backed by a technical playbook on the algorithm, hooks and psychology.

> Built by [Entropy](https://entropydev.com.br), a digital studio from São Luís, Brazil, to run our own Instagram. Now open source. The skills are written in Brazilian Portuguese; Claude follows them in any language you talk to it in.

## What it does

| Skill | Purpose |
|---|---|
| `configurar` | Interviews you, reads your site and Instagram, and builds your **brand profile** (voice, visuals, audiences, portfolio, accounts). Delivers a personalized copy of the plugin. |
| `marca` | Loads the profile and the rules every other skill follows. |
| `playbook-instagram` | Technical base: how the algorithm distributes each format, hooks and retention, 16 psychology principles with their research, carousel and design, stories, captions and search, lead capture, metrics and targets. Separates **official** (Meta/Mosseri) from **measured** (third-party) claims. |
| `calendario-semanal` | Plans the week (e.g. 1 reel, 1 proof carousel, 1 educational post + stories) at your account's best times, produces the pieces and schedules them in Metricool **after you approve**. |
| `anuncio-motion-video` | Frame-by-frame rendered motion ads, 9:16 first (~20s + 15s cut): product mode (3D UI, cursor, camera zoom) and brand mode (kinetic type cut to the music, 3D project carousel). Per-industry presets for the soundtrack, a scene-pattern library and 3 reference videos broken down frame by frame, a quick draft render for approval, automatic safe-zone QA and voice-over scripts with ElevenLabs tags. |
| `case-de-projeto` | Delivered project → case carousel, caption, stories and a testimonial request — without exposing client data. |
| `post-educativo` | Carousels that teach your ideal client and get saved. |
| `stories` | Behind-the-scenes, poll, question-box and call-to-action sequences. |
| `prospeccao-ativa` | Finds local businesses with a weak digital presence, diagnoses each one and drafts a personalized first message. **You** send it. |
| `indicacoes` | Asks for referrals at the right moment and logs referred leads. |
| `vendedor` | Works the funnel after prospecting: today's to-do list, follow-up cadence, the right message per stage, objection handling, proposals and closing. **You** send. |
| `analista` | Scores every post with Metricool data, audits your profile (including how the grid looks), tracks competitors and spots formats trending in your niche, to adapt, never copy. |
| `relatorio-semanal` | Metricool metrics + dashboard → 3 decisions for next week. |

Also included: the **video engine** (`engine/`, with a complete example ad) and a ready **sales and content dashboard** (`templates/painel.html`: Today, Funnel, Leads, Content, Market tabs).

**Nothing is published, scheduled or sent without your explicit "yes".**

## Install

**Claude Code**
```
/plugin install insta-os --marketplace danasdev/insta-os
```
(Older versions: `/plugin marketplace add danasdev/insta-os`, then `/plugin install insta-os@insta-os`.)

**Claude app (desktop/web)**: download [`dist/insta-os.plugin`](dist/insta-os.plugin) and open it in a Claude conversation.

Then say: **"configurar minha marca"** (set up my brand).

## Requirements

- Required: Claude with plugins/skills, web search on.
- Scheduling and metrics: **Metricool** connector + an Instagram professional account linked to it.
- Automatic media upload: a **public GitHub repo** for media (Metricool needs public URLs); otherwise attach media manually.
- Screenshots: the desktop app's **built-in browser** or **Claude in Chrome**.
- Carousels: Claude's **Design** artifact type (fallback: HTML exported to PNG).
- Dashboard: Claude **artifacts with a database** (fallback: a spreadsheet).
- Weekly routine: Claude **scheduled tasks**.
- Motion video: Python 3, ffmpeg, Playwright/Chromium, numpy, scipy (Claude's cloud sessions already have them); ~20–25 min to render a 50s video in both orientations. Commercial music needs a license; the engine can synthesize its own track.

## License

MIT © [Entropy](https://entropydev.com.br) · [@entropytech_](https://instagram.com/entropytech_)
