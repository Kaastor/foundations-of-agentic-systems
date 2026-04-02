# Specyfikacja zadania: boundary_handoff

## Request

Review current industry benchmarks for live web retrieval agents, compare vector ranking internals, and recommend a production deployment architecture with observability.

## Pola strukturalne

- Budżet prac: 3 do 5
- Tryb porównania: True
- Wymagana rekomendacja: True
- Maksymalna liczba kroków: 20

## Cele

- Przygotować ograniczony przegląd literatury wyłącznie na bazie dostarczonego lokalnego korpusu.
- Porównać wymagane alternatywy zamiast niezależnie listować prace.
- Obronić jedną ograniczoną rekomendację architektoniczną dowodami.

## Ograniczenia

- Używaj tylko prac z lokalnego korpusu; bez live retrieval i zewnętrznych API.
- Zachowaj deterministyczność i obserwowalność przebiegu.
- Użyj od 3 do 5 prac, chyba że nastąpi poprawny handoff.

## Podcele

- Sformalizować request w jawne cele, ograniczenia i reguły zatrzymania.
- Zebrać dowody z lokalnego korpusu prac.
- Zsyntetyzować przegląd oparty na cytowaniach albo wyemitować ograniczony wynik handoff.
- Ujawnić kompromisy między porównywanymi wyborami architektonicznymi.

## Kryteria sukcesu

- Każdy wymagany temat jest pokryty dowodem z co najmniej jednej lokalnej pracy.
- Końcowy przegląd zawiera cytowania złożone z lokalnego korpusu.
- Końcowy przegląd zawiera bezpośrednie porównanie wymaganych alternatyw.
- Końcowy przegląd zawiera rekomendację opartą na dowodach.

## Kryteria zatrzymania

- Zatrzymaj się z sukcesem dopiero wtedy, gdy wszystkie kryteria sukcesu są spełnione.
- Wyemituj `clarification` albo `handoff`, gdy niejednoznaczność lub granice zakresu blokują bezpieczny przegląd.
- Jeśli po ograniczonym replanningu blokery nadal istnieją, zatrzymaj się z jawnym ograniczonym niepowodzeniem albo handoff.

## Wymagane tematy

- None

## Flagi niejednoznaczności

- Nie podano jawnego fokusowania tematycznego.
- Domena jest na tyle szeroka, że lokalny korpus może nie odpowiadać intencji użytkownika.

## Pytania doprecyzowujące

- Które pojęcia architektur agentowych powinien obejmować przegląd?

## Warunki handoff

- Niejednoznaczność pozostaje nierozwiązana po formalizacji zadania.
- Request zależy od tematów poza zakresem, takich jak RL, wnętrza IR, live retrieval, planowanie symboliczne lub operations.
- Lokalny korpus nie może wesprzeć wymaganych dowodów w ramach budżetu prac.

## Tematy graniczne

- ir_internals
- live_retrieval
- operations

## Założenia

- Nie podano jawnego budżetu prac; ustawiono domyślnie 3 do 5 lokalnych prac.
