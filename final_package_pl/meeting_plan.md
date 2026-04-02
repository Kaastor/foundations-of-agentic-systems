# Plan spotkań

## Sześć spotkań

### Spotkanie 1. Co sprawia, że system jest agentowy?

**Podtytuł techniczny:** Od modelu do agenta

**Pytanie przewodnie:** Co trzeba dodać wokół modelu generatywnego, aby rozsądnie nazwać cały system agentowym?

**Dlaczego to spotkanie jest pierwsze:** Studenci potrzebują stabilnego rozróżnienia między zachowaniem model-only, skryptowymi przepływami pracy i adaptacyjnymi pętlami agentowymi, zanim zacznie mieć sens rozmowa o stanie, narzędziach, pamięci czy planowaniu.

**Akcent czytelniczy:**
- model vs system interaktywny vs skryptowy przepływ pracy vs system agentowy
- minimalna pętla sterowania
- agentowość jako własność architektury

**Uzupełniająca lektura z książki:**
- Lektura główna: `book/book.pdf`, rozdział 1, s. 7-15
- Na co zwrócić uwagę: rozróżnienie model/skryptowy/agentowy, minimalna pętla oraz przewodnie zadanie przeglądu literatury

**Wsparcie w repozytorium:**
- przegląd i ogólne ramy: `code/README.md`
- dokumenty wspierające: `code/docs/architecture-variants.md`, `code/docs/running-case-literature-review-assistant.md`, `code/docs/slices/AA-S01.md`
- artefakty referencyjne: `code/examples/compare_architectures/clear_bounded_review/`
- kod i testy: `code/src/m2a/baselines.py`, `code/src/m2a/control.py`, `code/tests/test_comparison.py`
- sugerowany workflow: `poetry run m2a compare-architectures data/expected_task_specs/clear_bounded_review.json --out-dir scratch/compare-clear`

**Akcent przykładu przewodniego:** Porównaj wersję prompt-only, wersję skryptową i wersję pętlową asystenta do przeglądu literatury.

### Spotkanie 2. Czym dokładnie jest zadanie?

**Podtytuł techniczny:** Specyfikacja zadania: cele, ograniczenia, sukces, zatrzymanie

**Pytanie przewodnie:** Jak surowa prośba użytkownika staje się jawnym kontraktem zadania, który może sterować zachowaniem systemu?

**Dlaczego to spotkanie jest drugie:** Kiedy studenci wiedzą już, jaki rodzaj systemu analizują, muszą jeszcze zrozumieć, co dokładnie system ma spełnić.

**Akcent czytelniczy:**
- prośba użytkownika vs specyfikacja zadania
- cele, ograniczenia i kryteria sukcesu
- warunki zatrzymania i przekazania
- doprecyzowanie jako pełnoprawny ruch projektowy

**Uzupełniająca lektura z książki:**
- Lektura główna: `book/book.pdf`, rozdział 2, s. 16-23
- Na co zwrócić uwagę: prośba vs specyfikacja zadania, obsługa niejednoznaczności oraz warunki zatrzymania lub przekazania

**Wsparcie w repozytorium:**
- dokument wspierający: `code/docs/slices/AA-S02.md`
- fixture’y próśb: `code/data/requests/clear_bounded_review.txt`, `code/data/requests/ambiguous_request.txt`, `code/data/requests/boundary_handoff.txt`
- artefakty referencyjne: `code/examples/spec_review/clear_bounded_review/`, `code/examples/spec_review/ambiguous_request/`, `code/examples/spec_review/boundary_handoff/`
- kod i testy: `code/src/m2a/goals.py`, `code/src/m2a/artifacts.py`, `code/tests/test_goals.py`
- sugerowane workflow:
  - `poetry run m2a spec-review data/requests/clear_bounded_review.txt --out-dir scratch/spec-clear`
  - `poetry run m2a spec-review data/requests/ambiguous_request.txt --out-dir scratch/spec-ambiguous`

**Akcent przykładu przewodniego:** Przepisz nieprecyzyjne prośby o przegląd literatury na ograniczone specyfikacje zadania.

### Spotkanie 3. Co system przenosi między krokami?

**Podtytuł techniczny:** Pętle sterowania, stan, kontekst i ślady wykonania

**Pytanie przewodnie:** Jakie informacje trwają, co się zmienia, a co znika w trakcie działania systemu?

