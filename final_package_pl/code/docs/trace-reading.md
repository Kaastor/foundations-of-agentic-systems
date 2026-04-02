# Jak czytać ślady

Repozytorium jest użyteczne tylko wtedy, gdy potrafisz odtworzyć, dlaczego dany przebieg zachował się właśnie tak.

Każdy przebieg emituje wspólny zestaw artefaktów. Czytaj je w tej kolejności.

## 1. `task_spec.json`

Ten plik mówi, co system naprawdę próbował spełnić.

Zanim ocenisz przebieg, sprawdź:

- żądane tematy,
- budżet artykułów,
- wymagania dotyczące porównania lub rekomendacji,
- flagi niejednoznaczności,
- warunki przekazania,
- granice zakresu.

## 2. `plan.json`

To jest zadeklarowana zamierzona struktura przebiegu. Nie jest dowodem, że przebieg się udał. Jest zamierzonym szkieletem sterowania.

## 3. `trace.jsonl`

To jest przyczynowy kręgosłup przebiegu. Każdy rekord zawiera:

- `step`
- `phase`
- `event_type`
- `action_name`
- `message`
- `evidence_refs`
- `data`

Ważne pytanie nie brzmi „co system powiedział?”, ale „co zmieniło się z powodu tego kroku?”.

Główne fazy to:

| Faza | Znaczenie |
| --- | --- |
| `observe` | wczytanie zadania albo stanu świata |
| `think` | propozycja kolejnego ograniczonego działania |
| `act` | wywołanie narzędzia albo draftowanie treści |
| `update` | zmiana stanu wewnętrznego bez wywołania narzędzia |
| `verify` | sprawdzenie blokerów względem jawnych kryteriów |
| `stop` | wytworzenie ograniczonego końcowego wyniku |

## 4. `state_snapshots.jsonl`

Migawki stanu odpowiadają na pytanie, na które ślad nie odpowiada: gdzie teraz żyje informacja?

Każda migawka rozdziela:

- `active_context`
- `external_state`
- `memory_summary`
- `world_outcomes`
- `unresolved_issues`

To tutaj repozytorium czyni widocznym rozróżnienie `context != state != memory`.

## 5. `tool_observations.jsonl`

To są ugruntowane obserwacje, do których można odwoływać się w późniejszych decyzjach. Wyszukiwanie, czytanie, pisanie notatek i składanie cytowań są tutaj zapisane z jawnymi wejściami i wyjściami.

## 6. `memory_log.jsonl`

To dopisywana historia pamięci. Zawiera:

- migawkę polityki,
- pamięć startową,
- zapisy,
- pobrania,
- zdarzenia zapominania.

Nie myl tego pliku z aktualnym aktywnym kontekstem. Element pamięci może istnieć, nie będąc aktywnym w bieżącym kroku.

## 7. `verification.jsonl` i `stop_decision.json`

Te dwa pliki mówią, czy przebieg naprawdę spełnił kontrakt.

Przebieg może zakończyć się normalnym sukcesem tylko wtedy, gdy końcowa weryfikacja nie zawiera blokującego problemu.

Ta reguła jest wymuszana w kodzie i testach.

## Minimalny wzorzec czytania

Gdy przebieg Cię zaskoczy, użyj takiego wzorca:

1. przeczytaj końcowe blokery w `stop_decision.json`,
2. znajdź odpowiadające im zdarzenie `verify` w `trace.jsonl`,
3. obejrzyj pobliskie obserwacje z narzędzi i zdarzenia pamięci,
4. potwierdź, która migawka stanu nadal trzymała nierozwiązany problem.

## Przykłady do przećwiczenia

Dobre miejsca do ćwiczeń:

- udany przebieg porównawczy w zakresie:
  `examples/compare_architectures/clear_bounded_review/variants/capstone_agent/`
- bloker związany ze starą pamięcią:
  `examples/run_review/capstone_stale_memory_harms/`
- wynik doprecyzowania:
  `examples/run_review/capstone_ambiguous_request/`
