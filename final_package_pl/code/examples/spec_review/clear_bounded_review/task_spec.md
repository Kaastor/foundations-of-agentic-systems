# Specyfikacja zadania: clear_bounded_review

## Request

Prepare a beginner-friendly literature review about planning, memory, and grounding in offline literature-review assistants. Use only the local corpus. Compare lightweight planning with more explicit architecture choices. Cite 4 local papers and stop only when each requested topic is covered with evidence.

## Pola strukturalne

- Budżet prac: 4 do 4
- Tryb porównania: True
- Wymagana rekomendacja: False
- Maksymalna liczba kroków: 20

## Cele

- Przygotować ograniczony przegląd literatury wyłącznie na bazie dostarczonego lokalnego korpusu.
- Wyjaśnić pamięć z jawnymi dowodami.
- Wyjaśnić grounding z jawnymi dowodami.
- Wyjaśnić planowanie z jawnymi dowodami.
- Porównać wymagane alternatywy zamiast niezależnie listować prace.

## Ograniczenia

- Używaj tylko prac z lokalnego korpusu; bez live retrieval i zewnętrznych API.
- Zachowaj deterministyczność i obserwowalność przebiegu.
- Użyj od 4 do 4 prac, chyba że nastąpi poprawny handoff.

## Podcele

- Sformalizować request w jawne cele, ograniczenia i reguły zatrzymania.
- Zebrać dowody z lokalnego korpusu prac.
- Zsyntetyzować przegląd oparty na cytowaniach albo wyemitować ograniczony wynik handoff.
- Ujawnić kompromisy między porównywanymi wyborami architektonicznymi.

## Kryteria sukcesu

- Każdy wymagany temat jest pokryty dowodem z co najmniej jednej lokalnej pracy.
- Końcowy przegląd zawiera cytowania złożone z lokalnego korpusu.
- Końcowy przegląd zawiera bezpośrednie porównanie wymaganych alternatyw.

## Kryteria zatrzymania

- Zatrzymaj się z sukcesem dopiero wtedy, gdy wszystkie kryteria sukcesu są spełnione.
- Wyemituj `clarification` albo `handoff`, gdy niejednoznaczność lub granice zakresu blokują bezpieczny przegląd.
- Jeśli po ograniczonym replanningu blokery nadal istnieją, zatrzymaj się z jawnym ograniczonym niepowodzeniem albo handoff.

## Wymagane tematy

- memory
- grounding
- planning

## Flagi niejednoznaczności

- None

## Pytania doprecyzowujące

- None

## Warunki handoff

- Niejednoznaczność pozostaje nierozwiązana po formalizacji zadania.
- Request zależy od tematów poza zakresem, takich jak RL, wnętrza IR, live retrieval, planowanie symboliczne lub operations.
- Lokalny korpus nie może wesprzeć wymaganych dowodów w ramach budżetu prac.

## Tematy graniczne

- None

## Założenia

- Zamierzonym odbiorcą jest początkujący, który szuka strukturalnej orientacji, a nie specjalizacji domenowej.
