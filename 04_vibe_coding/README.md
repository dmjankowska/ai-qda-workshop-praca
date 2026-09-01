# Ścieżka 3: Vibe Coding For QDA

**Środowisko:** czat AI w Google Colabie oraz API Gemini lub OpenAI.

**Warunek wejścia:** ukończony
[moduł zerowy GitHub + Colab + Gemini](../00_github_colab/README.md). Jego
zalecane 2 godziny 30 minut są dodatkowe i nie wchodzą do ośmiu godzin tego
modułu.

W tym module uczestnik nie tworzy pojedynczej odpowiedzi analitycznej. W
czterech małych notebookach projektuje zależne procedury prowadzące od
rejestru materiału do kandydackiej książki kodowej. AI pomaga pisać krótkie
kontrole i proponuje wyniki, a badacz projektuje model kodowania, ocenia
fragmenty oraz zapisuje decyzje.

Nie mieszamy dwóch porządków. Kod powstaje przez rozmowę w czacie Colaba i
jest wklejany do jednej komórki uczestnika. Analiza fragmentów odbywa się
dopiero przez wspólny adapter API; wybór `gemini` albo `openai` nie zmienia
komórek analitycznych ani struktury artefaktów.

Każdy blok działa na świeżym klonie prywatnego repo uczestnika. Sprawdzone
produkty trafiają do `04_vibe_coding/outputs/`, a osobna komórka tworzy commit
i push. Dzięki temu kolejny notebook oraz później Codex mogą odczytać ten sam
stan pracy. Bez sekretów repo notebook pozostaje w bezpiecznym trybie
demonstracyjnym i nie publikuje wyników.

## Jak Pracujemy Low-code/no-code

Nie pisz pipeline'u z pamięci i nie proś modelu o cały projekt. Uzupełnij
protokół kodowania, wybierz jeden cel etapu i nazwij potrzebną procedurę.
Najpierw opisz jej sens badawczy, rezultat, kontrolę i decyzję zastrzeżoną dla
badacza. Dopiero przygotowana infrastruktura dołącza nazwę funkcji, schemat
tabeli oraz przypadek brzegowy. Uczestnik ocenia checklistę, rekordy i
ograniczenie.

Główna praca uczestnika dotyczy pytania badawczego, soczewki relewancji,
jednostki kodowania, porównywania kodów i fragmentów, granic kategorii,
przypadków negatywnych oraz decyzji o książce kodowej. Przygotowane moduły
Pythona są infrastrukturą, nie materiałem do zapamiętania.

## Najpierw Zobacz Rezultat

Moduł zaczyna się od krótkiego spaceru po
[zaakceptowanym wyniku referencyjnym](reference_results/README.md) dla 32
wywiadów. Oglądamy tylko:

1. skalę i jedną ścieżkę `T -> S -> F -> D -> cytat`;
2. jedną operacyjną kartę S w pełnej książce kodowej;
3. graf relacji w widoku `F-F + T-T` oraz legendę.

Pełna książka i przypisania są dostępne później do walidacji w Codexie.
Embeddingi, cache, Flex, wykonanie asynchroniczne, kolejki audytowe, relacje
D-D, logi kosztowe i kod autorskiego generatora nie należą do głównej ścieżki
uczestnika.

## Co Budujesz

Na ograniczonym pakiecie z `PREWORK_01-03` tworzysz jawne artefakty czterech
procedur:

```text
ograniczony pakiet rzeczywistych fragmentów
  -> rejestr jednostek i stabilne identyfikatory
  -> selekcja fragmentów relewantnych dla doświadczeń prekaryjnych
  -> przypisania kod-fragment i procesualne kody D
  -> wzorce i mechanizmy F
  -> operacyjne karty S
  -> oszczędne zakresy T
  -> książka T-S-F-D, statystyki i kolejka przeglądu
```

Wynik uczestnika jest kandydacki i celowo ograniczony. Wynik `full` pokazuje
rezultat pogłębionej procedury autorskiej, nie obiecuje więc, że cztery
ćwiczenia odtworzą identyczną książkę.

## Cztery Etapy

| Etap | Główne zadanie | Najważniejsze wyjście | Pytanie kontrolne |
| --- | --- | --- | --- |
| 1. Przygotowanie | Porównaj możliwe jednostki i zachowaj źródło, kolejność, mówcę oraz dokładny tekst. | `01_unit_register.csv` i decyzja o polityce jednostki | Czy od identyfikatora wrócę do niezmienionego tekstu? |
| 2. Kodowanie opisowe | Najpierw oceń relewancję, potem nadaj 0-n kandydackich kodów D. | `02_d_assignments.csv` i log porównania promptów | Czy D jest krótką procesualną parafrazą cytatu? |
| 3. Kodowanie zogniskowane | Porównuj profile D i twórz F tylko dla wspólnego wzorca lub mechanizmu. | `03_focused_categories.csv` oraz `03_d_to_f.csv` | Co F pozwala zobaczyć ponad pojedyncze D? |
| 4. Książka kodowa | Z kilku zgodnych F zbuduj jedną operacyjną S i umieść ją w oszczędnym T. | `04_candidate_codebook.csv` i handoff do Codexa | Czy drugi koder wie, kiedy zastosować S i kiedy go nie stosować? |

