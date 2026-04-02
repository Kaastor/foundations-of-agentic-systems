# Podstawy architektur systemów agentowych: od modeli generatywnych do systemów ukierunkowanych na cel

## Opis kursu

Ten pakiet wprowadza w sposób zorientowany na zrozumienie do ważnego i konkretnego obszaru współczesnej generatywnej AI: do architektonicznego przejścia od modelu generatywnego do ograniczonego, ukierunkowanego na cel systemu agentowego.

Nie jest to ogólne wprowadzenie do całej GenAI. Zakres jest celowo węższy i bardziej precyzyjny. Pakiet koncentruje się na architekturach agentowych: jawnych celach, pętlach sterowania, stanie, pamięci, planowaniu, użyciu narzędzi, weryfikacji, warunkach zatrzymania, logice przekazania oraz porównywaniu architektur.

Centralne pytanie kursu brzmi:

> Jak model generatywny staje się poprzez architekturę ograniczonym, ukierunkowanym na cel systemem agentowym?

## Od czego zacząć

Jeśli jesteś studentem lub studentką, zacznij w tej kolejności:

1. [STUDENT_SETUP.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/STUDENT_SETUP.md)
2. [assignments/README.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/assignments/README.md)
3. [book.pdf](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/book/book.pdf)
   Rozdział 1, s. 7-15

Jeśli prowadzisz kurs, zacznij w tej kolejności:

1. [lesson_0.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/assignments/lesson_0.md)
2. [TEACHER_GUIDE.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/TEACHER_GUIDE.md)
3. [meeting_plan.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/meeting_plan.md)
4. [meeting_prep_checklist.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/meeting_prep_checklist.md)

## Rola poszczególnych dokumentów

Korzystaj z dokumentów z jasnym podziałem ról:

- [README.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/README.md): o czym jest kurs, po co istnieje i jak zbudowany jest pakiet
- [STUDENT_SETUP.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/STUDENT_SETUP.md): konfiguracja lokalna i uruchamianie repozytorium
- [assignments/README.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/assignments/README.md): model zadań i mapa folderów z zadaniami
- [meeting_plan.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/meeting_plan.md): szkielet kursu i logika spotkań
- [TEACHER_GUIDE.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/TEACHER_GUIDE.md): model pracy prowadzącego i próg wejścia przed kursem
- [lesson_0.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/assignments/lesson_0.md): wspólny plik wiedzy do `Lesson 0`, z treścią pojęciową i lokalnymi danymi instancji kursu

## Dla kogo jest ten kurs

Ten kurs jest przeznaczony dla:

- studentów, którzy chcą zbudować rygorystyczne podstawy pojęciowe przed specjalizacją,
- samodzielnych uczących się, którym zależy na zrozumieniu struktury zamiast na receptach frameworkowych,
- inżynierów i osób technicznych, które potrzebują jasnego obrazu tego, jak złożone są systemy agentowe,
- początkujących badaczy szukających ograniczonego i inspekcyjnego wejścia w temat architektur agentowych.

Kurs zakłada swobodę w pracy z abstrakcją, rozumowaniem krok po kroku i podstawowym myśleniem obliczeniowym. Doświadczenie z reinforcement learning, information retrieval, planowaniem symbolicznym czy systemami produkcyjnymi nie jest wymagane. Podstawowa znajomość programowania jest pomocna, ale niekonieczna dla części czysto koncepcyjnej.

## Cel dydaktyczny

Celem pakietu jest rozwinięcie strukturalnej biegłości w rozumieniu systemów agentowych. Po ukończeniu kursu student powinien umieć opisać nieznany system przez pryzmat:

- reprezentacji zadania,
- struktury sterowania,
- zarządzania stanem,
- polityki pamięci,
- interfejsów narzędziowych,
- logiki weryfikacji,
- warunków zatrzymania i przekazania.

Pakiet kładzie nacisk na:

- jawne rozróżnienia architektoniczne zamiast mglistych etykiet „agentowych”,
- artefakty i ślady możliwe do prześledzenia zamiast nieprzejrzystych demonstracji,
- deterministyczne, offline’owe przepływy pracy zamiast ukrytych zachowań modelu,
- ograniczone rozumowanie o projektowaniu systemów zamiast szerokich deklaracji o całej GenAI.

## Efekty uczenia się

Po ukończeniu kursu student powinien umieć:

- wyjaśnić różnicę między odpowiedzią model-only, skryptowym przepływem pracy i pętlą agentową,
- przekształcić nieprecyzyjną prośbę w jawną specyfikację zadania z ograniczeniami, kryteriami sukcesu i warunkami zatrzymania,
- odróżnić kontekst, stan zewnętrzny, trwałą pamięć, obserwacje i ślady wykonania,
- wyjaśnić pamięć jako reprezentację plus politykę, a nie jako ogólny magazyn danych,
- analizować użycie narzędzi jako kontrakt ze środowiskiem, a nie jako ozdobny dodatek,
- rozumować o planowaniu, dekompozycji, przeplanowywaniu i wyborze działań w ograniczonych systemach,
- połączyć weryfikację i informację zwrotną z dalszymi decyzjami sterującymi,
- traktować doprecyzowanie, zatrzymanie i przekazanie jako elementy poprawności,
- porównywać alternatywne architektury na tym samym zadaniu i uzasadniać, która z nich jest lepiej dopasowana.

