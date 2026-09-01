# Plan 8h: Od Wyniku Referencyjnego Do Własnego Pipeline'u

Moduł zajmuje cztery bloki po 2 godziny. Uczestnicy widzieli już kodowanie w
chacie i MAXQDA, dlatego nie powtarzają całej analizy. Projektują podstawowy
proces na ograniczonym pakiecie fragmentów z `PREWORK_01-03` i porównują jego
strukturę z wynikiem pełnego korpusu.

Przed tymi ośmioma godzinami odbywa się osobny, zalecany **moduł zerowy 2,5 h**
z GitHuba, Colaba i pierwszego vibe codingu z Gemini. Jego plan znajduje się w
[`00_github_colab/plan_modulu.md`](../00_github_colab/plan_modulu.md). Dzięki
temu Blok 1 nie traci czasu na zakładanie kont, wyjaśnianie runtime'u ani
pierwszy commit.

Każdy blok przechodzi przez cykl: cel, pierwsza próba, krótka demonstracja,
zadanie, prezentacja, feedback, poprawa i transfer.

Warstwa implementacyjna ma zawsze tę samą kolejność: model kodowania i cel
etapu -> rozpoznanie potrzebnej procedury -> karta procedury badawczej ->
techniczny dodatek infrastruktury -> instrukcja do czatu Colaba -> jedna
mikrofunkcja -> czytelna checklista -> dwa porównania analityczne przez API ->
ogląd rekordów -> decyzja badacza. Uczestnik nie pisze parsera ani adaptera API
od zera i nie otrzymuje gotowej logiki tworzącej D/F/S/T.

Czat Colaba służy do tworzenia kodu. Adapter API służy wyłącznie do analizy
materiału i ma ten sam interfejs dla Gemini oraz OpenAI. Zmiana providera nie
jest zmianą pipeline'u badawczego.

## Miejsce W Turze

| Moment | Temat |
| --- | --- |
| Dzień 2, 09:00-11:00 | Vibe 1: rezultat docelowy, kontrakt i jednostki |
| Dzień 2, 11:30-13:30 | Vibe 2: selekcja relewancji i kody D |
| Dzień 2, 14:30-16:30 | Vibe 3: wzorce F i operacyjne karty S |
| Dzień 3, 09:00-11:00 | Vibe 4: T-S-F-D, statystyki, relacje i handoff |
| Dzień 3, 11:30-16:30 | AI Programming: lokalna walidacja, zmiana i Git |

## Blok 1: Zobacz Wynik, Potem Zaprojektuj Wejście

**Cel:** rozpoznać, że książka kodowa jest wynikiem kilku sprawdzalnych
transformacji, a nie jedną odpowiedzią LLM.

| Czas | Działanie | Wynik |
| --- | --- | --- |
| 0-20 min | Prowadzący przechodzi przez `reference_results/README.md`: skalę, jedną gałąź T-S-F-D, kartę S i graf F-F/T-T. | Wspólny obraz rezultatu bez czytania pełnej dokumentacji. |
| 20-35 min | Pary rozpisują wstecz, jakie wejścia i decyzje były potrzebne do powstania pokazanej gałęzi. | Szkic pipeline'u i punkty kontroli człowieka. |
| 35-50 min | Demonstracja `io_contract.md`: tabela jest umową między krokami. | Lista pól potrzebnych do traceability. |
| 50-70 min | Notebook 1: uczestnicy oglądają ograniczony rejestr rzeczywistych fragmentów i rozróżniają jednostkę kontekstu, relewancji i przypisania. | Rozpoznana potrzeba procedury jednostkowania. |
| 70-90 min | Karta procedury oraz `check_unit_register`: uczestnik przekazuje instrukcję do czatu Colaba, wkleja jedną funkcję i uruchamia checklistę. | Karta, mikrofunkcja i nazwane ograniczenie. |
| 90-110 min | Porównanie przez API polityki „zdanie” z „tura jako kontekst + fragment dowodowy”. | Decyzja o jednostce oparta na skutkach dla kodowania. |
| 110-120 min | Inspekcja rekordów, publikacja punktu kontrolnego i zapis handoffu. | `01_unit_register.csv`, karta procedury i decyzja badacza w prywatnym repo. |

**Warunek odbioru:** `text_unit_id` jest niepusty i unikalny, liczba oraz tekst
fragmentów nie zmieniają się, a uczestnik potrafi wyjaśnić, jaki kontekst
zachowa przy późniejszym przypisaniu kodu.

## Blok 2: Najpierw Relewancja, Potem Kod D

**Cel:** zakodować tylko fragmenty związane z doświadczeniami prekaryjnymi i
zachować dokładny ślad dowodowy.

| Czas | Działanie | Wynik |
| --- | --- | --- |
| 0-15 min | Pary kodują ręcznie dwie tury: jedna może dostać kilka D, druga żadnego. | Kryteria `precarity_relevant/not_relevant/needs_review`. |
| 15-30 min | Demonstracja różnicy między jednostką, fragmentem dowodowym, przypisaniem i unikalnym kodem. | Poprawny model tabel. |
| 30-50 min | Notebook 2: pytanie, soczewka i karta procedury relewancji oraz D. | Jawny model decyzji przed wywołaniem API. |
| 50-65 min | Czat Colaba tworzy `check_d_assignments`; uczestnik wkleja jedną funkcję do notebooka. | Kontrola techniczna gotowa przed analizą korpusu. |
| 65-90 min | Adapter API porównuje prompt ogólny i kontraktowy przy tym samym modelu oraz materiale. | Dwie odpowiedzi i zapisane przewidywanie. |
| 90-110 min | Powrót do cytatów; uczestnicy zapisują cztery własne decyzje D albo `needs_review`. | Kandydacka tabela przypisań kod–fragment. |
| 110-115 min | `check_d_assignments` kontroluje ID, dosłowność cytatu i statusy, ale nie trafność kodu. | Checklista i poprawiona karta procedury. |
| 115-120 min | Zapis artefaktów, handoff i punkt kontrolny GitHub. | `02_d_assignments.csv` oraz decyzje promptowe w prywatnym repo; pełny log API lokalnie. |

