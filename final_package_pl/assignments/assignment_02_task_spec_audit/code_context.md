# Kontekst repozytorium

## Główne źródła

- [AA-S02.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/code/docs/slices/AA-S02.md)
- [ambiguous_request task_spec.json](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/code/examples/spec_review/ambiguous_request/task_spec.json)
- [clear_bounded_review task_spec.json](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/code/examples/spec_review/clear_bounded_review/task_spec.json)
- [boundary_handoff task_spec.json](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/code/examples/spec_review/boundary_handoff/task_spec.json)

## Wymagany Implementation Lens

Obejrzyj jeden albo oba pliki:

- [goals.py](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/code/src/m2a/goals.py)
- [schemas.py](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/code/src/m2a/schemas.py)

Skup się na:

- tym, jak `build_task_spec` zamienia prośbę w jawne pola,
- tym, jak `TaskSpec.validate()` czyni część z tych pól nieopcjonalnymi dla dalszego sterowania.

## Opcjonalny workflow

```bash
poetry run m2a spec-review data/requests/ambiguous_request.txt --out-dir scratch/spec-ambiguous
```

## Mocne źródła dowodowe

- porównaj trzy zapisane pliki `task_spec.json`,
- obejrzyj odpowiadające im pliki `task_spec.md`, aby zobaczyć różnice w sformułowaniu.

## Ścieżka bez agenta kodującego

Zadanie można wykonać w całości na podstawie zapisanych przykładów i dokumentacji.
W ramach `Implementation Lens` wystarczy przeczytać wskazane moduły źródłowe i połączyć je z zapisanymi artefaktami `task_spec.json`.
