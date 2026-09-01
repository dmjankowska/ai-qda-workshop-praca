# Kontrakt Wejść I Wyjść: Wersja Uczestnika

Każdy notebook realizuje jedną małą procedurę badawczą i zapisuje artefakt,
który można przekazać do kolejnego etapu. Kontrakt nie narzuca gotowej
implementacji: najpierw określasz sens procedury i decyzję badacza, a dopiero
potem prosisz model o krótką funkcję techniczną.

Zakres `sample` to ograniczony pakiet fragmentów z `PREWORK_01-03` oraz
kandydackie artefakty tworzone na warsztacie. Zakres `full` jest oddzielnym
wynikiem referencyjnym dla 32 wywiadów. Nie łącz ich rekordów.

## Etap 1: Od Transkrypcji Do Jednostek

**Cel:** zaprojektować jednostkę pracy, która zachowuje tekst, rozmówcę i
kontekst potrzebny do późniejszego kodowania.

**Wejście:** ograniczony pakiet fragmentów z `PREWORK_01-03`.

**Artefakt:** `01_unit_register.csv`.

**Minimalne pola:** `text_unit_id`, `case_id`, `source_file`, `sequence`,
`speaker`, `text`.

**Decyzja badacza:** czy jednostką analizy jest zdanie, tura czy fragment
wyznaczony inaczej oraz ile kontekstu trzeba zachować. Kontrola techniczna może
wykryć brak identyfikatora lub tekstu, ale nie rozstrzyga tej decyzji.

## Etap 2: Od Fragmentu Do Kandydata Kodu D

**Cel:** odróżnić ocenę relewancji od kodowania i związać kandydacki kod D z
dosłownym fragmentem materiału.

**Wejście:** `01_unit_register.csv` oraz soczewka kodowania.

**Artefakt:** `02_d_assignments.csv`.

**Minimalne pola:** `assignment_id`, `code_id`, `text_unit_id`, `source_file`,
`code_name`, `evidence_quote`, `memo`, `review_status`.

**Decyzja badacza:** co w świetle pytania badawczego jest relewantne, jak
blisko danych ma pozostać nazwa D i kiedy przykład wymaga przeglądu. AI nie
nadaje statusu `accepted`.

## Etap 3: Od Kodów D Do Wzorców F

**Cel:** sprawdzić, czy kilka kodów D opisuje wspólny mechanizm, a nie tylko
używa podobnych słów.

**Wejścia:** `02_d_assignments.csv` i przykłady użycia kodów D.

**Artefakty:** `03_focused_categories.csv` oraz `03_d_to_f.csv`.

**Minimalne pola F:** `focused_id`, `focused_name`, `analytic_rationale`,
`boundary`, `negative_case`, `review_status`.

**Decyzja badacza:** które D można roboczo połączyć, co wyznacza granicę F i
czy przypadek negatywny podważa proponowany wzorzec. Każdy D musi mieć rodzica
F albo jawny status `needs_review`.

## Etap 4: Od Wzorców Do Kandydackiej Książki T-S-F-D

**Cel:** zbudować audytowalną hierarchię kandydacką bez automatycznego
ogłaszania wyniku analizy.

**Wejścia:** kategorie F, mapowanie D-F oraz ślady dowodowe.

**Artefakty:** `04_candidate_codebook.csv` i `handoff_to_codex.md`.

**Minimalne pola:** `code_id`, `parent_code_id`, `code_name`, `code_level`,
`definition`, `inclusion_criteria`, `exclusion_criteria`, `example_quote`,
`text_unit_id`, `source_file`, `review_status`.

**Decyzja badacza:** czy karta S ma operacyjną definicję i granice, czy T
rzeczywiście określa zakres analityczny oraz które elementy wymagają dalszego
porównania z korpusem.

## Kontrole Między Etapami

- identyfikatory są unikalne, a wskazani rodzice istnieją;
- hierarchia nie ma cykli;
- żaden D, F ani S nie znika bez wpisu `needs_review`;
- cytat jest dosłownym fragmentem wskazanej jednostki;
- nie każda jednostka musi być relewantna lub zakodowana;
- poprawny format nie oznacza poprawnej interpretacji;
- AI nie nadaje statusu `accepted`.

## Rozwinięcie Do Pełnego Korpusu

Po warsztacie tę samą sekwencję procedur można uruchamiać na kolejnych
partiach korpusu, zachowując wersje kart, promptów, artefaktów i decyzji.
Batchowanie, embeddingi, cache, zadania w tle i checkpointy mogą usprawnić
wykonanie na większej skali, ale nie zastępują decyzji o relewancji, kodzie,
kategorii ani zakresie teoretycznym.

[`../01_data/codebook/`](../01_data/codebook/) pokazuje rezultat `full` do
oglądania i porównania. Nie jest wejściem do generowania `sample` i nie zawiera
autorskiego generatora.
