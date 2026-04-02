# Kontekst repozytorium

## Główne źródła

- [trace-reading.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/code/docs/trace-reading.md)
- [AA-S03.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/code/docs/slices/AA-S03.md)
- [capstone_ambiguous_request trace.jsonl](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/code/examples/run_review/capstone_ambiguous_request/trace.jsonl)
- [capstone_ambiguous_request state_snapshots.jsonl](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/code/examples/run_review/capstone_ambiguous_request/state_snapshots.jsonl)
- [capstone_ambiguous_request stop_decision.json](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/code/examples/run_review/capstone_ambiguous_request/stop_decision.json)
- [capstone_ambiguous_request handoff_note.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/code/examples/run_review/capstone_ambiguous_request/handoff_note.md)

## Wymagany Implementation Lens

Obejrzyj jeden albo oba pliki:

- [state.py](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/code/src/m2a/state.py)
- [control.py](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/code/src/m2a/control.py)

Skup się na:

- tym, jak `RunState` zapisuje zdarzenia śladu osobno od migawek stanu,
- tym, jak pętla sterowania decyduje, kiedy doprecyzowanie albo przekazanie staje się kolejnym ograniczonym ruchem.

## Opcjonalny workflow

```bash
poetry run m2a run-review data/expected_task_specs/ambiguous_request.json --variant capstone_agent --out-dir scratch/run-ambiguous
```

## Ścieżka bez agenta kodującego

Zadanie można wykonać w całości na podstawie zapisanych artefaktów `run-review`.
W ramach `Implementation Lens` obejrzyj tylko nazwane moduły i wyjaśnij, jak oświetlają podział artefaktów.
