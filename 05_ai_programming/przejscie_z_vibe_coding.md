# Przejście Z Vibe Codingu Do Codexa: 4h

Uczestnik ma cztery karty procedur, kandydackie artefakty zapisane przez
notebooki oraz dostęp do `04_vibe_coding/reference_results/`. Celem jest
zobaczenie projektu jako łańcucha decyzji i zależnych funkcjonalności, nie
odtwarzanie autorskiego pipeline'u full.

Zacznij od sprawdzenia, czy ostatnia komórka notebooka 04 zwróciła `pushed`
albo `up_to_date`. Następnie sklonuj lokalnie **własne prywatne repo
uczestnika**, nie publiczny wzorzec. Dzięki temu Codex zobaczy sprawdzone
artefakty w `04_vibe_coding/outputs/` oraz ich historię commitów.

Punktem wyjścia jest model kodowania opisany wcześniej przez badacza, a nie
kod. Wypełnij najpierw
`resources/templates/codex_adaptation_brief_template.md`: wskaż pytanie,
jednostki kodowania, znaczenie etapów D/F/S/T, decyzje zastrzeżone dla badacza
i tylko jedną planowaną adaptację.

Wspólna pętla pracy pozostaje taka sama jak w Colabie:

```text
model kodowania -> cel etapu -> potrzebna procedura -> karta badawcza
-> techniczny kontrakt -> mała funkcja -> checklista
-> przegląd danych -> decyzja badacza
```

Codex scala i adaptuje infrastrukturę. Nie rozstrzyga relewancji fragmentu,
nie zatwierdza kodów oraz nie przenosi automatycznie kodów zaakceptowanych dla
innego korpusu lub pytania badawczego.

## Zasada Zakresu

Codex może czytać:

- cztery notebooki uczestnika, karty procedur i własne artefakty;
- `codebook_schema.md`, `io_contract.md` i notatki audytowe;
- referencyjny codebook CSV oraz przypisania full do porównań i walidacji.

Nie prosimy go o analizę autorskich notebooków, kompletnych runnerów,
dostrojonych promptów, logów API, embeddingów, cache ani kolejek audytu.
Relacje D-D nie są domyślnym zadaniem.

## Start: Krótki Prompt

```text
Najpierw nie zmieniaj plików. Przejrzyj cztery notebooki uczestnika, moje
karty procedur, handoff i kandydackie artefakty. Odtwórz dla każdego etapu:
cel kodowania, wejście, procedurę, kontrolę techniczną, artefakt i decyzję
badacza. Sprawdź ślad do text_unit_id i source_file oraz zależności D -> F ->
S -> T. Wynik full traktuj wyłącznie jako zaakceptowane porównanie skali, nie
jako kod ani książkę do automatycznego przeniesienia.
```

## Blok A: Inwentaryzacja Kart I Artefaktów

**Czas:** 45-50 min

1. Wskaż Codexowi `04_vibe_coding/outputs/`; nie kopiuj plików ręcznie między repo.
2. Poproś o zestawienie `cel → wejście → procedura → artefakt → kontrola → decyzja`.
3. Porównaj mapę Codexa z własnym protokołem kodowania.
4. Zapisz krótki przepływ:

```text
transkrypcje -> jednostki -> D -> F -> S -> T -> książka
```

**Wynik:** `05_ai_programming/outputs/pipeline_map.md` albo poprawiona notatka
w `handoff_to_codex.md`. Mapa ma wynikać z modelu kodowania, nie z nazw plików.

## Blok B: Walidator Książki

**Czas:** 60 min

Uruchom przygotowany walidator i jego testy, zanim cokolwiek zmienisz:

```bash
python 05_ai_programming/starter/validate_codebook.py \
  04_vibe_coding/reference_results/codebook_prekariat_full.csv
python -m unittest discover -s 05_ai_programming/starter/tests
```

Walidator sprawdza:

