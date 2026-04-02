# Wskazówki dotyczące użycia AI

## Chatboty

Przydatne do:

- wygenerowania początkowego zestawu rekomendacji,
- przewidzenia, co może zrobić wyłączenie gałęzi granicznej w `_render_recommendation()`.

## Agenci kodujący

Tylko opcjonalnie.  
Przydatni do:

- zlokalizowania dokładnego warunku do edycji wewnątrz `_render_recommendation()`,
- szybkiego porównania plików rekomendacyjnych `before` i `after`.

## Słabe użycie AI

- wykonanie patcha testu obciążeniowego i zaufanie zmienionej rekomendacji bez jej krytyki.

## Mocne użycie AI

- wygenerowanie prognozy przed testem obciążeniowym,
- użycie AI do wykonania ograniczonej zmiany,
- porównanie artefaktów rekomendacyjnych `before/after`,
- gotowość do uznania, że obciążona rekomendacja jest gorsza od pierwotnej ograniczonej reguły.
