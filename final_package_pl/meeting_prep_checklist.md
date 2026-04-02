# Checklista przygotowania do spotkań

Używaj tego pliku jako operacyjnej checklisty prowadzenia kursu spotkanie po spotkaniu bez gubienia całościowej mapy.

Wszystkie polecenia terminalowe poniżej uruchamiaj z katalogu:

- [code](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/code)

Stały rytm dla każdego spotkania:

- `7 dni wcześniej`
- `48 godzin wcześniej`
- `30 minut wcześniej`
- `nie zapomnij`

## Przed startem kursu

### Przed `Meeting 1`: zadania uruchomieniowe kursu

Wykonaj zadania uruchomieniowe kursu przed pierwszymi zajęciami:

- uzupełnić lokalne pola instancji kursu w [lesson_0.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/assignments/lesson_0.md)
- utworzyć przestrzeń lub kanał `Teams`
- skonfigurować workflow oddawania prac:
  GitHub Classroom, jedno repozytorium na studenta lub inna ustalona ścieżka repozytoryjna
- przygotować szablon repozytorium studenta lub strukturę starter repo, jeśli będzie używana
- zweryfikować oczekiwaną strukturę oddawania:
  jeden plik `submission.md` na zadanie
- ustalić i opublikować terminy spotkań, godziny oraz salę albo link zdalny
- ustalić i opublikować terminy zadań
- ustalić wagi ocen, jeśli będą używane
- wysłać studentom ścieżkę dostępu do pakietu
- wysłać studentom [STUDENT_SETUP.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/STUDENT_SETUP.md)
- wysłać studentom [book.pdf](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/book/book.pdf) z instrukcją:
  rozdział 1, strony 7-15 przed `Meeting 1`
- zweryfikować repozytorium raz samodzielnie przez jednorazowy dry run poniżej

### Minimalna mapa mentalna przed `Meeting 1`

Przed pierwszymi zajęciami upewnij się, że umiesz wyjaśnić:

- centralne pytanie kursu:
  `Jak model generatywny staje się poprzez architekturę ograniczonym, ukierunkowanym na cel systemem agentowym?`
- sześciospotkaniowy szkielet:
  `model -> task -> loop/state/trace -> action/tools/grounding -> memory/planning -> feedback/stop/comparison`
- przykład przewodni:
  jeden offline’owy asystent do przeglądu literatury używany przez cały kurs
- główne kontrasty architektoniczne:
  `model_only`, `scripted_pipeline`, `tool_rich_memoryless`, `memory_rich_tool_poor`, `capstone_agent`
- workflowy operacyjne:
  `m2a spec-review`, `m2a run-review`, `m2a compare-architectures`
- granice kursu:
  nie RL, nie wnętrza IR, nie formalizmy planowania symbolicznego, nie wdrożenie, nie frameworki vendorowe

### Co przeczytać i uwewnętrznić przed `Meeting 1`

Z książki przeczytaj:

- [book.pdf](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/book/book.pdf)
  Rozdział 1, strony 7-15
- [book.pdf](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/book/book.pdf)
  Rozdział 2, strony 16-23
- [book.pdf](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/book/book.pdf)
  Rozdział 3, strony 24-31

Potem przejrzyj orientacyjnie:

- [book.pdf](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/book/book.pdf)
  Rozdziały 4-9, strony 32-85

Z warstwy zadań przeczytaj:

- [assignments/README.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/assignments/README.md)

Z kodu i dokumentacji przeczytaj:

- [code/README.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/code/README.md)
- [code/docs/architecture.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/code/docs/architecture.md)
- [code/docs/architecture-variants.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/code/docs/architecture-variants.md)
- [code/docs/bridge-refresh.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/code/docs/bridge-refresh.md)
- [code/docs/trace-reading.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/code/docs/trace-reading.md)
- [code/docs/running-case-literature-review-assistant.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/code/docs/running-case-literature-review-assistant.md)
- [code/docs/misconceptions-and-failure-modes.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/code/docs/misconceptions-and-failure-modes.md)
- [code/docs/deferred-topics-and-boundaries.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/code/docs/deferred-topics-and-boundaries.md)

Obejrzyj:

- [code/examples/compare_architectures/clear_bounded_review](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/code/examples/compare_architectures/clear_bounded_review)

Uwewnętrznij:

- jak model zadań pasuje do struktury kursu i co dokładnie oddają studenci,
- różnicę między `model-only`, skryptowym workflowem i sterowaniem agentowym,
- różnicę między `request`, `task spec`, `trace`, `state`, `memory` i `evidence`,
- że ten sam przykład przewodni wraca we wszystkich workflowach,
- że kurs jest ograniczony i architektoniczny, a nie przekrojowy.

### Jednorazowy dry run

Uruchom raz przed startem kursu:

```bash
poetry install
poetry run m2a spec-review data/requests/clear_bounded_review.txt --out-dir scratch/spec-clear
poetry run m2a run-review data/expected_task_specs/clear_bounded_review.json --variant capstone_agent --out-dir scratch/run-clear
poetry run m2a compare-architectures data/expected_task_specs/clear_bounded_review.json --out-dir scratch/compare-clear
```

## Meeting 1

### 7 dni wcześniej

- Przeczytaj część `Meeting 1` w [meeting_plan.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/meeting_plan.md)
- Przeczytaj rozdział 1 książki, strony 7-15
- Przeczytaj [AA-S01.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/code/docs/slices/AA-S01.md)
- Przeczytaj [architecture-variants.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/code/docs/architecture-variants.md)
- Obejrzyj [clear_bounded_review](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/code/examples/compare_architectures/clear_bounded_review)

### 48 godzin wcześniej

- Uruchom `poetry run m2a compare-architectures data/expected_task_specs/clear_bounded_review.json --out-dir scratch/compare-clear`
- Wybierz pierwszy kontrast, który pokażesz:
  `model_only` vs `scripted_pipeline` albo `scripted_pipeline` vs `capstone_agent`
- Przygotuj jedno zdanie:
  `agentowość to architektura sterowania, a nie samo użycie narzędzi`

### 30 minut wcześniej

- Otwórz ponownie `scratch/compare-clear/comparison_matrix.md` albo commitowany przykład porównania
- Otwórz krótki `trace.jsonl` dla wybranego kontrastu
- Ustal pytanie końcowe:
  `Co sprawia, że ten system jest agentowy, a nie tylko interaktywny albo skryptowy?`

### Nie zapomnij

- Wydobądź błędne przekonanie:
  `agent to po prostu chatbot z lepszym promptem`

## Meeting 2

### 7 dni wcześniej

- Przeczytaj część `Meeting 2` w [meeting_plan.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/meeting_plan.md)
- Przeczytaj rozdział 2 książki, strony 16-23
- Przeczytaj [AA-S02.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/code/docs/slices/AA-S02.md)
- Obejrzyj przykłady `spec_review` dla `clear_bounded_review` i `ambiguous_request`

### 48 godzin wcześniej

- Uruchom `poetry run m2a spec-review data/requests/clear_bounded_review.txt --out-dir scratch/spec-clear`
- Uruchom `poetry run m2a spec-review data/requests/ambiguous_request.txt --out-dir scratch/spec-ambiguous`
- Porównaj oba `task_spec.json`
- Przygotuj zdanie:
  `request to jeszcze nie task spec gotowy do sterowania`

### 30 minut wcześniej

- Otwórz oba `task_spec.json`
- Zdecyduj, którą różnicę pokażesz najpierw: niejednoznaczność, warunki zatrzymania czy ograniczenia zakresu
- Ustal pytanie końcowe:
  `Co zmienia się, gdy ogólna prośba staje się jawną specyfikacją zadania?`

### Nie zapomnij

- Wydobądź błędne przekonanie:
  `dobry prompt wystarczy`

## Meeting 3

### 7 dni wcześniej

- Przeczytaj część `Meeting 3` w [meeting_plan.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/meeting_plan.md)
- Przeczytaj rozdział 3 książki, strony 24-31
- Opcjonalnie: rozdział 4, strony 32-35
- Przeczytaj [trace-reading.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/code/docs/trace-reading.md)
- Przeczytaj [AA-S03.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/code/docs/slices/AA-S03.md)
- Obejrzyj jeden `trace.jsonl` i odpowiadający mu `state_snapshots.jsonl`

### 48 godzin wcześniej

- Otwórz commitowany przykład `capstone_ambiguous_request`
- Zidentyfikuj najwcześniejszy krok, który rzeczywiście pokazuje konieczność `clarification` albo `handoff`
- Przygotuj jedno zdanie:
  `trace pokazuje kolejność przyczynową, a state pokazuje gdzie informacja aktualnie żyje`

