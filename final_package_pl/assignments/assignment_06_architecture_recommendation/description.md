# Zadanie 6: test obciążeniowy granic architektury

**Powiązane spotkanie:** [meeting_plan.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/meeting_plan.md)  
Spotkanie 6: „Jak system pozostaje ograniczony i jak porównujemy architektury?”

**Po co istnieje to zadanie:** Studenci powinni wyjść z kursu z umiejętnością porównywania architektur, respektowania granic i bronienia ograniczonej rekomendacji zamiast sloganu.

**Główny akcent pętli rozumowania:** `wygeneruj -> porównaj -> skrytykuj -> popraw -> uzasadnij`

**Oczekiwany czas:** `4 godziny`

**Poziom kodowania:** `jedna ograniczona zmiana kodu plus rerun`

## Zadanie

Napisz końcową notatkę rekomendacyjną odpowiadającą na pytanie:

`Dla jednego przypadku mieszczącego się w zakresie i jednego przypadku naciskającego na granice, która architektura pasuje najlepiej, co powinna zrobić i gdzie powinna się zatrzymać albo przekazać sprawę dalej?`

Następnie wykonaj jeden test obciążeniowy granic we własnej kopii [comparison.py](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/code/src/m2a/comparison.py):

- tymczasowo wyłącz gałąź boundary-only w `_render_recommendation()`, zmieniając linię `if task_spec.boundary_topics:` wewnątrz tej funkcji na `if False and task_spec.boundary_topics:`

Ważne:

- zmień warunek wewnątrz `_render_recommendation()`, a nie wcześniejszą logikę scoringową,
- to właśnie ta kontrola graniczna obecnie produkuje rekomendację `none_in_scope`.

Uruchom porównanie graniczne przed i po tej zmianie, a następnie oceń, czy zmodyfikowany recommender jest lepszy czy gorszy od pierwotnego ograniczonego zachowania.

Raport końcowy powinien zrobić obie rzeczy:

- obronić normalną rekomendację architektoniczną dla przypadku w zakresie,
- wyjaśnić, co test obciążeniowy granic ujawnia o tym, po co istnieje jawna obsługa `none_in_scope`,
- wyjaśnić, czy `boundary_note` po teście powinna się zmienić, czy pozostać stabilna.

## Checklista oddania

- omów jeden przypadek w zakresie i jeden przypadek graniczny,
- przywołaj artefakty porównania, diagnozy porażek i granicy,
- uruchom i przywołaj porównanie graniczne `before` i `after`,
- wykonaj dokładnie wskazaną zmianę w `comparison.py`,
- obejrzyj co najmniej jeden nazwany moduł źródłowy i wyjaśnij, jak kształtuje rekomendację albo zachowanie graniczne,
- skrytykuj warstwę rekomendacyjną po teście, a nie tylko pierwotną wersję,
- podaj ograniczoną końcową rekomendację z jawną logiką zatrzymania albo przekazania.
