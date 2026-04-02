# Szablon raportu

## 1. Task

Podaj dwa pytania rekomendacyjne:

- dla przypadku w zakresie,
- dla przypadku granicznego.

## 2. Candidate Options Or Initial Answer

Podaj:

- swój początkowy zestaw rekomendacji przed zmianą kodu,
- co najmniej jedną sensowną alternatywę albo kontrprognozę dla testu granicznego.

## 3. Comparison Criteria

Użyj kryteriów takich jak:

- dopasowanie do zadania,
- jakość materiału źródłowego,
- ograniczona autonomia,
- jakość zatrzymania albo przekazania,
- ryzyko porażki.

## 4. Before Evidence

Przywołaj:

- zapisane albo lokalne dowody `before` dla przypadku w zakresie,
- plik `fit_recommendation.md` dla przypadku granicznego przed zmianą,
- jeden artefakt graniczny albo przekazania, np. `boundary_note.md` albo `failure_diagnosis.md`.

## 5. Intervention And Implementation Lens

Obejrzyj:

- [comparison.py](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/code/src/m2a/comparison.py)
- [feedback.py](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/code/src/m2a/feedback.py)

Zapisz:

- dokładny plik, który zmieniłeś,
- dokładną ograniczoną zmianę,
- przewidywany efekt przed rerunem.

Następnie wyjaśnij w 3-5 zdaniach, po co istnieje pierwotna gałąź graniczna i co powinno testować jej wyłączenie.

## 6. After Evidence And Critique

Przywołaj:

- plik `fit_recommendation.md` dla przypadku granicznego po zmianie,
- jeden zmieniony albo niezmieniony artefakt wspierający, np. `boundary_note.md` albo `comparison_matrix.md`.

Następnie wyjaśnij:

- co zmieniło się w obciążonej rekomendacji,
- czy zmodyfikowane zachowanie jest bardziej czy mniej ograniczone,
- co to ujawnia o logice rekomendacji vs rzeczywistych granicach systemu.

## 7. Revision Or Selected Option

Przedstaw:

- swoją końcową rekomendację dla przypadku w zakresie,
- końcowy osąd dla przypadku granicznego,
- decyzję, czy patch testu obciążeniowego należy odrzucić czy zachować.

## 8. Final Justification

Obroń obie rekomendacje i wyjaśnij, gdzie system powinien się zatrzymać albo przekazać sprawę dalej, zwłaszcza po obejrzeniu obciążonej rekomendacji granicznej.

## 9. Uncertainty Or Remaining Weakness

Nazwij jedno otwarte ryzyko albo nierozstrzygnięty punkt porównania.
