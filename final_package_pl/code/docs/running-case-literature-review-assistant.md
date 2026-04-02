# Przykład przewodni: asystent do przeglądu literatury

Całe repozytorium jest zakotwiczone w jednym ograniczonym zastosowaniu: w offline’owym asystencie do przeglądu literatury opartym na małym lokalnym korpusie.

To wybór celowy. Jest wystarczająco duży, żeby odsłonić cele, stan, pamięć, planowanie, narzędzia, weryfikację oraz zatrzymanie lub przekazanie. Jest wystarczająco mały, żeby pozostać deterministyczny i możliwy do zbadania.

## Czym jest środowisko

„Środowisko” nie jest tutaj siecią. To dostarczony korpus w `data/corpus/papers.jsonl` plus cztery lokalne narzędzia:

- `search_corpus`
- `read_paper`
- `write_note`
- `assemble_citations`

To wystarcza, żeby uczynić semantykę narzędzi konkretną bez wprowadzania infrastruktury retrievalowej albo API dostawców.

## Co asystent ma zrobić

W różnych fixture’ach asystent musi:

- przekształcić surową prośbę w ograniczoną specyfikację zadania,
- zebrać materiał z korpusu,
- zsyntetyzować przegląd z cytowaniami albo zwrócić wynik typu doprecyzowanie/przekazanie,
- porównać architektury, gdy workflow tego wymaga.

Fixture’y próśb są celowo zróżnicowane:

| Fixture | Po co istnieje |
| --- | --- |
| `clear_bounded_review.txt` | kanoniczny przypadek porównawczy mieszczący się w zakresie |
| `ambiguous_request.txt` | wymusza doprecyzowanie zamiast cichego zgadywania |
| `tradeoff_memory_vs_tools.txt` | uwidacznia kanoniczną parę kompromisową |
| `tool_success_not_task_success.txt` | pokazuje, że udane wyszukiwanie nie oznacza sukcesu zadania |
| `over_planning_overhead.txt` | pokazuje, że mniejsze zadania mogą faworyzować prostsze architektury |
| `stale_memory_harms.txt` | pokazuje, że nieaktualne przywołanie z pamięci może stać się blokerem |
| `boundary_handoff.txt` | wymusza jawną notę graniczną |

## Dlaczego ten przypadek dobrze uczy architektury agentowej

Przegląd literatury jest dobrym przykładem dydaktycznym, bo sukces zależy od czegoś więcej niż płynny tekst.

Udany przebieg wymaga:

- jawnego kontraktu zadania,
- zbierania materiału źródłowego,
- śledzenia stanu przez wiele kroków,
- opcjonalnej pamięci dla zachowania ciągłości,
- logiki planowania albo selekcji,
- weryfikacji sprawdzającej *przegląd*, a nie samo wywołanie narzędzia,
- zdolności do zatrzymania się, doprecyzowania albo przekazania sprawy.

To mapuje się bezpośrednio na głęboki rdzeń tej ścieżki.

## Czego ten przypadek uczy poprawnie

- `Nawyk zbliżony do produkcji`: udany przegląd zależy od jawnych celów, ugruntowanego materiału źródłowego, weryfikacji i ograniczonej logiki zatrzymania, a nie tylko od płynnego tekstu.
- `Nawyk zbliżony do produkcji`: wyniki narzędzi mają znaczenie, bo dostarczają obserwacji możliwych do inspekcji, z których później korzysta weryfikacja i synteza.
- `Nawyk zbliżony do produkcji`: to samo zadanie może uzasadniać różne architektury w zależności od skali zadania, niejednoznaczności, potrzeb pamięci i wymagań dowodowych.

## Co ten przypadek celowo przycina

- `Uproszczenie dydaktyczne`: korpus jest syntetyczny i stały.
- `Uproszczenie dydaktyczne`: wyszukiwanie jest lokalne i leksykalne, a nie oparte na pełnym stosie retrievalowym.
- `Uproszczenie dydaktyczne`: doprecyzowanie jest emitowane jako artefakt zamiast zachodzić w interaktywnej pętli z użytkownikiem.
- `Uproszczenie dydaktyczne`: zachowanie „modelu” jest deterministyczne, tak aby dało się odizolować efekty architektury.

`Warto przenieść`: potrzebę jawnych kontraktów zadania, narzędzi niosących materiał źródłowy i ograniczonego sterowania.

`Nie uogólniaj nadmiernie`: dokładnego kształtu korpusu, mechanizmu wyszukiwania i deterministycznej symulacji.

## Projekt korpusu

Korpus jest syntetyczny i uproszczony z założenia. Każda karta artykułu zawiera:

- identyfikator cytowania,
- tytuł i rok,
- abstrakt,
- słowa kluczowe,
- kanoniczne tagi tematyczne,
- jedno lub więcej ustaleń,
- ograniczenia.

Artykuły nie są tu po to, by uczyć retrievalu literatury. Są po to, by uczyć, jak architektura zamienia materiał źródłowy w ograniczone zachowanie.

## Czego celowo tu nie ma

Brak:

- wyszukiwania w żywej sieci,
- infrastruktury rankingowej,
- embedding store’ów,
- benchmark harnesses,
- produkcyjnej obserwowalności,
- uczenia polityki.

To są realne tematy, ale przesunęłyby repozytorium poza centralne pytanie architektoniczne.
