# Student Setup

Ten plik opisuje wyłącznie:

- konfigurację lokalną,
- uruchamianie repozytorium,
- to, które zadania wymagają rerunów.

W sprawie terminów i workflow oddawania prac użyj logistyki przekazanej podczas `Lesson 0` i na `Teams`.
W sprawie modelu zadań użyj [assignments/README.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/assignments/README.md).

## Minimalna konfiguracja

Potrzebujesz:

- `python3.11+`,
- lokalnej kopii pakietu kursowego,
- edytora tekstu.

Pomocne, ale niewymagane:

- `poetry`,
- `git`,
- coding agent.

## Standardowa ścieżka setupu

Uruchamiaj te polecenia z [code](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/code):

```bash
poetry install
poetry run m2a spec-review data/requests/clear_bounded_review.txt --out-dir scratch/spec-clear
poetry run m2a run-review data/expected_task_specs/clear_bounded_review.json --variant capstone_agent --out-dir scratch/run-clear
poetry run m2a compare-architectures data/expected_task_specs/clear_bounded_review.json --out-dir scratch/compare-clear
```

## Jednokomendowy check setupu

```bash
poetry run m2a compare-architectures data/expected_task_specs/clear_bounded_review.json --out-dir scratch/setup-check
```

Jeśli setup działa, powinny pojawić się:

- `scratch/setup-check/comparison_matrix.md`
- `scratch/setup-check/fit_recommendation.md`

## Ścieżka read-only vs rerun

Zadania 1-4 można wykonać z zapisanych artefaktów w [code/examples](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/code/examples).

Zadania 5-6 wymagają rerunów i jednej ograniczonej zmiany kodu.

## Wymagania runtime dla poszczególnych zadań

- Zadania 1-4:
  - zapisane artefakty wystarczą,
  - rerun jest opcjonalny
- Zadanie 5:
  - jedna ograniczona zmiana kodu w [control.py](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/code/src/m2a/control.py)
  - jeden rerun `before/after`
- Zadanie 6:
  - jedna ograniczona zmiana kodu w [comparison.py](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/code/src/m2a/comparison.py)
  - jeden rerun `before/after`

## Bezpieczny wzorzec dla zadań 5-6

1. skopiuj repozytorium albo zapisz aktualny stan,
2. uruchom komendę `before`,
3. zrób dokładnie tę ograniczoną zmianę z zadania,
4. uruchom komendę `after`,
5. porównaj tylko artefakty wskazane w zadaniu,
6. cofnij lokalną zmianę po zakończeniu albo pracuj na osobnej kopii.

## Jeśli setup nie działa

Najpierw napisz na `Teams`.

Jeśli potrzebujesz fallbacku runtime:

```bash
PYTHONPATH=src python3.13 -m m2a.cli ...
```