## Przykład przewodni

Cały pakiet jest osadzony w jednym ograniczonym przykładzie przewodnim: w offline’owym asystencie do przeglądu literatury.

To celowe ograniczenie. Przykład jest wystarczająco bogaty, żeby odsłonić rdzeń architektury agentowej, a jednocześnie na tyle mały, żeby pozostać deterministyczny, inspekcyjny i dydaktycznie przejrzysty. Celem nie jest zbudowanie produkcyjnego asystenta badawczego, lecz uczynienie architektury widoczną.

## Zakres i celowe wyłączenia

Ten kurs nie dotyczy przede wszystkim:

- API dostawców i orkiestracji specyficznej dla frameworków,
- prompt engineering rozumianego jako zbiór trików,
- żywego pobierania z sieci lub produkcyjnych systemów RAG,
- wewnętrznych mechanizmów retrievalu i algorytmów rankingowych,
- sterowania opartego na reinforcement learning,
- formalnych frameworków planowania symbolicznego,
- wdrożenia, obserwowalności, governance ani operacji produkcyjnych.

To ważne obszary, ale w tym pakiecie pozostają tematami sąsiednimi, a nie osią nauczania.

## Dlaczego to jest dobra baza

Ten kurs stanowi mocny fundament dla kilku dalszych ścieżek uczenia się i praktyki. W szczególności przygotowuje do:

- dalszej nauki agent engineering, zwłaszcza tam, gdzie trzeba koordynować cele, narzędzia, pamięć i weryfikację,
- bardziej zaawansowanej pracy nad niezawodnymi systemami używającymi narzędzi, w tym asystentami opartymi na źródłach i przepływami retrieval-augmented,
- kolejnych kursów z planowania, sekwencyjnego podejmowania decyzji lub reinforcement learning, gdzie struktura sterowania staje się bardziej formalna,
- nauki o ewaluacji i niezawodności w systemach GenAI, zwłaszcza tam, gdzie trzeba rozróżniać proces i wynik,
- pracy nad interakcją człowiek-agent, systemami mixed-initiative i projektowaniem delegowania,
- ścieżek badawczych lub inżynierskich dotyczących pamięci, reprezentacji, world models i długiego horyzontu zachowania systemu.

Wartość tego kursu jako fundamentu polega na tym, że uczy słownictwa architektonicznego i rozróżnień pojęciowych, które powracają w wielu podobszarach nowoczesnych systemów GenAI.

## Struktura pakietu

Pakiet zawiera dwa uzupełniające się komponenty:

- `book/` zawiera materiały koncepcyjne do czytania,
- `code/` zawiera deterministyczne repozytorium dydaktyczne, w którym koncepcje stają się konkretne.

Zawiera również warstwę organizacji kursu:

- [meeting_plan.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/meeting_plan.md) z sześciospotkaniowym szkieletem kursu,
- [TEACHER_GUIDE.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/TEACHER_GUIDE.md) do przygotowania prowadzącego,
- [meeting_prep_checklist.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/meeting_prep_checklist.md) do przygotowania każdego spotkania,
- [STUDENT_SETUP.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/STUDENT_SETUP.md) z konfiguracją środowiska i pracą lokalną,
- [assignments](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package_pl/assignments) z zadaniami, zasadami oddawania prac i materiałami do Lesson 0.

W katalogu `code/` studenci znajdą:

- `src/` z implementacją,
- `docs/` z wyjaśnieniami specyficznymi dla repozytorium i dokumentami przekrojowymi,
- `examples/` z zapisanymi artefaktami referencyjnymi,
- `data/` z lokalnymi fixture’ami i syntetycznym korpusem,
- `tests/` z testami zachowania i regresjami.

## Co wyróżnia ten pakiet

Pakiet jest zorganizowany wokół kilku jawnych zobowiązań dydaktycznych:

- deterministyczne zachowanie zamiast ukrytych wywołań modeli zewnętrznych,
- wyniki możliwe do prześledzenia zamiast impresyjnych demonstracji,
- ograniczony zakres zamiast niezróżnicowanego wprowadzenia do całej GenAI,
- porównywanie architektur zamiast promowania jednego wzorca,
- przenaszalne rozumienie pojęciowe zamiast szkolenia narzędziowego zależnego od jednego dostawcy.

## Oczekiwany rezultat

Osoby, które ukończą ten pakiet, powinny zdobyć więcej niż znajomość słownictwa agentowego. Powinny umieć odtworzyć architekturę nieznanego systemu, wyjaśnić, dlaczego zachowuje się w określony sposób, wskazać prawdopodobne strukturalne punkty awarii i rozumować o tym, kiedy jedna architektura jest bardziej odpowiednia od innej.

Podstawowym rezultatem edukacyjnym jest więc strukturalna biegłość w rozumieniu systemów agentowych.
