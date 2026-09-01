# Schemat Książki Kodowej Prekariat

Produktem warsztatowym jest kandydacka książka kodowa, a produktem
referencyjnym książka opracowana na pełnym korpusie:

- `MyDrive/AI_QDA_Workshop/04_candidate_codebook.csv` - kandydacka tabela
  uczestnika do walidacji i dalszego przeglądu;
- [`../01_data/codebook/codebook_prekariat_final.csv`](../01_data/codebook/codebook_prekariat_final.csv)
  i [wersja Markdown](../01_data/codebook/codebook_prekariat_final.md) - wynik
  `full` do porównania struktury oraz skali.

Przypisania kod-fragment pozostają w osobnej tabeli
`MyDrive/AI_QDA_Workshop/02_d_assignments.csv`.
Jedna jednostka może mieć kilka kodów, a część jednostek nie otrzymuje żadnego.

## Poziomy Hierarchii

```text
T01 zakres teoretyczny
  S01 operacyjna karta książki kodowej
    F001 wzorzec lub mechanizm zogniskowany
      D0001 procesualna parafraza blisko danych
```

| Poziom | Pytanie | Rola | Wymagane pola analityczne |
| --- | --- | --- | --- |
| D | O czym mówi ten fragment? | Krótka procesualna parafraza ściśle związana z cytatem. | Nazwa, cytat i ślad do danych; bez osobnej definicji i kryteriów. |
| F | Jaki ważniejszy wzorzec lub mechanizm reprezentują te obserwacje? | Zachowuje analityczne zróżnicowanie kilku D. | Nazwa, krótkie objaśnienie wzorca, przykłady i uzasadnienie grupowania. |
| S | Kiedy drugi koder powinien zastosować ten kod do nowego fragmentu? | Operacyjna karta książki kodowej. | Definicja, kryteria włączenia i wyłączenia, granica oraz przykład. |
| T | Jaki szerszy zakres analityczny porządkuje te karty S? | Oszczędna rama i poziom memo. | Nazwa i zakres analityczny; nie udaje kodu operacyjnego. |

S pochodzi od `synthetic coding`: syntezy kilku zgodnych wzorców F w kod
wyższego rzędu, który można operacjonalizować w książce kodowej. „Synthetic”
nie opisuje pochodzenia danych i nie oznacza sztucznie wygenerowanego korpusu.

- `T...` nie ma rodzica;
- `S...` wskazuje rodzica `T...`;
- `F...` wskazuje rodzica `S...`;
- `D...` wskazuje rodzica `F...`;
- element `needs_review` może chwilowo pozostać bez rodzica, ale nie może zniknąć.

## Minimalne Kolumny CSV

```text
code_id
parent_code_id
code_name
code_level
definition
inclusion_criteria
exclusion_criteria
example_quote
text_unit_id
source_file
review_status
```

Wynik `full` może zawierać dodatkowe pola audytowe, takie jak `code_type`,
`related_research_question`, `stage`, `created_by`, `prompt_id`, `notebook`,
`cell_reference`, `audit_notes` i `version`. Walidator uczestnika nie wymaga
ich w kandydackim artefakcie z małej próbki.

`code_level` przyjmuje wartości `descriptive`, `focused`, `synthetic`
lub `theoretical`. Pola `definition`, `inclusion_criteria` i
`exclusion_criteria` są obowiązkowe dla S. D pozostawia je puste; F może
zawierać opis analityczny w `definition`, a T krótki zakres analityczny.

## Kryteria Akceptacji

Każdy zaakceptowany wpis:

- ma stabilny `code_id`, poprawnego rodzica i decyzję badacza w audycie;
- prowadzi przez `example_quote`, `text_unit_id` i `source_file` do danych;
- nie jest duplikatem innego wpisu na tym samym poziomie;
- zachowuje różnicę między dowodem, interpretacją i hipotezą memo.

Dodatkowo:

- D ma nazwę gerundialną/odczasownikową i jest krótką parafrazą działania lub
  procesu, nie tematem;
- F wnosi nazwany zysk analityczny ponad pojedyncze D i nie wynika wyłącznie z
  podobieństwa słów;
- S ma definicję oraz sprawdzalne kryteria włączenia i wyłączenia, które
  odróżniają ją od sąsiednich S;
- T porządkuje S bez dopisywania gotowej teorii i bez kryteriów właściwych
  kodowi operacyjnemu.

Status `accepted` może nadać wyłącznie badacz. Poprawne wykonanie kodu ani
odpowiedź LLM nie są akceptacją analityczną.

## Czego Nie Wpisywać Jako Kod

- streszczeń całych fragmentów;
- tematów tak szerokich jak „problemy”, „praca” albo „relacje”;
- kategorii połączonych tylko przez podobne słowa lub częstość;
- interpretacji bez przykładu, granicy i możliwości powrotu do danych;
- wyników AI, których nikt ręcznie nie sprawdził.
