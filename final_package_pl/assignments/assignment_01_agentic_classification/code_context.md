# Kontekst repozytorium

## Główne źródła

- [architecture-variants.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/code/docs/architecture-variants.md)
- [AA-S01.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/code/docs/slices/AA-S01.md)
- [comparison_matrix.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/code/examples/compare_architectures/clear_bounded_review/comparison_matrix.md)
- [fit_recommendation.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/code/examples/compare_architectures/clear_bounded_review/fit_recommendation.md)

## Wymagany Implementation Lens

Obejrzyj jeden z plików:

- [baselines.py](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/code/src/m2a/baselines.py)
- [control.py](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/code/src/m2a/control.py)

Skup się na:

- tym, jak `run_model_only` albo `run_scripted_pipeline` różni się od logiki pętli sterowania w `control.py`,
- tym, co ta różnica mówi o stałym przepływie vs wyborze kolejnych kroków zależnym od obserwacji.

## Mocne źródła dowodowe

- ślady wariantów w:
  [clear_bounded_review variants](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/code/examples/compare_architectures/clear_bounded_review/variants)
- szczególnie:
  - [model_only trace.jsonl](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/code/examples/compare_architectures/clear_bounded_review/variants/model_only/trace.jsonl)
  - [scripted_pipeline trace.jsonl](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/code/examples/compare_architectures/clear_bounded_review/variants/scripted_pipeline/trace.jsonl)
  - [capstone_agent trace.jsonl](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/code/examples/compare_architectures/clear_bounded_review/variants/capstone_agent/trace.jsonl)

## Opcjonalny workflow

```bash
poetry run m2a compare-architectures data/expected_task_specs/clear_bounded_review.json --out-dir scratch/compare-clear
```

## Ścieżka bez agenta kodującego

Zadanie można wykonać w całości na podstawie zapisanych artefaktów porównawczych i dokumentacji.
W ramach `Implementation Lens` wystarczy przeczytać jeden mały nazwany moduł źródłowy i wyjaśnić, co dzięki niemu staje się jaśniejsze.