### 30 minut wcześniej

- Otwórz ponownie `trace.jsonl`, `state_snapshots.jsonl` i `handoff_note.md`
- Ustal pytanie końcowe:
  `Jaki był najwcześniejszy rozstrzygający sygnał, że system nie powinien iść dalej zwykłą ścieżką sukcesu?`

### Nie zapomnij

- Wydobądź błędne przekonanie:
  `najważniejszy jest tylko końcowy wynik`

## Meeting 4

### 7 dni wcześniej

- Przeczytaj część `Meeting 4` w [meeting_plan.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/meeting_plan.md)
- Przeczytaj rozdział 5 książki, strony 42-49
- Przeczytaj [AA-S05.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/code/docs/slices/AA-S05.md)
- Przeczytaj [AA-S07.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/code/docs/slices/AA-S07.md)
- Obejrzyj `tool_observations.jsonl` i `verification.jsonl` z jednego udanego przebiegu

### 48 godzin wcześniej

- Otwórz materiały dla `clear_bounded_review`
- Przygotuj dwa krótkie twierdzenia: jedno dobrze ugruntowane i jedno zbyt mocne
- Przygotuj jedno zdanie:
  `wywołanie narzędzia nie jest jeszcze groundingiem`

### 30 minut wcześniej

- Otwórz `tool_observations.jsonl`, `verification.jsonl` i końcowy artefakt tekstowy
- Ustal pytanie końcowe:
  `Po czym poznajemy, że twierdzenie jest wsparte przez artefakty, a nie tylko brzmi wiarygodnie?`

### Nie zapomnij

- Wydobądź błędne przekonanie:
  `jeśli system użył narzędzia, to wynik jest ugruntowany`

## Meeting 5

### 7 dni wcześniej

- Przeczytaj część `Meeting 5` w [meeting_plan.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/meeting_plan.md)
- Przeczytaj rozdział 6 książki, strony 50-58
- Przeczytaj [AA-S04.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/code/docs/slices/AA-S04.md)
- Przeczytaj [AA-S06.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/code/docs/slices/AA-S06.md)
- Obejrzyj `memory_log.jsonl`, `plan.json` i artefakty dla `stale_memory_harms`

### 48 godzin wcześniej

- Przejdź raz ścieżkę zadania 5
- Sprawdź, że ograniczona zmiana kodu daje czytelną różnicę w `memory_log.jsonl`, `verification.jsonl` i `stop_decision.json`
- Przygotuj jedno zdanie:
  `pamięć jest polityką, a planowanie jest polityką wyboru, nie ogólną inteligencją`

### 30 minut wcześniej

- Otwórz ponownie `before/after` dla zadania 5
- Ustal pytanie końcowe:
  `Co dokładnie zmieniła mała zmiana polityki pamięci i dlaczego to ma znaczenie dla ograniczonego zachowania systemu?`

### Nie zapomnij

- Wydobądź błędne przekonanie:
  `więcej pamięci i więcej planowania zawsze pomaga`

## Meeting 6

### 7 dni wcześniej

- Przeczytaj część `Meeting 6` w [meeting_plan.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/meeting_plan.md)
- Przeczytaj rozdziały 7-10 wskazane w planie spotkania
- Przeczytaj [AA-S08.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/code/docs/slices/AA-S08.md)
- Przeczytaj [AA-S09.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/code/docs/slices/AA-S09.md)
- Obejrzyj artefakty `compare_architectures` dla `clear_bounded_review` i `boundary_handoff`

### 48 godzin wcześniej

- Przejdź raz ścieżkę zadania 6
- Sprawdź, że ograniczona zmiana w `comparison.py` daje czytelną różnicę w warstwie rekomendacji
- Przygotuj jedno zdanie:
  `dobra architektura to taka, która umie również powiedzieć: nie tutaj`

### 30 minut wcześniej

- Otwórz ponownie `comparison_matrix.md`, `fit_recommendation.md` i `boundary_note.md`
- Ustal pytanie końcowe:
  `Kiedy poprawna rekomendacja powinna wskazać architekturę, a kiedy powinna odmówić zamknięcia zadania in-scope?`

### Nie zapomnij

- Wydobądź błędne przekonanie:
  `najlepsza architektura jest zawsze ta sama`
