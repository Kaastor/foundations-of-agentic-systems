# Kontekst repozytorium

## Główne źródła

- [AA-S07.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/code/docs/slices/AA-S07.md)
- [AA-S08.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/code/docs/slices/AA-S08.md)
- [AA-S09.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/code/docs/slices/AA-S09.md)
- [capstone-synthesis-guide.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/code/docs/capstone-synthesis-guide.md)
- [misconceptions-and-failure-modes.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/code/docs/misconceptions-and-failure-modes.md)
- [deferred-topics-and-boundaries.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/code/docs/deferred-topics-and-boundaries.md)
- [clear_bounded_review comparison](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/code/examples/compare_architectures/clear_bounded_review)
- [boundary_handoff comparison](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/code/examples/compare_architectures/boundary_handoff)
- [boundary_note.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/code/examples/compare_architectures/boundary_handoff/boundary_note.md)

## Wymagana interwencja

W swojej kopii roboczej edytuj:

- [comparison.py](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/code/src/m2a/comparison.py)

Wykonaj dokładnie tę ograniczoną zmianę testu obciążeniowego wewnątrz `_render_recommendation()`:

- zmień linię `if task_spec.boundary_topics:` wewnątrz `_render_recommendation()` na `if False and task_spec.boundary_topics:`

To tymczasowo wyłącza specjalną gałąź rekomendacji `none_in_scope`, dzięki czemu możesz zobaczyć, co recommender robi bez niej.
Nie zmieniaj wcześniejszego warunku granicznego w logice scoringowej.

## Wymagany Implementation Lens

Obejrzyj jeden lub więcej plików:

- [comparison.py](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/code/src/m2a/comparison.py)
- [feedback.py](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/code/src/m2a/feedback.py)

Skup się na:

- tym, jak oceny architektury i rekomendacje dopasowania są renderowane z obserwowanych wyników przebiegów,
- tym, jak blokery i granice kształtują ograniczone rekomendacje,
- dlaczego warstwa rekomendacyjna nadal potrzebuje jawnej obsługi granic, nawet jeśli istnieją dowody porównawcze.

## Wymagane workflow

```bash
poetry run m2a compare-architectures data/expected_task_specs/boundary_handoff.json --out-dir scratch/compare-boundary-before
# make the bounded change in comparison.py
poetry run m2a compare-architectures data/expected_task_specs/boundary_handoff.json --out-dir scratch/compare-boundary-after
```

Możesz użyć zapisanego [clear_bounded_review comparison](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/code/examples/compare_architectures/clear_bounded_review) jako stabilnego odniesienia dla przypadku w zakresie.

## Mocne źródła dowodowe

- porównaj `scratch/compare-boundary-before/fit_recommendation.md` z `scratch/compare-boundary-after/fit_recommendation.md`,
- porównaj `boundary_note.md` przed i po, nawet jeśli pozostanie niezmienione,
- opcjonalnie porównaj jeden artefakt porażki albo porównania.

## Ścieżka bez agenta kodującego

Agent kodujący nie jest wymagany.
Interwencja to jedna ręczna zmiana, którą da się wykonać w dowolnym edytorze.
Chatbot może pomóc, ale rzeczywiste artefakty rekomendacyjne `before/after` musisz zweryfikować samodzielnie.
