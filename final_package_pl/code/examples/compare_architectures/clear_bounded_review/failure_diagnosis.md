# Diagnoza niepowodzenia: clear_bounded_review

## Diagnoza wariant po wariancie

- `model_only` nie przeszedł z diagnozami `grounding, goal, action, stop` i blokerami: grounding: final review lacks sufficient citations, goal: comparison requested but output does not compare alternatives.
- `scripted_pipeline` przeszedł. Dominująca diagnoza: none.
- `tool_rich_memoryless` nie przeszedł z diagnozami `planning, grounding, stop` i blokerami: planning: missing topic coverage for grounding, grounding: final review lacks sufficient citations.
- `memory_rich_tool_poor` przeszedł. Dominująca diagnoza: none.
- `capstone_agent` przeszedł. Dominująca diagnoza: none.

## Błędne przekonania ujawnione między wariantami

- Wywołania narzędzi nie implikują sukcesu zadania; część wariantów znalazła prace, ale i tak nie przeszła końcowej weryfikacji.
- Więcej pamięci nie zawsze znaczy lepiej; stary recall może wytworzyć bloker specyficzny dla pamięci.
- Planowanie ma sens tylko wtedy, gdy zmienia zbieranie dowodów albo zachowanie `stop`.
