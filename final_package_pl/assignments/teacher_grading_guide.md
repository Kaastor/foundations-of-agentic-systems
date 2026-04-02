# Przewodnik oceniania dla prowadzącego

Ten pakiet został zaprojektowany pod:

- raportowe oddawanie zadań,
- ocenianie dużej grupy,
- pierwszy przebieg sprawdzania przez coding agenta,
- spot-check prowadzącego w przypadkach oznaczonych jako niepewne.

Używaj tego pliku razem z:

- [shared_submission_rules.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/assignments/shared_submission_rules.md)
- [shared_rubric.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/assignments/shared_rubric.md)
- folderem aktualnie ocenianego zadania

## Model oceniania

Nie próbuj wykrywać, czy student używał AI.
Użycie AI jest oczekiwane.

Sprawdzaj:

- czy raport pokazuje osąd oparty na dowodach,
- czy `Implementation Lens` jest trafny i objaśniający,
- w późniejszych zadaniach: czy opisana zmiana kodu jest ograniczona i poparta różnicą `before/after`,
- czy student porównał sensowne opcje zamiast brać pierwszą odpowiedź,
- czy krytyka i rewizja są realne,
- czy końcowy wniosek jest ograniczony i uzasadniony.

## Rekomendowany workflow oceniania

1. Przeczytaj `description.md` i `teacher_notes.md` dla danego zadania.
2. Przeczytaj raport studenta.
3. Oceń go według [shared_rubric.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/assignments/shared_rubric.md).
4. Sprawdź, czy przywołane artefakty są sensowne i rzeczywiście wspierają tezę.
5. Oznacz do ręcznego przeglądu, jeśli raport uruchamia reguły spot-checku.

## Typowe słabe wzorce

- mocno brzmiący tekst z prawie zerową pracą na artefaktach,
- powtarzanie słownictwa z książki bez zastosowania go do materiałów zadania,
- wymienienie pliku źródłowego bez wyjaśnienia, co on wnosi,
- twierdzenie, że zmiana kodu pomogła, bez pokazania różnicy `before/after`,
- krytyka czysto kosmetyczna,
- „rewizja”, która jest tylko przeformułowaniem,
- końcowe wnioski szersze niż to, co naprawdę wspiera materiał dowodowy.

## Mocne raporty wygenerowane z pomocą AI

Jeśli raport wygląda na napisany z dużą pomocą AI, ale jest merytorycznie mocny, oceniaj treść.

Nie obniżaj oceny za:

- czystą strukturę,
- płynny styl,
- dobre opracowanie tekstu.

Obniżaj ocenę za:

- słabe dowody,
- pozorną krytykę,
- nieuzasadnioną pewność siebie.

## Prompt do pierwszego przebiegu oceniania przez coding agenta

Użyj tego bloku jako instrukcji dla pierwszego przebiegu:

```text
Oceniasz jeden raport w kursie o architekturach agentowych.

Użyj tych źródeł:
- description.md dla bieżącego zadania
- teacher_notes.md dla bieżącego zadania
- shared_submission_rules.md
- shared_rubric.md
- raport studenta

Oceniaj tylko to, co jest widoczne w raporcie.
Nie karz za użycie AI.
Skup się na:
- zrozumieniu zadania,
- jakości dowodów,
- trafności Implementation Lens,
- jakości porównania i krytyki,
- jakości rewizji lub wyboru,
- ograniczonym i uzasadnionym końcowym osądzie.

Zwróć:
1. krótkie podsumowanie,
2. ocenę według kryteriów,
3. najważniejsze mocne strony,
4. najważniejsze braki,
5. informację, czy raport wymaga ręcznego sprawdzenia przez prowadzącego.
```
