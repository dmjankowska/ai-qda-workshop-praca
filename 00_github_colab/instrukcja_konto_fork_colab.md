# Konto, prywatne repo i trwała praca w Colabie

Publiczne repo warsztatu jest wzorcem materiałów, ale nie jest miejscem na
wyniki uczestników. Publiczny fork również pozostaje publiczny. Dlatego do
pracy tworzymy **nowe prywatne repo z publicznego szablonu**.

## Docelowy przepływ

```text
publiczny wzorzec caqdastm/ai_qda-workshop-1u
  -> prywatne repo uczestnika utworzone przez Use this template
  -> notebook klonuje prywatne repo do runtime'u Colaba
  -> zapisuje sprawdzone produkty w outputs/
  -> osobna zgoda uruchamia commit i push
  -> kolejny notebook klonuje repo i czyta wcześniejszy produkt
  -> Codex pracuje później na lokalnym klonie tego samego repo
```

## 1. Utwórz prywatne repo z szablonu

1. Zaloguj się na GitHubie i otwórz
   [publiczne repo warsztatu](https://github.com/caqdastm/ai_qda-workshop-1u).
2. Wybierz **Use this template**.
3. Wybierz **Create a new repository**.
4. Jako właściciela wybierz swoje konto.
5. Nadaj nazwę, np. `ai-qda-workshop-praca`.
6. Ustaw widoczność **Private**.
7. Utwórz repo i sprawdź, czy przy nazwie znajduje się etykieta **Private**.

Nie używaj **Fork** do przechowywania wyników. Fork publicznego repo nie może
mieć niezależnie ustawionej prywatnej widoczności.

## 2. Utwórz ograniczony token GitHub

Token pozwala notebookowi sklonować prywatne repo i wysłać do niego wybrane
produkty. Traktuj go jak hasło.

1. Na GitHubie otwórz **Settings** swojego konta.
2. Przejdź do **Developer settings → Personal access tokens → Fine-grained
   tokens**.
3. Wybierz **Generate new token**.
4. Ustaw krótki termin ważności obejmujący warsztat.
5. W **Repository access** wybierz **Only select repositories** i wskaż tylko
   prywatne repo warsztatowe.
6. W **Repository permissions** ustaw **Contents: Read and write**.
7. Nie przyznawaj uprawnień administracyjnych ani dostępu do innych repo.
8. Zapisz token w menedżerze haseł. Pełna wartość nie będzie później widoczna.

## 3. Dodaj dwa sekrety w Colabie

1. Otwórz dowolny notebook warsztatowy w Colabie.
2. W lewym panelu wybierz ikonę klucza **Secrets**.
3. Dodaj sekret `AI_QDA_REPOSITORY` z wartością w formacie
   `twój-login/ai-qda-workshop-praca`.
4. Dodaj sekret `GITHUB_TOKEN` z tokenem utworzonym wcześniej.
5. Włącz dostęp obu sekretów dla notebooka.

Nie wpisuj tokenu do komórki, promptu ani adresu repo. Notebook przekazuje go
procesowi Git przez tymczasowy nagłówek i nie zapisuje w plikach ani commitach.

Klucze do analitycznego API są osobnymi sekretami: `GEMINI_API_KEY` lub
`OPENAI_API_KEY`. Nie zastępują `GITHUB_TOKEN`.

## 4. Sprawdź prywatny workspace

1. Otwórz notebook
   [`00_start_here_github_colab.ipynb`](00_start_here_github_colab.ipynb).
2. Uruchom komórki od początku.
3. Komórka infrastruktury powinna wyświetlić
   `Tryb workspace: participant_repository` oraz nazwę Twojego repo.
4. Uzupełnij kartę procedury i przeczytaj zapisany plik.
5. Dopiero po kontroli ustaw `PUBLISH_RESULTS_TO_GITHUB=True`.
6. Oczekiwany status to `pushed`. Ponowne uruchomienie bez zmian może zwrócić
   `up_to_date`; oba statusy oznaczają trwały zapis.
7. W prywatnym repo znajdź
   `00_github_colab/outputs/00_procedure_card.csv` i najnowszy commit.

Jeśli widzisz `public_demo`, notebook działa na czystym wzorcu. Możesz obejrzeć
ćwiczenie, ale komórka publikacji nie pozwoli zapisać wyników do repo
prowadzących.

## 5. Otwieraj notebooki z prywatnego repo

Odznaka Colaba jest adresem absolutnym i zawsze otwiera publiczny wzorzec. Nie
potrafi automatycznie przełączyć się na repo konkretnego uczestnika. Zwykłe
linki względne na GitHubie pozostają natomiast w aktualnie oglądanym repo.

Do właściwej pracy:

1. w Colabie wybierz **Plik → Otwórz notatnik → GitHub**;
2. jeśli trzeba, zezwól Colabowi na dostęp do prywatnych repo;
3. wyszukaj własne repo;
4. wybierz notebook z zachowaniem jego oryginalnej ścieżki;
5. uruchom komórki od początku, aby notebook pobrał aktualne wyniki.

## 6. Zapis notebooka i produktów to dwa osobne działania

Komórka `Zapisz trwały punkt kontrolny` publikuje tylko wybrane artefakty z
`outputs/`. Nie zapisuje zmian w samym notebooku.

Po zakończeniu ćwiczenia:

1. sprawdź artefakty i uzyskaj status `pushed` albo `up_to_date`;
2. wybierz **Plik → Zapisz kopię w GitHubie**;
3. wskaż własne prywatne repo;
4. zachowaj oryginalną ścieżkę notebooka;
5. na GitHubie sprawdź osobno commit produktów i commit notebooka.

## 7. Jak kolejny blok odzyskuje wcześniejszą pracę

Cztery notebooki Vibe Coding używają wspólnego katalogu
`04_vibe_coding/outputs/`. Nazwy zaczynają się od numeru bloku, np.:

- `01_unit_register.csv`;
- `02_d_assignments.csv`;
- `03_focused_categories.csv`;
- `04_candidate_codebook.csv`;
- `04_handoff_to_codex.json`.

Nowy runtime klonuje prywatne repo. Następny notebook czyta plik poprzedniego
bloku z tego katalogu. Brak pliku oznacza, że poprzedni wynik nie został
opublikowany albo notebook wskazuje inne repo.

## Bezpieczeństwo i sytuacje awaryjne

- Nie uruchamiaj dwóch notebooków równolegle na tym samym repo. Dwa commity
  mogą wymagać ręcznego rozwiązania konfliktu.
- Publikowane są tylko pliki CSV, JSON i MD z katalogów `outputs/`.
- Pliki `*_prompt_runs.jsonl` pozostają domyślnie poza commitem, ponieważ mogą
  zawierać pełne prompty, fragmenty korpusu i odpowiedzi modelu.
- Helper skanuje wybrane pliki pod kątem typowych formatów tokenów i kluczy.
  Taki skan jest dodatkową ochroną, nie zastępuje przeglądu badacza.
- Jeśli push się nie udał, nie zamykaj sesji. Zachowaj komunikat bez sekretów i
  użyj instrukcji [awaryjnego zapisu](awaryjne_zapisanie_pliku.md).
- Jeśli token pojawił się w notebooku, pliku, commicie albo wiadomości,
  natychmiast go unieważnij i utwórz nowy.
- Po warsztacie możesz unieważnić token. Prywatne repo i historia pracy
  pozostaną dostępne.
