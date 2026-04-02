# Założenia

Repozytorium przyjmuje kilka wąskich założeń po to, żeby pozostać deterministyczne i dydaktyczne.

## Założenia przyjęte celowo

- „Model” jest symulowany lokalnie przez deterministyczny kod. Repo uczy architektury, a nie integracji z providerem.
- Korpus literatury jest syntetyczny i dostarczony w repo, aby uniknąć zależności sieciowych i licencyjnych.
- `Search` oznacza wyszukiwanie leksykalne po lokalnym korpusie, a nie live retrieval.
- `Clarification` i `handoff` są emitowane jako artefakty, a nie interaktywne pytania do użytkownika.
- Domyślne środowisko jest offline i CPU-only.
- Preferowane są artefakty tekstowe, a nie stan ukryty lub binarny.

## Małe wnioskowania wynikające z niedookreślenia

- Budżet liczby prac jest parsowany z prośby, jeśli to możliwe, a w przeciwnym razie przyjmuje `3..5`.
- Jeśli prośba nie określa odbiorcy, repo zakłada początkującego, który chce zbudować strukturalną orientację.
- Workflow porównania capstone może zarekomendować `none_in_scope`, gdy zadanie jest zdominowane przez odłożone tematy.

## Które założenia należy przenosić dalej

- `Do transfer`: utrzymuj domyślne założenia jawne i widoczne w kodzie, artefaktach i dokumentacji.
- `Do transfer`: preferuj ograniczone wyniki, takie jak `clarification` albo `handoff`, zamiast udawać, że system rozwiązuje odłożone tematy.
- `Do transfer`: pozwól logice porównań rekomendować brak architektury in-scope, gdy dowody do tego prowadzą.

## Które założenia są uproszczeniami dydaktycznymi

- `Do not overgeneralize`: deterministyczny symulator modelu.
- `Do not overgeneralize`: syntetyczny lokalny korpus.
- `Do not overgeneralize`: wyszukiwanie leksykalne jako jedyny mechanizm retrieval.
- `Do not overgeneralize`: artefaktowe `clarification` zamiast interaktywnego kanału użytkownika.

## Czym te założenia nie są

To nie są ukryte wymagania produktowe.
To jawne decyzje projektowe, które utrzymują repozytorium w zamierzonym zakresie.