**Dlaczego to spotkanie jest trzecie:** Nie da się rozumować o zachowaniu systemu agentowego, jeśli nie wiadomo, gdzie informacja żyje i jak przemieszcza się między krokami.

**Akcent czytelniczy:**
- pętle sterowania rozciągnięte w czasie
- kontekst vs stan zewnętrzny vs stan świata
- ślady wykonania
- plan vs ślad wykonania

**Uzupełniająca lektura z książki:**
- Lektura główna: `book/book.pdf`, rozdział 3, s. 24-31
- Opcjonalny podgląd: `book/book.pdf`, rozdział 4, s. 32-35, jeśli grupa potrzebuje wcześniejszego mostu do tematu trwałości

**Wsparcie w repozytorium:**
- dokumenty wspierające: `code/docs/trace-reading.md`, `code/docs/slices/AA-S03.md`
- artefakty referencyjne:
  - `code/examples/compare_architectures/clear_bounded_review/variants/capstone_agent/trace.jsonl`
  - `code/examples/compare_architectures/clear_bounded_review/variants/capstone_agent/state_snapshots.jsonl`
  - `code/examples/run_review/capstone_ambiguous_request/trace.jsonl`
- kod i testy: `code/src/m2a/state.py`, `code/src/m2a/control.py`, `code/tests/test_state_and_traces.py`
- sugerowany workflow: `poetry run m2a run-review data/expected_task_specs/clear_bounded_review.json --variant capstone_agent --out-dir scratch/run-clear`

**Akcent przykładu przewodniego:** Przeczytaj wielokrokowy przebieg asystenta do przeglądu literatury i wskaż miejsce, w którym błąd po raz pierwszy stał się widoczny.

### Spotkanie 4. Jak system działa i co liczy się jako podstawa źródłowa?

**Podtytuł techniczny:** Wybór działań, narzędzia i grounding

**Pytanie przewodnie:** Jak system wybiera między myśleniem, pytaniem, działaniem i zatrzymaniem oraz które obserwacje można traktować jako ugruntowaną podstawę źródłową?

**Dlaczego to spotkanie jest czwarte:** Gdy studenci potrafią już czytać pętlę, mogą zrozumieć, jak ta pętla sprzęga się z narzędziami i środowiskiem.

**Akcent czytelniczy:**
- think / ask / act / stop
- kontrakty narzędziowe
- skutki uboczne
- twierdzenia ugruntowane vs nieugruntowane

**Uzupełniająca lektura z książki:**
- Lektura główna: `book/book.pdf`, rozdział 5, s. 42-49
- Na co zwrócić uwagę: wybór działań, kontrakty narzędziowe, kanały obserwacji i ugruntowana podstawa źródłowa

**Wsparcie w repozytorium:**
- dokumenty wspierające: `code/docs/architecture.md`, `code/docs/running-case-literature-review-assistant.md`, `code/docs/slices/AA-S05.md`
- artefakty referencyjne:
  - `code/examples/compare_architectures/clear_bounded_review/variants/capstone_agent/tool_observations.jsonl`
  - `code/examples/compare_architectures/clear_bounded_review/variants/scripted_pipeline/tool_observations.jsonl`
- kod i testy: `code/src/m2a/tools.py`, `code/src/m2a/control.py`, `code/tests/test_tools.py`
- sugerowany workflow: `poetry run m2a run-review data/expected_task_specs/clear_bounded_review.json --variant capstone_agent --out-dir scratch/run-tools`

**Akcent przykładu przewodniego:** Zdefiniuj wyszukiwanie, czytanie, tworzenie notatek i sprawdzanie cytowań jako jawne kontrakty narzędziowe.

### Spotkanie 5. Co powinno się utrwalać i kiedy planowanie pomaga?

**Podtytuł techniczny:** Pamięć, planowanie i przeplanowywanie

**Pytanie przewodnie:** Jakie informacje system powinien utrwalać i kiedy jawne planowanie pomaga zamiast szkodzić?

**Dlaczego to spotkanie jest piąte:** Pamięć i planowanie stają się zrozumiałe dopiero po opanowaniu zadań, stanu, śladów i interfejsów działań.

**Akcent czytelniczy:**
- typy pamięci i polityki pamięci
- kompromisy związane z trwałością
- dekompozycja i przeplanowywanie
- systemy pamięciowe vs systemy narzędziowe

