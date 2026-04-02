# Przewodnik dla prowadzącego

## Cel i tryb pracy

Ten dokument jest dla prowadzącego, który uczy tego kursu równolegle z własnym pogłębianiem zrozumienia systemów agentowych.

Założenie nie brzmi: „muszę opanować całe pole przed startem kursu”.
Brzmi: „muszę wejść w kurs ze stabilną mapą, a kolejne warstwy mogę uczyć się krok przed studentami”.

Używaj tego pliku razem z:

- [README.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/README.md)
- [meeting_plan.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/meeting_plan.md)
- [meeting_prep_checklist.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/meeting_prep_checklist.md)
- [code](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/code)

Wszystkie polecenia terminalowe poniżej uruchamiaj z katalogu:

- [code](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/code)

## Główna teza dydaktyczna

Ucz ze stabilnej mapy. Następną warstwę poznawaj dokładniej we właściwym momencie.

W tym kursie oznacza to:

- przed `Meeting 1` rozumiesz centralne pytanie kursu,
- przed `Meeting 1` rozumiesz sześciospotkaniowy szkielet zależności,
- przed `Meeting 1` rozumiesz przykład przewodni,
- przed `Meeting 1` rozumiesz granice kursu,
- a potem przygotowujesz się do każdego spotkania jedno ogniwo przed studentami.

To wystarczy, żeby prowadzić kurs odpowiedzialnie.

## Co musisz wiedzieć przed `Meeting 1`

Przed pierwszymi zajęciami powinieneś umieć jasno powiedzieć:

1. centralne pytanie:
   `Jak model generatywny staje się poprzez architekturę ograniczonym, ukierunkowanym na cel systemem agentowym?`
2. szkielet kursu:
   `model -> task -> loop/state/trace -> action/tools/grounding -> memory/planning -> feedback/stop/comparison`
3. przykład przewodni:
   jeden ograniczony, offline’owy asystent do przeglądu literatury używany przez cały kurs
4. główne kontrasty architektoniczne:
   `model_only`, `scripted_pipeline`, `tool_rich_memoryless`, `memory_rich_tool_poor`, `capstone_agent`
5. trzy główne workflowy:
   `m2a spec-review`, `m2a run-review`, `m2a compare-architectures`
6. granice kursu:
   nie uczysz tu RL, wnętrza IR, formalizmów planowania symbolicznego, wdrożeń ani frameworków vendorowych

Jeśli te sześć punktów jest stabilne w głowie, możesz przygotowywać się do kursu lokalnie, spotkanie po spotkaniu.

## Co przeczytać i uwewnętrznić przed `Meeting 1`

### Z książki

Przeczytaj najpierw:

- [book.pdf](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/book/book.pdf)
  Rozdział 1, strony 7-15
- [book.pdf](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/book/book.pdf)
  Rozdział 2, strony 16-23
- [book.pdf](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/book/book.pdf)
  Rozdział 3, strony 24-31

Potem przejrzyj orientacyjnie:

- [book.pdf](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/book/book.pdf)
  Rozdziały 4-9, strony 32-85

Opcjonalnie:

- [book.pdf](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/book/book.pdf)
  Rozdział 10, strony 86-98

Z książki masz wynieść przede wszystkim:

- różnicę między modelem, workflowem skryptowym i systemem agentowym,
- fakt, że prośba użytkownika nie jest jeszcze specyfikacją zadania gotową do sterowania,
- różnicę między `context`, `state`, `trace` i `memory`,
- że użycie narzędzia ma znaczenie tylko wtedy, gdy zmienia to, co można zaobserwować i uzasadnić,
- że zatrzymanie i handoff są częścią poprawności, a nie sprzątaniem po fakcie.

### Z kodu, dokumentacji i artefaktów

Przeczytaj najpierw:

- [assignments/README.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/assignments/README.md)
- [code/README.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/code/README.md)
- [code/docs/architecture.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/code/docs/architecture.md)
- [code/docs/architecture-variants.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/code/docs/architecture-variants.md)
- [code/docs/bridge-refresh.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/code/docs/bridge-refresh.md)
- [code/docs/trace-reading.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/code/docs/trace-reading.md)
- [code/docs/running-case-literature-review-assistant.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/code/docs/running-case-literature-review-assistant.md)
- [code/docs/misconceptions-and-failure-modes.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/code/docs/misconceptions-and-failure-modes.md)
- [code/docs/deferred-topics-and-boundaries.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/code/docs/deferred-topics-and-boundaries.md)

Obejrzyj przynajmniej jeden zestaw już zapisanych artefaktów:

- [code/examples/compare_architectures/clear_bounded_review](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/code/examples/compare_architectures/clear_bounded_review)

Z kodu i artefaktów masz wynieść:

- jak model zadań pasuje do struktury kursu i co dokładnie oddają studenci,
- jakie pliki produkuje każdy workflow,
- gdzie pokazać studentom kontrast zamiast tłumaczyć go wyłącznie słownie,
- że `trace`, `state_snapshots`, `tool_observations`, `memory_log` i `stop_decision` są różnymi powierzchniami dowodowymi,
- że repozytorium uczy jednego spójnego systemu, a nie sześciu niepowiązanych dem.

## Jednorazowy dry run przed kursem

Uruchom raz przed startem kursu:

```bash
poetry install
poetry run m2a spec-review data/requests/clear_bounded_review.txt --out-dir scratch/spec-clear
poetry run m2a run-review data/expected_task_specs/clear_bounded_review.json --variant capstone_agent --out-dir scratch/run-clear
poetry run m2a compare-architectures data/expected_task_specs/clear_bounded_review.json --out-dir scratch/compare-clear
```

Celem nie jest pełne zrozumienie implementacji.
Celem jest poczuć pakiet jako działający system i zobaczyć, gdzie żyją główne artefakty.

## Rytm pracy prowadzącego

- Przed kursem: budujesz mapę mentalną, czytasz podstawowe rozdziały książki, czytasz najważniejsze dokumenty kodu i robisz jeden dry run.
- 7 dni przed spotkaniem: wracasz do odpowiedniej sekcji [meeting_plan.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/meeting_plan.md), czytasz wskazane strony z książki i wskazane dokumenty repo.
- 48 godzin przed spotkaniem: uruchamiasz jeden workflow, na którym oprzesz zajęcia, i oglądasz dokładnie artefakt, który pokażesz studentom.
- 30 minut przed zajęciami: otwierasz ponownie artefakt, pytanie końcowe i najważniejsze nieporozumienie, które chcesz wydobyć.
- Po zajęciach: zapisujesz 3-5 zdań o tym, co było niezrozumiałe i czy wybrany artefakt zadziałał.

## Metoda prowadzenia spotkań

Na każdym spotkaniu utrzymuj ten sam kształt pracy:

1. Nazwij pytanie spotkania.
2. Nazwij jedno kluczowe rozróżnienie.
3. Pokaż jeden artefakt albo jeden kontrast.
4. Poproś studentów o przewidywanie przed wyjaśnieniem.
5. Pokaż, co system faktycznie zrobił.
6. Wyjaśnij zachowanie przyczynowo, odwołując się do artefaktu.
7. Podepnij to z powrotem do sześciospotkaniowego szkieletu.
8. Powiedz wyraźnie, co zostaje odłożone na później.

Utrzymuj niezmienne przez cały kurs:

- centralne pytanie,
- kolejność spotkań,
- przykład przewodni,
- kontrasty architektoniczne,
- granice kursu.
