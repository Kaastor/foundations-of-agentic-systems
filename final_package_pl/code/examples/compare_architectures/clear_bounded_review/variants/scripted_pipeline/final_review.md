# Przegląd literatury: clear_bounded_review

Wariant: `scripted_pipeline`

## Zakres

Przygotuj przyjazny dla początkujących przegląd literatury o planowaniu, pamięci i groundingu w offline’owych asystentach do przeglądu literatury. Użyj tylko lokalnego korpusu. Porównaj lekkie planowanie z bardziej jawnymi wyborami architektonicznymi. Zacytuj 4 lokalne prace i zatrzymaj się dopiero wtedy, gdy każdy wymagany temat jest pokryty dowodami.

## Ustalenia według tematów

### Pamięć

Pamięć musi obejmować politykę odczytu i zapominania, a nie tylko przechowywanie. Niekontrolowana stara pamięć sprawia, że refleksja wygląda na bardziej wiarygodną, niż pozwalają na to dowody. [P04-MemoryPolicy] [P13-StaleReflection]

### Grounding

Wybór uwzględniający pokrycie i planowanie specyficzne dla tematu lepiej odzyskują brakujące dowody niż zachłanny wybór top-k. [P14-CoverageTrap]

### Planowanie

Lekkie rozbicie zadania daje wystarczającą strukturę dla małych zadań przeglądowych bez ciężkiego planowania formalnego. Wybór uwzględniający pokrycie i planowanie specyficzne dla tematu lepiej odzyskują brakujące dowody niż zachłanny wybór top-k. [P06-PlanSketch] [P14-CoverageTrap]

## Porównanie

`MemoryPolicy: When Notes Help and When They Mislead` podkreśla pamięć i stan, podczas gdy `CoverageTrap: Why Greedy Paper Selection Misses Evidence Linking` podkreśla planowanie i grounding. Wybór architektury zależy więc od tego, czy wąskim gardłem zadania jest dostęp do dowodów, retencja czy dyscyplina sterowania. [P04-MemoryPolicy] [P14-CoverageTrap]

## Cytowania

- [P04-MemoryPolicy] MemoryPolicy: When Notes Help and When They Mislead (2024)
- [P06-PlanSketch] PlanSketch: Lightweight Decomposition for Small Review Tasks (2023)
- [P13-StaleReflection] Stale Reflection Notes and the Cost of Unchecked Recall (2023)
- [P14-CoverageTrap] CoverageTrap: Why Greedy Paper Selection Misses Evidence Linking (2024)
