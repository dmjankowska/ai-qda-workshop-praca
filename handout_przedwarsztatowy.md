# Przed warsztatem: przygotuj konta i komputer

Ten handout jest przeznaczony dla osób uczestniczących w warsztacie
**wykorzystania AI i dużych modeli językowych w jakościowej analizie danych**.
Nie musisz mieć wcześniejszego doświadczenia z programowaniem, GitHubem ani
Google Colab.

Przeznacz na przygotowanie około **30-45 minut**, najlepiej co najmniej dzień
przed zajęciami. Pracuj na własnym laptopie, na którym możesz instalować
aplikacje.

> **Najważniejsze:** publiczne repo zawiera materiały, a własne prywatne repo
> będzie trwałym miejscem Twojej pracy. Colab uruchamia kod w środowisku
> tymczasowym, dlatego sprawdzone wyniki będziemy zapisywać w prywatnym repo.
> Token GitHub i klucz modelu są dwoma różnymi sekretami. Żadnego z nich nie
> wklejaj do notebooka.

## Co przygotować

Przed warsztatem przygotuj:

- konto GitHub z potwierdzonym adresem e-mail;
- konto Google i działający dostęp do Google Colab;
- prywatne repo warsztatowe utworzone z publicznego szablonu;
- ograniczony token GitHub zapisany jako sekret Colaba;
- konto ChatGPT/OpenAI oraz aplikację ChatGPT z dostępem do Codexa;
- Git i Python 3.11 lub nowszy na własnym komputerze;
- jeden wskazany przez prowadzącego klucz API: Gemini albo OpenAI.

W module wprowadzającym można pracować bez klucza API. Główne notebooki Vibe
Coding mają również bezkosztowy tryb `mock`, który pozwala sprawdzić przepływ,
ale nie tworzy rzeczywistego wyniku analitycznego.

## 1. Konto GitHub i prywatne repo

