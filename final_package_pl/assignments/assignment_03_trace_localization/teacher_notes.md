# Notatki dla prowadzącego

## Po co jest to zadanie

To zadanie wymusza biegłość w czytaniu `trace`, zanim studenci przejdą do kompromisów związanych z narzędziami, pamięcią i planowaniem.

## Co powinien zawierać mocny raport

- rzeczywiste porównanie co najmniej dwóch możliwych punktów dowodowych,
- przyczynowe użycie zarówno `trace`, jak i `state`,
- krótki `Implementation Lens`, wyjaśniający, dlaczego system zapisuje te kanały osobno,
- wyraźne połączenie z logiką `stop` albo `handoff`.

## Typowe słabe wzorce

- opowiadanie całego przebiegu bez lokalizacji dowodu,
- wskazywanie końcowego artefaktu handoff bez wcześniejszego sygnału przyczynowego,
- mylenie `trace` z pamięcią.

## Niuanse oceniania

Różni studenci mogą wybrać sąsiadujące kroki.
Najważniejsze jest, czy uczciwie i jasno bronią kryterium „najwcześniejszego rozstrzygającego sygnału”.
Dla `Implementation Lens` wystarczy poprawne wyjaśnienie strukturalne.