**Warunek odbioru:** D jest krótką procesualną parafrazą bez osobnej definicji;
każde przypisanie wskazuje dokładny fragment, a nie każda jednostka ma kod.

## Blok 3: Od D Do Wzorca F

**Cel:** rozdzielić dwa kroki abstrakcji: odkrycie wzorca F i zbudowanie
używalnej przez drugiego kodera karty S.

| Czas | Działanie | Wynik |
| --- | --- | --- |
| 0-20 min | Pary porównują 8-12 profili D i wskazują, które łączy mechanizm, a które tylko słownictwo. | Pierwsze F i kody pozostawione bez przypisania. |
| 20-35 min | Demonstracja pytania F: „co widzimy ponad pojedyncze D?”. | Kryterium zysku analitycznego. |
| 35-50 min | Notebook 3: karta procedury F i jawne kryterium wspólnego mechanizmu. | Kryterium zysku analitycznego i granicy. |
| 50-65 min | Czat Colaba tworzy `find_unmapped_d`; uczestnik wkleja jedną funkcję. | Kontrola kompletności gotowa przed grupowaniem. |
| 65-90 min | Adapter API porównuje podobieństwo nazw z kontraktem wymagającym mechanizmu, granicy i przypadku negatywnego. | Dwie konkurencyjne propozycje grupowania. |
| 90-110 min | Pary wracają do cytatów i zapisują split/merge/review oraz mapowanie D–F. | Kandydackie F i jawne decyzje mapowania. |
| 110-115 min | `find_unmapped_d` wskazuje D bez jednej decyzji, ale nie wymusza F. | Lista braków proceduralnych, nie ranking kategorii. |
| 115-120 min | Zapis artefaktów, handoff i punkt kontrolny GitHub. | `03_focused_categories.csv` i `03_d_to_f.csv` w prywatnym repo. |

**Warunek odbioru:** podobieństwo wybiera materiał do porównania, ale nie
rozstrzyga grupowania. Każdy D ma jedną kandydacką F albo jawną decyzję
`needs_review`.

## Blok 4: Złóż Książkę I Przygotuj Handoff

**Cel:** domknąć hierarchię, porównać sample z full i przygotować repo do
lokalnej pracy z Codexem.

| Czas | Działanie | Wynik |
| --- | --- | --- |
| 0-20 min | Notebook 4: z kilku zgodnych F uczestnicy określają potrzebę operacyjnej S i rolę oszczędnego T. | Karta procedury operacjonalizacji. |
| 20-35 min | Czat Colaba tworzy `check_codebook_hierarchy`; uczestnik wkleja jedną funkcję. | Kontrola hierarchii gotowa przed syntezą. |
| 35-60 min | Adapter API porównuje ogólną syntezę z promptem wymagającym definicji, włączenia, wyłączenia, granicy i kontrprzykładu. | Dwie odpowiedzi i decyzja, czego nie scalać. |
| 60-80 min | Uczestnicy zapisują jedną kandydacką S i T; infrastruktura składa jawne T–S–F–D. | Kandydacka książka bez statusu `accepted`. |
| 80-90 min | `check_codebook_hierarchy` kontroluje rodziców, duplikaty i pola S. | Checklista i ograniczenie walidatora. |
| 90-100 min | Porównanie ćwiczenia z wynikiem full: skala, pokrycie i elementy widoczne dopiero w całym korpusie. | Nota o wpływie skali bez kopiowania kodów. |
| 100-110 min | Prowadzący korzysta z [noty o architekturze skali](notatka_dla_prowadzacego_skalowanie.md): embeddingi, cache, Flex, asynchroniczność i checkpointy jako opcje inżynieryjne. | Rozróżnienie metodologii od optymalizacji wykonania. |
| 110-115 min | Uzupełnienie handoffu i briefu adaptacji: kruche miejsce, jedna walidacja i jedna zmiana. | Gotowe przekazanie do Codexa. |
| 115-120 min | Publikacja sprawdzonych artefaktów i handoffu; pełne logi API pozostają ignorowane. | Prywatne repo gotowe do lokalnego klonu i pracy z Codexem. |

**Warunek odbioru:** S mają kompletne karty, hierarchia nie ma brakujących
rodziców ani cykli, a status `accepted` nie jest nadawany automatycznie.

## Granica Materiału Uczestnika

Uczestnik dostaje cztery notebooki proceduralne, ograniczony pakiet
rzeczywistych fragmentów, neutralny adapter analityczny Gemini/OpenAI i
zaakceptowane wyniki full.
Nie dostaje kompletnego runnera tworzącego D/F/S/T, dostrojonych promptów,
retrievalu embeddingowego, harmonizacji między batchami, cache, checkpointów,
autorskich walidatorów jakości ani generatora grafu relacji.