1. Utwórz bezpłatne konto na [GitHubie](https://github.com/signup) albo
   zaloguj się na istniejące.
2. Potwierdź adres e-mail i włącz uwierzytelnianie dwuskładnikowe (2FA).
3. Otwórz publiczny szablon
   [ai_qda-workshop-1u](https://github.com/caqdastm/ai_qda-workshop-1u).
4. Wybierz **Use this template -> Create a new repository**.
5. Nadaj repo nazwę, np. `ai-qda-workshop-praca`, i wybierz widoczność
   **Private**.
6. Sprawdź etykietę `Private` przy nazwie repo i zapisz jego identyfikator w
   formacie `login/nazwa-repo`.

Nie używaj publicznego forka do przechowywania wyników. Repo utworzone z
szablonu jest samodzielną kopią i może być prywatne. Nie wymaga to płatnego
planu GitHub ani znajomości poleceń Git. Pomoc GitHuba:
[tworzenie konta](https://docs.github.com/en/account-and-profile/how-tos/account-management/creating-an-account-on-github)
oraz
[tworzenie repo z szablonu](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template).

### Token do zapisywania wyników z Colaba

Utwórz token typu **fine-grained personal access token**:

1. GitHub -> **Settings -> Developer settings -> Personal access tokens ->
   Fine-grained tokens -> Generate new token**.
2. Ustaw krótki termin ważności obejmujący warsztat.
3. W **Repository access** wybierz wyłącznie prywatne repo warsztatowe.
4. W **Repository permissions** ustaw tylko **Contents: Read and write**.
5. Wygeneruj token i zachowaj go w menedżerze haseł.

Nie przyznawaj tokenowi dostępu do wszystkich repozytoriów ani uprawnień
administracyjnych. Po warsztacie możesz go unieważnić bez usuwania repo i
zapisanej historii. Szczegóły opisuje dokumentacja
[GitHub personal access tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens).

## 2. Konto Google i Google Colab

1. Zaloguj się na konto Google.
2. Otwórz [Google Colab](https://colab.research.google.com/).
3. Utwórz pusty notebook.
4. W pierwszej komórce wpisz i uruchom:

   ```python
   print("Colab działa")
   ```

5. Sprawdź, czy pod komórką pojawił się tekst `Colab działa`.
6. Sprawdź, czy w interfejsie widzisz ikonę Gemini lub panel pomocy AI.

Do ćwiczeń nie jest potrzebny Colab Pro. Runtime Colaba jest tymczasowy:
może zostać wyłączony, a po rozpoczęciu nowej sesji komórki wykonuje się od
góry. Trwałe będą dopiero pliki opublikowane w prywatnym repo.

Brak panelu Gemini nie blokuje modułu wprowadzającego. Notebook zawiera
rozwiązanie bazowe, a kod można również uzyskać w zwykłym czacie Gemini.
Aktualne informacje o środowisku znajdują się w
[FAQ Google Colab](https://research.google.com/colaboratory/faq.html).

### Dodaj sekrety prywatnego repo

W Colabie wybierz po lewej stronie ikonę klucza **Secrets**, a następnie dodaj:

- `AI_QDA_REPOSITORY` z wartością `login/nazwa-repo`;
- `GITHUB_TOKEN` z ograniczonym tokenem utworzonym wcześniej.

Włącz dostęp obu sekretów dla otwartego notebooka. Nie wpisuj tokenu do kodu,
promptu, komentarza, adresu repo ani commita.

Pełna instrukcja wraz z testem zapisu znajduje się w
[module GitHub i Colab](00_github_colab/instrukcja_konto_fork_colab.md).

## 3. Sprawdź trwały zapis wyników

Ten test potwierdza, że Colab korzysta z właściwego repo, a wynik nie zniknie
po zakończeniu runtime'u.

1. Otwórz notebook
   [`00_start_here_github_colab.ipynb`](00_github_colab/00_start_here_github_colab.ipynb)
   z własnego prywatnego repo przez **Plik -> Otwórz notatnik -> GitHub**.
2. Uruchom komórki od początku.
3. Sprawdź komunikat `Tryb workspace: participant_repository` i nazwę swojego
   repo.
4. Uzupełnij kartę procedury i przeczytaj utworzony plik.
5. Dopiero po kontroli ustaw `PUBLISH_RESULTS_TO_GITHUB=True`.
6. Oczekiwany status to `pushed`. Status `up_to_date` oznacza, że identyczna
   wersja jest już zapisana.
7. Na stronie prywatnego repo znajdź plik
   `00_github_colab/outputs/00_procedure_card.csv` oraz commit.

Jeśli notebook pokazuje `public_demo`, działa na publicznym wzorcu i nie może
publikować wyników. Sprawdź nazwy sekretów, ich dostęp dla notebooka oraz
uprawnienie tokenu do prywatnego repo.

Komórka publikacji zapisuje wybrane produkty z `outputs/`, ale nie zapisuje
zmian w samym notebooku. Notebook zachowasz osobno przez
**Plik -> Zapisz kopię w GitHubie**, wybierając własne prywatne repo i tę samą
ścieżkę pliku.

## 4. Konto OpenAI i aplikacja ChatGPT z Codexem

Ta część jest potrzebna przed lokalnym blokiem wprowadzającym do pracy z
Codexem.

1. Utwórz konto ChatGPT/OpenAI albo zaloguj się na konto wskazane przez swoją
   instytucję.
2. Pobierz aplikację z oficjalnej strony
   [ChatGPT desktop app](https://learn.chatgpt.com/docs/app).
3. Zainstaluj aplikację, uruchom ją i zaloguj się.
4. Sprawdź, czy możesz rozpocząć zadanie w Codexie i wybrać lokalny folder.
5. Utwórz pusty folder testowy, otwórz go jako projekt i wyślij prośbę:

   ```text
   Wyjaśnij, jakie pliki znajdują się w tym folderze. Niczego nie zmieniaj.
   ```

Dla pustego folderu poprawna jest informacja, że nie ma w nim plików. Ważne
jest samo otwarcie lokalnego projektu. Podczas warsztatu Codex otworzy lokalny
klon tego samego prywatnego repo, w którym Colab zapisał wcześniejsze wyniki.

Konto instytucjonalne może ograniczać instalowanie aplikacji albo dostęp do
Codexa. Sprawdź to przed zajęciami i zgłoś prowadzącym, jeśli nie widzisz tej
funkcji po zalogowaniu.

## 5. Git i Python do lokalnego ćwiczenia

Zainstaluj:

- [Git](https://git-scm.com/downloads);
- [Python 3.11 lub nowszy](https://www.python.org/downloads/).

Opcjonalnie możesz użyć
[GitHub Desktop](https://desktop.github.com/download/), jeżeli wolisz pobrać
repozytorium przez interfejs graficzny.

Po instalacji otwórz PowerShell na Windows albo Terminal na macOS/Linux i
sprawdź:

```text
git --version
python --version
```

Jeżeli drugie polecenie nie działa, spróbuj `py --version` na Windows albo
`python3 --version` na macOS/Linux. Wynik powinien wskazywać Python 3.11 lub
nowszy.

Nie trzeba instalować Node.js, WSL, Jupytera, VS Code ani PyCharma.

## 6. Jeden klucz API do analizy materiału

Konto ChatGPT, panel Gemini w Colabie i klucz API pełnią różne funkcje:

- konto lub panel czatu służy do rozmowy z modelem i projektowania kodu;
- klucz API pozwala notebookowi wywołać model podczas analizy materiału;
- `GITHUB_TOKEN` służy wyłącznie do odczytu i zapisu prywatnego repo.

Przygotuj tylko dostawcę wskazanego przez prowadzącego. Nie twórz dwóch kluczy
„na wszelki wypadek”. W obrębie jednego ćwiczenia używaj tego samego modelu,
bo zmiana modelu utrudnia porównanie wpływu promptu i procedury.

### Gemini API

1. Zaloguj się do [Google AI Studio](https://aistudio.google.com/).
2. Otwórz [API Keys](https://aistudio.google.com/apikey) i utwórz klucz do
   projektu wskazanego na warsztacie.
3. Sprawdź dostępność usługi, limity i zasady rozliczeń dla swojego regionu.
4. Zapisz klucz w menedżerze haseł.

### OpenAI API

1. Zaloguj się do [OpenAI API Platform](https://platform.openai.com/).
2. Otwórz [API keys](https://platform.openai.com/api-keys) i utwórz zwykły
   klucz projektu, nie klucz administracyjny.
3. Sprawdź rozliczenia i dostępny limit. Subskrypcja ChatGPT nie oznacza
   automatycznie środków na API.
4. Zapisz klucz w menedżerze haseł.

### Dodaj klucz do Colaba

W panelu **Secrets** dodaj tylko właściwy sekret i włącz jego dostęp dla
notebooka:

- `GEMINI_API_KEY` dla Gemini; albo
- `OPENAI_API_KEY` dla OpenAI.

Nie wpisuj klucza do notebooka, promptu, czatu, nazwy pliku, zrzutu ekranu ani
commita. Jeśli trafił do GitHuba lub wiadomości, natychmiast go unieważnij i
utwórz nowy.

W wariancie OpenAI notebook pozwala świadomie wybrać ustawienie
`OPENAI_STORE_RESPONSES`. `True` umożliwia późniejsze pobranie odpowiedzi
przez jej identyfikator w okresie retencji, a `False` wyłącza taki zapis po
stronie Responses API. Ustawienie nie zastępuje zasad bezpieczeństwa i
retencji dostawcy.

## 7. Dane, modele i prywatność

W części analitycznej pracujemy z publicznie udostępnionym i zanonimizowanym
korpusem wywiadów z projektu PREWORK: **„Młodzi pracownicy prekaryjni w Polsce
i Niemczech: socjologiczne studium porównawcze warunków pracy i życia,
świadomości społecznej i aktywności obywatelskiej”**. Repo warsztatowe zawiera
kopię 32 transkrypcji, materiały kontekstowe i metryczkę. Szczegóły znajdują
się w [opisie korpusu](01_data/prekariat/README.md).

Pierwsze ćwiczenie techniczne korzysta z osobnej mini-transkrypcji. W głównej
części wybrane fragmenty rzeczywistych wywiadów mogą być przesyłane do
Gemini API albo OpenAI API. Anonimizacja i publiczna dostępność nie zmieniają
tych materiałów w dane syntetyczne.

Przed przesłaniem własnych danych sprawdź podstawę ich przetwarzania, zgodę,
anonimizację oraz zasady projektu, instytucji i wybranego dostawcy. Nie używaj
własnych materiałów w ćwiczeniu, jeśli nie masz pewności, że wolno je
przekazać do danej usługi.

Korzystanie z modelu oznacza, że dostawca przetwarza prompt i przesłany
fragment, aby wygenerować odpowiedź. Warunki, retencja i dostęp ludzi do
danych mogą zależeć od produktu, planu, regionu oraz ustawień konta. Przed
zajęciami zapoznaj się z aktualnymi zasadami:

- [Google Colab FAQ](https://research.google.com/colaboratory/faq.html);
- [warunki Gemini API](https://ai.google.dev/gemini-api/terms) i
  [zasady użycia](https://ai.google.dev/gemini-api/docs/usage-policies);
- [OpenAI API data controls](https://developers.openai.com/api/docs/guides/your-data).

Pełne logi wywołań API mogą zawierać prompty, fragmenty korpusu i odpowiedzi.
Dlatego pliki `*_prompt_runs.jsonl` są domyślnie pomijane podczas publikacji
do repo. Zanim zapiszesz inne produkty, przeczytaj je i sprawdź diff.

## 8. Test gotowości dzień przed zajęciami

Zaznacz każde pole:

- [ ] Mogę zalogować się do GitHuba, a mój adres e-mail jest potwierdzony.
- [ ] Utworzyłem z publicznego szablonu własne repo z etykietą `Private`.
- [ ] Mój fine-grained `GITHUB_TOKEN` ma dostęp tylko do tego repo i
  uprawnienie **Contents: Read and write**.
- [ ] W Colab Secrets mam `AI_QDA_REPOSITORY` oraz `GITHUB_TOKEN` i włączyłem
  ich dostęp dla notebooka startowego.
- [ ] Notebook pokazuje `Tryb workspace: participant_repository`.
- [ ] Plik `00_github_colab/outputs/00_procedure_card.csv` jest widoczny w
  prywatnym repo po statusie `pushed` albo `up_to_date`.
- [ ] Otwieram Colab i potrafię uruchomić prostą komórkę.
- [ ] Widzę panel Gemini albo wiem, że skorzystam z rozwiązania bazowego.
- [ ] Aplikacja ChatGPT jest zainstalowana i mogę otworzyć lokalny folder w
  Codexie.
- [ ] `git --version` pokazuje zainstalowaną wersję Git.
- [ ] Polecenie dla Pythona pokazuje wersję 3.11 lub nowszą.
- [ ] Mam jeden wskazany klucz API zapisany jako sekret Colaba albo wiem, że
  podczas ćwiczenia wybiorę tryb `mock`.
- [ ] Mam urządzenie potrzebne do 2FA, ładowarkę, aktualną przeglądarkę i około
  2 GB wolnego miejsca.

## Zasady bezpieczeństwa podczas warsztatu

- Nie publikuj sekretów, plików `.env`, haseł ani danych wrażliwych.
- Nie wpisuj kluczy do czatu AI w celu rozwiązania problemu technicznego.
- Nie uruchamiaj wielu notebooków równolegle na tym samym repo.
- Publikuj tylko przeczytane produkty z katalogów `outputs/`.
- Nie uruchamiaj ponownie płatnego wywołania tylko dlatego, że wynik wymaga
  interpretacji. Najpierw omów go i sprawdź koszt.
- Walidacja techniczna potwierdza strukturę pliku, nie trafność kodu,
  kategorii ani interpretacji. Te decyzje należą do badacza.

## Gdy coś nie działa

Nie czekaj do rozpoczęcia zajęć. Wyślij prowadzącym:

1. nazwę i wersję systemu operacyjnego;
2. informację, na którym kroku pojawia się problem;
3. dokładny komunikat błędu lub zrzut ekranu bez sekretów;
4. wynik `git --version` oraz polecenia sprawdzającego wersję Pythona, jeżeli
   problem dotyczy części lokalnej.

Nigdy nie wysyłaj prowadzącym hasła, tokenu GitHub ani wartości klucza API.
