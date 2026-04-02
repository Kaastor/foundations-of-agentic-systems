# Zadanie 5: raport interwencji w politykę pamięci

**Powiązane spotkanie:** [meeting_plan.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/meeting_plan.md)  
Spotkanie 5: „Co powinno się utrwalać i kiedy planowanie pomaga?”

**Po co istnieje to zadanie:** Studenci mają rozumieć pamięć i planowanie jako selektywne wybory sterujące, a nie jako domyślne ulepszenia.

**Główny akcent pętli rozumowania:** `wygeneruj -> porównaj -> skrytykuj -> popraw -> uzasadnij`

**Oczekiwany czas:** `4 godziny`

**Poziom kodowania:** `jedna ograniczona zmiana kodu plus rerun`

## Zadanie

Użyj przypadku starej pamięci, aby odpowiedzieć na pytanie:

`Co się dzieje, gdy poluzujesz politykę obsługi starej pamięci w capstone agencie, i czego wynikowe zachowanie uczy o projektowaniu ograniczonej pamięci?`

W swojej kopii roboczej repozytorium wykonaj dokładnie tę ograniczoną interwencję w [control.py](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/code/src/m2a/control.py):

- dla `capstone_agent` zmień `stale_after_steps=5` na `stale_after_steps=1`,
- dla `capstone_agent` zmień `allow_stale_recall=False` na `allow_stale_recall=True`.

Następnie:

1. uruchom workflow starej pamięci raz przed zmianą,
2. wprowadź zmianę,
3. uruchom ten sam workflow jeszcze raz,
4. porównaj artefakty `before` i `after`,
5. oceń, czy interwencja poprawiła, pogorszyła czy tylko słabo zmieniła ograniczone zachowanie.

Raport końcowy powinien wyjaśnić, co zmieniło się w dowodach pamięciowych i co to ujawnia o polityce pamięci. Powinieneś też powiedzieć, czy samo planowanie wystarczyłoby do rozwiązania zaobserwowanego problemu.

## Checklista oddania

- zapisz przewidywany efekt przed zmianą kodu,
- uruchom i przywołaj zestaw artefaktów `before` i `after`,
- wykonaj dokładnie wskazaną zmianę w `control.py`,
- porównaj co najmniej `memory_log.jsonl`, `verification.jsonl` i `stop_decision.json`,
- obejrzyj co najmniej jeden nazwany moduł źródłowy i wyjaśnij, jaki kompromis polityki pamięci koduje,
- oceń, czy interwencja poprawiła, pogorszyła czy tylko słabo zmieniła ograniczone zachowanie,
- wyjaśnij jedno pozostałe ryzyko.
