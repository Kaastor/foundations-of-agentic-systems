# Notatki dla prowadzącego

## Po co jest to zadanie

To jest zadanie capstone dla całego sześciospotkaniowego szkieletu.

## Co powinien zawierać mocny raport

- osobne potraktowanie przypadku in-scope i boundary case,
- realne porównanie `before/after` dla rekomendacji granicznej,
- dokładnie wskazaną, ograniczoną interwencję w `comparison.py`,
- krótki `Implementation Lens`, wyjaśniający, po co warstwa rekomendacji ma jawne zarządzanie granicami,
- rozpoznanie, że `boundary_note.md` może pozostać bez zmian, bo granica repozytorium wciąż istnieje nawet wtedy, gdy warstwa rekomendacji jest przeciążona,
- jawną logikę `stop` albo `handoff`,
- ograniczone rekomendacje końcowe zamiast sloganów o „najlepszej architekturze”.

## Typowe słabe wzorce

- wybór jednej architektury jako uniwersalnie najlepszej,
- abstrakcyjne mówienie o refleksji lub weryfikacji bez użycia artefaktów,
- uznanie przeciążonej rekomendacji za lepszą tylko dlatego, że wskazuje konkretny wariant,
- ignorowanie różnicy między wynikiem rekomendacji a logiką granic repozytorium.

## Niuanse oceniania

To najbardziej syntetyczne zadanie w pakiecie.
Zostaw miejsce na różnice stylu, ale wymagaj ścisłej ograniczoności i rzeczywistej pracy na dowodach.
Najmocniejsze odpowiedzi zwykle odrzucą patch stres-testowy, ale pełna punktacja zależy od uczciwego rozumowania `before/after`, a nie od samego hasła.
