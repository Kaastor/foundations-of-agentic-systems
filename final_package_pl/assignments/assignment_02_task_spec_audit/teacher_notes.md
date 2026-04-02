# Notatki dla prowadzącego

## Po co jest to zadanie

To zadanie czyni kontrakt zadania widocznym, zanim studenci przejdą do śladów, narzędzi i pamięci.

## Co powinien zawierać mocny raport

- dwie naprawdę różne kandydackie wersje task spec,
- porównanie oparte na dowodach z zapisanymi artefaktami,
- poprawiony, końcowy kontrakt zadania, który zachowuje niejednoznaczność jako jawną,
- krótki `Implementation Lens`, łączący wymagane pola z `build_task_spec` albo `TaskSpec.validate()`,
- realne omówienie warunków `stop` albo `handoff`.

## Typowe słabe wzorce

- traktowanie parafrazy prośby jako task spec,
- zgadywanie intencji użytkownika zamiast oznaczenia niejednoznaczności,
- zapominanie o warunkach zatrzymania.

## Niuanse oceniania

Student nie musi odtworzyć dokładnie tej samej specyfikacji co artefakt referencyjny.
Musi jednak zaproponować wersję, która jest w obroniony sposób bardziej gotowa do sterowania niż ogólna prośba.
`Implementation Lens` powinien wyjaśniać, dlaczego pola mają znaczenie, a nie streszczać cały moduł.
