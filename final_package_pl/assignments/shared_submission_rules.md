# Wspólne zasady oddawania prac

## Jeśli masz zapamiętać tylko pięć rzeczy

- oddajesz jeden plik: `submission.md`
- trzymasz się szablonu raportu przypisanego do zadania
- użycie AI jest dozwolone
- materiał źródłowy liczy się bardziej niż gładki styl
- każde zadanie zawiera jeden mały `Implementation Lens`, a zadania 5-6 dodatkowo wymagają jednej ograniczonej zmiany kodu i porównania `before/after`

## Tryb oddawania

Wszystkie zadania są `report_only`.

Do każdego zadania oddajesz jeden raport w Markdown.
Kanoniczna nazwa pliku to:

- `submission.md`

Eksport PDF jest dopuszczalny tylko wtedy, gdy wymaga tego platforma kursowa, ale źródłem prawdy pozostaje Markdown.

## Oczekiwany czas pracy

Domyślny czas pracy nad jednym zadaniem:

- `4 godziny`

Nie musisz wykorzystać całego czasu.
Musisz jednak wykorzystać go tak, by zebrać wystarczający materiał do obrony swojego raportu.

## Dozwolone użycie AI

Dozwolone i normalne są:

- chatboty,
- pomoc AI w redakcji,
- pomoc AI w streszczaniu,
- opcjonalna pomoc agentów kodujących,
- ograniczone ręczne zmiany kodu w zadaniach, które wyraźnie tego wymagają.

Niewymagane są:

- płatny dostęp do agentów kodujących,
- narzędzia własnościowe,
- generowanie kodu wykraczające poza to, co jest potrzebne do inspekcji, rerunu lub wykonania jednej ograniczonej zmiany wskazanej w pakiecie.

Zadania są zaprojektowane tak, aby student korzystający wyłącznie ze zwykłych chatbotów nadal mógł je ukończyć.

## Za co jesteś oceniany

Nie jesteś oceniany za ukrywanie użycia AI.
Jesteś oceniany za:

- poprawne zrozumienie zadania,
- użycie dowodów z artefaktów lub lektur kursowych,
- użycie jednego ograniczonego `Implementation Lens` z kodu źródłowego,
- porównanie kilku sensownych opcji zamiast przyjęcia pierwszej odpowiedzi,
- krytykę słabych lub niepodpartych twierdzeń,
- ograniczoną poprawkę albo obroniony wybór,
- jasne uzasadnienie końcowego osądu.

## Wymagana struktura raportu

Każdy lokalny szablon zadania jest wariantem tej samej struktury:

1. `Task`
2. `Candidate Options Or Initial Answer`
3. `Comparison Criteria`
4. `Evidence`
5. `Implementation Lens`
6. `Critique`
7. `Revision Or Selected Option`
8. `Final Justification`
9. `Uncertainty Or Remaining Weakness`

Trzymaj się lokalnego szablonu z folderu zadania, ale nie usuwaj tych głównych sekcji.

## Zasady pracy z materiałem źródłowym

Raport musi odwoływać się do konkretnych dowodów.

Dobre źródła dowodowe to:

- dokładne ścieżki plików z pakietu kursowego,
- dokładne nazwy artefaktów,
- dokładne pola, kroki, warianty lub obserwacje,
- jeden dokładny moduł źródłowy albo granica funkcji, gdy zadanie wymaga `Implementation Lens`,
- krótkie cytaty, jeśli są naprawdę potrzebne,
- porównanie dwóch jawnie nazwanych alternatyw.

Słabe odwołania to:

- szerokie parafrazy bez wskazania artefaktu,
- „AI tak powiedziało”,
- „wydaje się, że”,
- ogólne pojęcia kursowe bez związku z materiałem zadania.

## Styl cytowania

Przy odwołaniu do artefaktów kursowych używaj:

- ścieżki pliku,
- nazwy artefaktu,
- opcjonalnie pola, sekcji, kroku lub identyfikatora zdarzenia.

Przykład:

- `code/examples/compare_architectures/clear_bounded_review/comparison_matrix.md`
- `code/examples/run_review/capstone_ambiguous_request/trace.jsonl`, krok 4
- `code/examples/spec_review/ambiguous_request/task_spec.json`, warunki zatrzymania

## Ujawnianie użycia AI

Nie musisz ujawniać każdego promptu.
Musisz jednak jasno pokazać:

- od jakich opcji lub wstępnej odpowiedzi startowałeś,
- co zostawiłeś,
- co odrzuciłeś,
- co poprawiłeś.
