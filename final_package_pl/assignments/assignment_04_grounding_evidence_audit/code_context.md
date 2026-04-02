# Kontekst repozytorium

## Główne źródła

- [architecture.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/code/docs/architecture.md)
- [running-case-literature-review-assistant.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/code/docs/running-case-literature-review-assistant.md)
- [AA-S05.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/code/docs/slices/AA-S05.md)
- [capstone_agent tool_observations.jsonl](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/code/examples/compare_architectures/clear_bounded_review/variants/capstone_agent/tool_observations.jsonl)
- [scripted_pipeline tool_observations.jsonl](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/code/examples/compare_architectures/clear_bounded_review/variants/scripted_pipeline/tool_observations.jsonl)
- [capstone_ambiguous_request verification.jsonl](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/code/examples/run_review/capstone_ambiguous_request/verification.jsonl)
- [starter_claim_set.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/assignments/assignment_04_grounding_evidence_audit/starter_claim_set.md)

## Wymagany Implementation Lens

Obejrzyj jeden albo oba pliki:

- [tools.py](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/code/src/m2a/tools.py)
- [feedback.py](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/code/src/m2a/feedback.py)

Skup się na:

- tym, jak kontrakty narzędziowe i wyjścia `ToolObservation` czynią część twierdzeń możliwymi do sprawdzenia,
- tym, jak `evaluate_progress` zamienia brakujące cytowania, luki tematyczne albo nierozwiązaną niejednoznaczność w jawne blokery.

## Opcjonalny workflow

```bash
poetry run m2a run-review data/expected_task_specs/clear_bounded_review.json --variant capstone_agent --out-dir scratch/run-tools
```

## Ścieżka bez agenta kodującego

Zadanie można wykonać w całości na podstawie zapisanych artefaktów.
Jeśli chcesz mieć stały punkt wyjścia, użyj starter claim set zamiast generować własny.
W ramach `Implementation Lens` wystarczy przeczytać wskazane moduły i połączyć je z zaobserwowanymi artefaktami z narzędzi i weryfikacji.
