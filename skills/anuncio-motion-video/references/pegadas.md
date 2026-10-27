# Pegadas por segmento

O motor e a estrutura são os mesmos (base tech); o que muda é ritmo, música, transições e acabamento. Cada pegada tem um preset em `scripts/presets.json`.

## Como aplicar

```bash
python3 scripts/apply_preset.py --list                       # segmentos disponíveis
python3 scripts/apply_preset.py music.py alimenticio         # reescreve BPM, CHORDS e ROOTS no music.py
```

O script imprime o resto do preset (som, transições, flash, blur, visual, voz). Leve esses campos ao template e ao roteiro:

1. **Cortes na grade nova.** Recalcule `CUTS`, `END_BAR_T`, `DUR`, `VO_T` e os tempos de UI como múltiplos da batida (`60/BPM`). Um BPM diferente muda a duração das cenas: ao trocar de 100 para 110 BPM, 33 batidas passam de 19,8s para 18s.
2. **Transições.** Use só as listadas no preset (`TR` no template). Pegadas sem `whip` ou sem flash não devem tê-los.
3. **Blur.** "alto" = o padrão do template; "baixo" = reduza o raio e a duração dos blurs de entrada de texto; "médio, lento" = alongue as entradas.
4. **Timbres e bateria.** Os presets só trocam acordes e baixo. Para timbre e percussão, ajuste em `music.py` conforme o campo `som` (ex.: alimentício: pluck mais curto e quente, sem pad longo; saúde: tire kick e clap, deixe o pad; games: kick mais forte e hats em semicolcheias).
5. **Ouça e ajuste.** Os acordes dos presets são ponto de partida; você não consegue ouvir, então diga isso e peça ao usuário para conferir.

## Tabela de referência

| Segmento | BPM / música | Cortes e transições | Visual | Voz |
|---|---|---|---|---|
| **Tech / SaaS (base)** | 100 BPM, Fmaj7–Am7–Cmaj7–G, synths limpos, kick + palmas suaves | zoom-through, reveal, whip, push, fade escuro no logo; flash curto | escuro monocromático, UI em 3D, cursor | confiante, moderna |
| Alimentício / delivery | 105–115 BPM, maior, plucks quentes, ukulele/marimba sintetizada, percussão leve | cortes mais rápidos, pops com escala elástica (overshoot), menos blur | fundo claro ou quente, fotos/ilustrações do produto, cantos bem arredondados | calorosa, sorridente |
| Saúde / bem-estar | 80–90 BPM, pads longos, sem bateria pesada | fades e blur lentos, sem whip | claro, verdes/azuis suaves, muito respiro | calma, acolhedora |
| Finanças / fintech | 95–100 BPM, menor com resolução maior, sub discreto | precisos, push e zoom curtos, números em contador | escuro ou navy, dados e gráficos | séria, segura |
| Educação | 100–110 BPM, maior, leve e otimista | reveal e slide, destaques em marca-texto | claro, cores vivas controladas | didática, animada |
| Moda / beleza | 90–100 BPM, groove elegante | cortes no tempo, máscaras e wipes, tipografia serifada grande | editorial, alto contraste | sofisticada, pausada |
| Imobiliário / corporativo B2B | 85–95 BPM, piano + pad | movimentos lentos de câmera, fades | sóbrio, fotos amplas | institucional |
| Games / entretenimento | 120–128 BPM, energia alta | glitch, shake, flashes fortes | saturado, neon | empolgada |

## Pegada fora da tabela

Crie uma entrada nova em `scripts/presets.json` (mesmos campos: `bpm`, `chords`, `roots` em MIDI, `acordes_nome`, `som`, `transicoes`, `flash`, `blur`, `visual`, `voz`) e use o `apply_preset.py` normalmente. Quando o segmento pedir um movimento que o template não tem, procure um padrão em `cenas-jitter.md` antes de inventar do zero.