**Uzupełniająca lektura z książki:**
- Lektura główna: `book/book.pdf`, rozdział 4, s. 32-41
- Lektura uzupełniająca: `book/book.pdf`, rozdział 6, s. 50-58
- Na co zwrócić uwagę: pamięć jako polityka, dekompozycja, przeplanowywanie oraz koszt nadmiernego planowania

**Wsparcie w repozytorium:**
- dokumenty wspierające: `code/docs/slices/AA-S04.md`, `code/docs/slices/AA-S06.md`
- dane i artefakty wspierające:
  - `code/data/memory/seed_memory.jsonl`
  - `code/data/planning/greedy_trap.json`
  - `code/data/expected_task_specs/stale_memory_harms.json`
  - `code/data/expected_task_specs/tradeoff_memory_vs_tools.json`
  - `code/examples/run_review/capstone_stale_memory_harms/memory_log.jsonl`
  - `code/examples/run_review/capstone_stale_memory_harms/plan.json`
- kod i testy: `code/src/m2a/memory.py`, `code/src/m2a/planning.py`, `code/tests/test_memory.py`, `code/tests/test_planning.py`
- sugerowane workflow:
  - `poetry run m2a run-review data/expected_task_specs/stale_memory_harms.json --variant capstone_agent --out-dir scratch/run-memory`
  - `poetry run m2a compare-architectures data/expected_task_specs/tradeoff_memory_vs_tools.json --out-dir scratch/compare-tradeoff`

**Akcent przykładu przewodniego:** Porównaj asystenta pamięciowego i narzędziowego, a następnie uzasadnij minimalną strukturę planu.

### Spotkanie 6. Jak system pozostaje ograniczony i jak porównujemy architektury?

**Podtytuł techniczny:** Weryfikacja, informacja zwrotna, zatrzymanie, przekazanie i synteza architektury

**Pytanie przewodnie:** Skąd system wie, czy ma kontynuować, poprawić wynik, zatrzymać się, przekazać sprawę dalej albo wręcz zarekomendować inną architekturę?

**Dlaczego to spotkanie jest ostatnie:** To spotkanie opiera się na wszystkim, co było wcześniej: na celach, śladach, narzędziach, pamięci, planowaniu i ugruntowanej podstawie źródłowej.

**Akcent czytelniczy:**
- weryfikacja i informacja zwrotna
- refleksja powiązana z dowodami
- zatrzymanie i przekazanie
- porównywanie architektur według kształtu zadania

**Uzupełniająca lektura z książki:**
- Lektura główna: `book/book.pdf`, rozdział 7, s. 59-66; rozdział 8, s. 67-77; rozdział 9, s. 78-85
- Dalsza lektura końcowa: `book/book.pdf`, rozdział 10, s. 86-98
- Na co zwrócić uwagę: weryfikację, ograniczoną autonomię, dopasowanie architektury i uzasadnioną syntezę

**Wsparcie w repozytorium:**
- dokumenty wspierające:
  - `code/docs/slices/AA-S07.md`
  - `code/docs/slices/AA-S08.md`
  - `code/docs/slices/AA-S09.md`
  - `code/docs/capstone-synthesis-guide.md`
  - `code/docs/misconceptions-and-failure-modes.md`
  - `code/docs/deferred-topics-and-boundaries.md`
- artefakty referencyjne:
  - `code/examples/run_review/capstone_ambiguous_request/verification.jsonl`
  - `code/examples/run_review/capstone_ambiguous_request/handoff_note.md`
  - `code/examples/compare_architectures/clear_bounded_review/`
  - `code/examples/compare_architectures/boundary_handoff/`
- kod i testy: `code/src/m2a/feedback.py`, `code/src/m2a/comparison.py`, `code/src/m2a/synthesis.py`, `code/tests/test_feedback.py`, `code/tests/test_stop_and_boundary.py`, `code/tests/test_comparison.py`
- sugerowane workflow:
  - `poetry run m2a compare-architectures data/expected_task_specs/clear_bounded_review.json --out-dir scratch/compare-clear`
  - `poetry run m2a compare-architectures data/expected_task_specs/boundary_handoff.json --out-dir scratch/compare-boundary`

**Akcent przykładu przewodniego:** Diagnozuj porażki, porównuj warianty i broń ograniczonej architektury asystenta do przeglądu literatury.
