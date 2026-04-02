# Przegląd literatury: clear_bounded_review

Wariant: `memory_rich_tool_poor`

## Zakres

Przygotuj przyjazny dla początkujących przegląd literatury o planowaniu, pamięci i groundingu w offline’owych asystentach do przeglądu literatury. Użyj tylko lokalnego korpusu. Porównaj lekkie planowanie z bardziej jawnymi wyborami architektonicznymi. Zacytuj 4 lokalne prace i zatrzymaj się dopiero wtedy, gdy każdy wymagany temat jest pokryty dowodami.

## Ustalenia według tematów

### Pamięć

Systemy bogate w narzędzia, ale bez pamięci, znajdują świeże dowody, lecz często gubią wcześniejsze wsparcie podczas syntezy. [P10-ToolRichNoMemory]

### Grounding

Interfejsy narzędzi zmieniają zarówno zdolność systemu, jak i to, jakie dowody mogą ugruntować końcowy przegląd. [P05-InterfaceGrounding]

### Planowanie

Systemy bogate w narzędzia, ale bez pamięci, znajdują świeże dowody, lecz często gubią wcześniejsze wsparcie podczas syntezy. [P10-ToolRichNoMemory]

## Porównanie

`Goal Contracts for Bounded Literature Review Assistants` podkreśla cele i zatrzymanie, a `Tool-Rich, Memoryless Review Systems` podkreśla narzędzia i pamięć. Wybór architektury zależy więc od tego, czy wąskim gardłem zadania jest dostęp do dowodów, retencja czy dyscyplina sterowania. [P02-GoalContract] [P10-ToolRichNoMemory]

## Użycie pamięci

- Użyto świeżej pamięci epizodycznej `M04-tool-interfaces` powiązanej z P05-InterfaceGrounding i P10-ToolRichNoMemory.
- Użyto świeżej notatki `note-9-7` powiązanej z P10-ToolRichNoMemory.

## Cytowania

- [P02-GoalContract] Goal Contracts for Bounded Literature Review Assistants (2024)
- [P05-InterfaceGrounding] Interface Contracts and Evidence Linking for Local Research Tools (2024)
- [P08-BoundedStop] BoundedStop: Clarification and Handoff as Correct Agent Outcomes (2024)
- [P10-ToolRichNoMemory] Tool-Rich, Memoryless Review Systems (2024)
