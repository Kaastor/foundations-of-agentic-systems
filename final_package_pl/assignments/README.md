# Pakiet zadań

Ten plik wyjaśnia wyłącznie:

- model zadań,
- co oddają studenci,
- jak zorganizowane są foldery z zadaniami.

W sprawie terminów i workflow repozytorium użyj logistyki przekazanej podczas `Lesson 0` i na `Teams`.
W sprawie konfiguracji i rerunów użyj [STUDENT_SETUP.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/STUDENT_SETUP.md).

## Model zadań

Kurs używa modelu raportowego dostosowanego do epoki AI:

- użycie chatbotów jest normalne,
- użycie coding agentów jest mile widziane, ale niewymagane,
- oddawane prace mają formę raportów,
- ocenianie opiera się na dowodach, porównaniu, krytyce, ograniczonej rewizji i uzasadnieniu.

## Co oddają studenci

Do każdego zadania oddajesz jeden plik:

- `submission.md`

Używaj lokalnego `report_template.md`.

Każde zadanie zawiera jedną małą sekcję `Implementation Lens`.
Zadania 5-6 wymagają też jednej ograniczonej zmiany kodu i porównania `before/after`.

## Jak korzystać z tego pakietu

Zacznij od [shared_submission_rules.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/assignments/shared_submission_rules.md), a potem przejdź do folderu z aktualnym zadaniem.

Każdy folder zadania zawiera:

- `description.md`
- `report_template.md`
- `book_context.md`
- `code_context.md`
- `ai_use_guidance.md`
- `teacher_notes.md`

Jest też jeden nieoceniany dokument wdrożeniowy:

- [lesson_0.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/assignments/lesson_0.md)

## Mapa zadań

| Zadanie | Meeting | Godziny | Poziom kodu | Główna rodzina artefaktów |
| --- | --- | ---: | --- | --- |
| Agentic Classification Report | 1 | 4 | ograniczone czytanie kodu / opcjonalny rerun | porównanie architektur |
| Task Specification Audit | 2 | 4 | ograniczone czytanie kodu / opcjonalny rerun | artefakty spec review |
| Trace Localization Report | 3 | 4 | ograniczone czytanie kodu / opcjonalny rerun | trace + snapshoty stanu |
| Grounding Evidence Audit | 4 | 4 | ograniczone czytanie kodu / opcjonalny rerun | obserwacje narzędzi + weryfikacja |
| Memory Policy Intervention Report | 5 | 4 | ograniczona zmiana kodu + rerun | logi pamięci + weryfikacja + artefakty planu |
| Architecture Boundary Stress Test | 6 | 4 | ograniczona zmiana kodu + rerun | artefakty porównawcze + granice |

## Foldery z zadaniami

- [assignment_01_agentic_classification](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/assignments/assignment_01_agentic_classification)
- [assignment_02_task_spec_audit](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/assignments/assignment_02_task_spec_audit)
- [assignment_03_trace_localization](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/assignments/assignment_03_trace_localization)
- [assignment_04_grounding_evidence_audit](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/assignments/assignment_04_grounding_evidence_audit)
- [assignment_05_memory_planning_tradeoff](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/assignments/assignment_05_memory_planning_tradeoff)
- [assignment_06_architecture_recommendation](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/assignments/assignment_06_architecture_recommendation)
