# Błędne przekonania i tryby awarii

Repozytorium jest zbudowane tak, aby uczący się mogli *zobaczyć* typowe błędy architektury agentowej, a nie tylko przeczytać przed nimi ostrzeżenie.

## Mapa błędnych przekonań

| Błędne przekonanie | Gdzie się ujawnia | Na co patrzeć |
| --- | --- | --- |
| „Agent to po prostu chatbot z promptem.” | `model_only` vs `scripted_pipeline` vs `capstone_agent` w `examples/compare_architectures/clear_bounded_review/` | to samo zadanie, radykalnie inna struktura sterowania i wyniki |
| „Każde użycie narzędzia czyni system agentowym.” | `scripted_pipeline` vs `capstone_agent` | oba używają narzędzi, ale tylko jeden używa weryfikacji jako wejścia do sterowania |
| „Okno kontekstu = pamięć.” | `tool_rich_memoryless` vs `capstone_agent` | oba czytają artykuły, ale tylko jeden utrzymuje materiał w pamięci do syntezy |
| „Więcej pamięci jest zawsze lepsze.” | `examples/run_review/capstone_stale_memory_harms/` i `data/requests/stale_memory_harms.txt` | nieaktualna pamięć staje się jawnym blokerem |
| „Planowanie jest zawsze lepsze niż bezpośrednie generowanie.” | `data/requests/over_planning_overhead.txt` i `tests/test_comparison.py` | repozytorium może rekomendować `scripted_pipeline` przy małym zadaniu |
| „Refleksja automatycznie poprawia poprawność.” | `src/m2a/feedback.py`, `tests/test_feedback.py` | działania refleksyjne są emitowane tylko wtedy, gdy istnieją blokery |
| „Udane wywołanie narzędzia oznacza, że zadanie się udało.” | `data/requests/tool_success_not_task_success.txt` i artefakty `verification.jsonl` | sukces wyszukiwania/czytania nie omija końcowej weryfikacji |
| „Zatrzymanie i przekazanie to sprawy tylko produkcyjne.” | `examples/run_review/capstone_ambiguous_request/`, `examples/compare_architectures/boundary_handoff/` | doprecyzowanie i noty graniczne są poprawnymi ograniczonymi wynikami |
| „Najpierw trzeba znać RL albo planowanie symboliczne.” | `docs/deferred-topics-and-boundaries.md` | repozytorium pozostaje w zakresie architektonicznym i mówi to wprost |

## Kategorie strukturalnych porażek

Workflow porównawczy diagnozuje porażki przez strukturę, a nie przez benchmark score.

Kategorie to:

- `goal`
- `planning`
- `memory`
- `grounding`
- `action`
- `stop`

Te etykiety pochodzą z `src/m2a/feedback.py` i są emitowane do wyników porównania.

## Dlaczego to ma znaczenie dydaktyczne

Osoba kończąca pracę z tym repozytorium powinna umieć przeczytać opis nieznanego systemu i odtworzyć:

- reprezentację celu,
- pętlę,
- podział między stanem a pamięcią,
- interfejsy narzędzi,
- sygnały weryfikacyjne,
- logikę zatrzymania lub przekazania.

To wymaga jawnych trybów awarii, a nie tylko demonstracji ścieżki szczęśliwej.