- wymagane kolumny i unikalne `code_id`;
- istnienie każdego `parent_code_id` i brak cykli;
- rodziców D->F, F->S i S->T;
- puste definicje/kryteria D;
- kompletne definicje oraz kryteria włączenia i wyłączenia S;
- puste `parent_code_id` dla T;
- przykład, `text_unit_id` i `source_file` dla wpisu `accepted`;
- brak automatycznej zmiany `candidate` na `accepted`.

Najpierw nazwij problem: kandydacki D/F/S może zniknąć z przepływu bez jawnej
decyzji o rodzicu albo `needs_review`. Określ, jaki raport pozwoli badaczowi
wykonać review i jakiego wniosku raport nie może narzucać.

Dopiero potem przeczytaj techniczny punkt rozszerzenia
`find_unmapped_candidate_codes`. Opisz jego wejście, oczekiwany wynik,
przypadek zwykły i brzegowy oraz zakaz automatycznego przypisywania rodzica.
Poproś Codexa o implementację tej jednej funkcji i odblokowanie testu.
Uruchom testy ponownie. Dopiero potem uruchom walidator osobno na sample i
`reference_results/codebook_prekariat_full.csv`. Błąd sample nie dowodzi błędu
full i odwrotnie.

**Wynik:** skrypt oraz czytelny raport PASS/FAIL.

## Blok C: Jedna Kontrolowana Adaptacja

**Czas:** 55-60 min

Każda para wybiera jedno zadanie wynikające z briefu adaptacji:

- podmiana listy plików wejściowych bez zmiany modelu kodowania;
- zmiana pytania badawczego lub soczewki z nową etykietą przebiegu;
- wydzielenie katalogu wynikowego do konfiguracji;
- dodanie raportu pokazującego wpływ jednego parametru na relewancję i kody D;
- dodanie testu kontraktu jednostki kodowania dla nowego układu transkrypcji.

Oddziel zmianę techniczną od analitycznej. Nowy format plików może wymagać
zmiany parsera; nowe pytanie badawcze wymaga ponownej oceny relewancji i
kodowania, a nie prostego skopiowania książki kodowej.

Prompt:

```text
Wykonaj tylko tę zmianę: [jedno zdanie]. Najpierw wskaż pliki i test
akceptacyjny. Po implementacji uruchom test, pokaż wynik i nie modyfikuj
autorskich wyników full.
```

**Wynik:** jedna mała zmiana, test i opis sposobu sprawdzenia.

## Blok D: Złożenie Procedur, Skala I Git

**Czas:** 45-50 min

Najpierw złóż cztery procedury w jedną mapę i sprawdź, czy każdy artefakt ma
następnego odbiorcę oraz bramkę decyzji badacza. Dopiero wtedy można opcjonalnie
nazwać role przyszłego workflow, np. `Unitizer`, `Descriptive Coder`,
`Category Curator`, `Evidence Checker` i `Human Review Gate`.

Prowadzący krótko wskazuje, gdzie przy większej skali przydałyby się
embeddingi, cache, Flex/background i checkpointy. Uczestnicy nie implementują
tych mechanizmów; opisują tylko ich funkcję oraz ryzyko dla audytu.

Na koniec sprawdź:

```bash
git status
git diff --check
```

Do commita dodaj kod, test, konfigurację i decyzje. W `outputs/` zachowuj tylko
sprawdzone produkty wybrane przez notebooki; nie dodawaj pełnych logów API,
kluczy ani pipeline'u autorskiego.

## Pytania Końcowe

1. Które kontrole są deterministyczne i nie potrzebują LLM?
2. Gdzie wynik wymaga interpretacyjnej decyzji badacza?
3. Co w sample jest wystarczające do nauki mechaniki, a czego dowiadujemy się
   dopiero z full?
4. Która procedura wymagałaby przy większej skali checkpointu albo doboru
   kandydatów i dlaczego nie zmienia to jej kryteriów metodologicznych?
