# Kontekst repozytorium

## Główne źródła

- [AA-S04.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/code/docs/slices/AA-S04.md)
- [AA-S06.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/code/docs/slices/AA-S06.md)
- [greedy_trap.json](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/code/data/planning/greedy_trap.json)
- [capstone_stale_memory_harms memory_log.jsonl](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/code/examples/run_review/capstone_stale_memory_harms/memory_log.jsonl)
- [capstone_stale_memory_harms plan.json](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/code/examples/run_review/capstone_stale_memory_harms/plan.json)
- [tradeoff comparison_matrix.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/code/examples/compare_architectures/clear_bounded_review/comparison_matrix.md)

## Wymagana interwencja

W swojej kopii roboczej edytuj:

- [control.py](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/code/src/m2a/control.py)

Wykonaj dokładnie tę ograniczoną zmianę wewnątrz `_memory_policy_for()` dla `capstone_agent`:

- zmień `stale_after_steps=5` na `stale_after_steps=1`,
- zmień `allow_stale_recall=False` na `allow_stale_recall=True`.

To jest celowy test obciążeniowy obsługi starej pamięci.

## Wymagany Implementation Lens

Obejrzyj:

- [control.py](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/code/src/m2a/control.py)
- [memory.py](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/code/src/m2a/memory.py)

Skup się na:

- tym, jak skonfigurowana jest polityka pamięci capstone,
- tym, jak stare wpisy są oznaczane i pobierane,
- dlaczego luźniejsza polityka przywoływania starej pamięci może zmienić dalszą weryfikację albo zachowanie przy zatrzymaniu.

## Wymagane workflow

```bash
poetry run m2a run-review data/expected_task_specs/stale_memory_harms.json --variant capstone_agent --out-dir scratch/run-memory-before
# make the bounded change in control.py
poetry run m2a run-review data/expected_task_specs/stale_memory_harms.json --variant capstone_agent --out-dir scratch/run-memory-after
```

## Mocne źródła dowodowe

- porównaj `scratch/run-memory-before/memory_log.jsonl` z `scratch/run-memory-after/memory_log.jsonl`,
- porównaj `scratch/run-memory-before/verification.jsonl` z `scratch/run-memory-after/verification.jsonl`,
- porównaj `scratch/run-memory-before/stop_decision.json` z `scratch/run-memory-after/stop_decision.json`,
- opcjonalnie porównaj `plan.json` i `final_review.md`.

## Ścieżka bez agenta kodującego

Agent kodujący nie jest wymagany.
Interwencja to mała ręczna zmiana, którą da się wykonać w dowolnym edytorze.
Chatbot może pomóc, ale rzeczywiste artefakty `before/after` musisz zweryfikować samodzielnie.
