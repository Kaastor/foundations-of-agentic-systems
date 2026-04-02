# Diagnoza niepowodzenia: boundary_handoff

## Diagnoza wariant po wariancie

- `model_only` nie przeszedł z diagnozami `stop, goal, grounding, action` i blokerami: boundary: request includes deferred topics and requires a boundary note, goal: unresolved ambiguity prevents a bounded review, grounding: final review lacks sufficient citations, goal: comparison requested but output does not compare alternatives.
- `scripted_pipeline` nie przeszedł z diagnozami `stop, goal, grounding` i blokerami: boundary: request includes deferred topics and requires a boundary note, goal: unresolved ambiguity prevents a bounded review, grounding: final review lacks sufficient citations, goal: comparison requested but output does not compare alternatives, goal: recommendation requested but output does not defend one.
- `tool_rich_memoryless` nie przeszedł z diagnozami `stop, goal, grounding` i blokerami: boundary: request includes deferred topics and requires a boundary note, goal: unresolved ambiguity prevents a bounded review, grounding: final review lacks sufficient citations, goal: comparison requested but output does not compare alternatives, goal: recommendation requested but output does not defend one.
- `memory_rich_tool_poor` nie przeszedł z diagnozami `goal, grounding, stop` i blokerami: goal: unresolved ambiguity prevents a bounded review, grounding: final review lacks sufficient citations, goal: comparison requested but output does not compare alternatives, goal: recommendation requested but output does not defend one.
- `capstone_agent` nie przeszedł z diagnozami `goal, grounding, stop` i blokerami: goal: unresolved ambiguity prevents a bounded review, grounding: final review lacks sufficient citations, goal: comparison requested but output does not compare alternatives, goal: recommendation requested but output does not defend one.

## Błędne przekonania ujawnione między wariantami

- Wywołania narzędzi nie implikują sukcesu zadania; część wariantów znalazła prace, ale i tak nie przeszła końcowej weryfikacji.
- Więcej pamięci nie zawsze znaczy lepiej; stary recall może wytworzyć bloker specyficzny dla pamięci.
- Planowanie ma sens tylko wtedy, gdy zmienia zbieranie dowodów albo zachowanie `stop`.