Każdy etap kończy się checklistą, inspekcją rekordów i decyzją badacza.
Liczebności mogą służyć kontroli pokrycia procedury, ale nie rankingowi
ważności kodów.

## Różne Role Poziomów

- **D** odpowiada „o czym mówi fragment?”; nazwa pełni funkcję opisu, więc nie
  ma osobnej definicji.
- **F** odpowiada „jaki ważniejszy wzorzec lub mechanizm reprezentują te
  obserwacje?”.
- **S** jest kartą operacyjną: ma definicję, kryterium włączenia, kryterium
  wyłączenia, granicę i przykład.
- **T** porządkuje szerszy zakres analityczny i wspiera memo; nie jest kodem
  do bezpośredniego nakładania na fragment.

### Co Oznacza „synthetic” W Poziomie S

`Synthetic coding` oznacza tutaj **syntezę** kilku zgodnych wzorców F w
operacyjną kartę kodu wyższego rzędu. Nie oznacza danych sztucznie
wygenerowanych ani automatycznie prawdziwej interpretacji. W wyniku
referencyjnym `synthetic_codes.csv` zawiera karty S z definicją i
kryteriami. Na warsztacie ich kandydacki odpowiednik trafia do
`04_candidate_codebook.csv` i wymaga przeglądu badacza.

## Tryb Warsztatowy I Tryb Autorski

Na zajęciach pracujesz synchronicznie na małej próbie: jedna procedura, wynik,
kontrola i poprawka. Korzystasz z
[czterech notebooków uczestnika](participant_notebooks/README.md), czatu AI
Colaba i synchronicznych odpowiedzi API Gemini albo OpenAI. Nie implementujesz
Flex, pollingu, cache, embeddingowego
retrievalu, wielorundowej harmonizacji ani pełnej relacyjnej analizy.

Te mechanizmy są krótko omawiane jako rozwiązania potrzebne przy skali 32
wywiadów z użyciem [noty dla prowadzącego](notatka_dla_prowadzacego_skalowanie.md).
Ich dostrojona implementacja pozostaje w repozytorium autorów.

## Dwa Zakresy

- `sample` - ograniczony pakiet fragmentów z `PREWORK_01-03` oraz artefakty
  tworzone kolejno w czterech notebookach;
- `full` - 32 wywiady; uczestnik ogląda wynik i używa jego wybranych tabel do
  porównania oraz walidacji.

Nie łącz rekordów obu zakresów. Porównuj ich strukturę, pokrycie i zróżnicowanie.

## Minimalna Pętla Pracy

1. Zapisz jednozdaniowy cel etapu.
2. Nazwij potrzebną procedurę i jej widoczny rezultat.
3. Uzupełnij kartę: wejście, kontrola i decyzja badacza.
4. Pozwól infrastrukturze dodać interfejs i poproś czat Colaba o jedną małą
   funkcję.
5. Uruchom checklistę i obejrzyj rekordy, nie tylko komunikat „sukces”.
6. Przez API porównaj dwa prompty analityczne na tym samym materiale; provider
   wybierz w jednym formularzu.
7. Nazwij niespełnione wymaganie, popraw kartę lub prompt i ponów krok.
8. Sprawdź artefakty, zapisz wybrane wyniki i decyzje w prywatnym repo, a pełne
   logi API pozostaw domyślnie poza historią.

## Zacznij

[Przejdź do czterech notebooków uczestnika](participant_notebooks/README.md).

Odznaki w tym katalogu otwierają czyste wzorce prowadzących. Do właściwej pracy
otwórz notebook z własnego prywatnego repo przez
**Plik → Otwórz notatnik → GitHub**.

1. [Wynik referencyjny](reference_results/README.md)
2. [Plan 8 godzin](plan_warsztatu.md)
3. [Kontrakt wejść i wyjść](io_contract.md)
4. [Schemat książki kodowej](codebook_schema.md)
5. [Protokół kodowania](../resources/templates/coding_pipeline_protocol_template.md)
6. [Cztery notebooki Colab](participant_notebooks/README.md)
7. [Przejście do Codexa](../05_ai_programming/przejscie_z_vibe_coding.md)
