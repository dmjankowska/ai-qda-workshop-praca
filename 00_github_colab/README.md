# GitHub, Colab i Gemini: moduł zerowy

Ten moduł odbywa się **przed ośmiogodzinną częścią Vibe Coding**. Jest
przeznaczony także dla osób, które wcześniej nie korzystały z GitHuba ani
notebooków. Nie jest kursem Pythona. Uczestnik przechodzi przez mały pełny cykl
pracy, zaczynając od potrzeby badawczej:

```text
potrzeba w pracy z materiałem
  -> procedura opisana zwykłym językiem
  -> kontrakt dla asystenta AI
  -> mały fragment kodu
  -> obserwacja wyniku i kontrola techniczna
  -> decyzja badacza
  -> zapis produktów i notebooka w prywatnym repo
```

[![Notebook 00: start](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/caqdastm/ai_qda-workshop-1u/blob/main/00_github_colab/00_start_here_github_colab.ipynb)
[![Notebook 01: Gemini](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/caqdastm/ai_qda-workshop-1u/blob/main/00_github_colab/01_colab_gemini_vibe_coding.ipynb)

### Prywatny workspace a odznaki Colaba

Odznaki mają adresy absolutne i zawsze otwierają publiczny wzorzec. Do trwałej
pracy utwórz prywatne repo przez **Use this template**, a następnie dodaj w
Colab Secrets `AI_QDA_REPOSITORY` i `GITHUB_TOKEN`.

- Pierwsze otwarcie może odbyć się przez odznakę w trybie demonstracyjnym.
- Powrót do zapisanej pracy: wybierz w Colabie
  **Plik -> Otwórz notatnik -> GitHub** i notebook z prywatnego repo.
- Komórka infrastruktury klonuje prywatne repo, a osobna komórka publikuje
  wyłącznie sprawdzone pliki z `outputs/`.

Dokładna ścieżka jest w
[instrukcji prywatnego repo i Colaba](instrukcja_konto_fork_colab.md).

## Ile czasu

**Zalecenie: 2 godziny 30 minut na żywo oraz 20-30 minut przygotowania kont
przed zajęciami.**

- 2 godziny wystarczą, gdy wszyscy mają już prywatne repo, token i sekrety;
- 2 godziny 30 minut dają czas na ćwiczenie, pytania i typowe problemy z
  logowaniem lub zapisem;
- 3 godziny są bezpieczniejsze, jeżeli konta mają być zakładane dopiero na
  sali.

Szczegółowy podział znajduje się w [planie modułu](plan_modulu.md).

## Efekt modułu

Po zakończeniu uczestnik:

- rozróżnia publiczny wzorzec, prywatne repo, runtime i commit;
- wie, co w Colabie jest tymczasowym wykonaniem, a co zapisanym notebookiem lub
  artefaktem;
- rozpoznaje potrzebną procedurę na podstawie celu pracy z materiałem;
- opisuje ją przez `problem + wejście + rezultat + kontrolę + decyzję badacza`;
- z pomocą przygotowanej infrastruktury przekłada ten opis na ograniczone
  zadanie dla Gemini;
- ocenia tabelę wynikową i czytelną listę kontroli zamiast ufać samemu
  komunikatowi sukcesu;
- zapisuje sprawdzone produkty i notebook w prywatnym repo;
- potrafi rozpocząć kolejny notebook od wyników zachowanych w poprzednim.

## Materiały i kolejność

1. Przed zajęciami wykonaj [checklistę kont i dostępu](checklista_przed_zajeciami.md).
2. Przejdź przez [instrukcję prywatnego repo i Colaba](instrukcja_konto_fork_colab.md).
3. Uruchom [notebook 00: od potrzeby do procedury](00_start_here_github_colab.ipynb).
4. Uruchom [notebook 01: od procedury do funkcji z Gemini](01_colab_gemini_vibe_coding.ipynb).
5. Korzystaj z [kart ćwiczeń i promptów](cwiczenia_git_colab_gemini.md).
6. Gdy zapis nie działa, użyj [ścieżki awaryjnej](awaryjne_zapisanie_pliku.md).

## Czego jeszcze nie robimy

W module zerowym nie kodujemy korpusu i nie budujemy książki kodowej. Pracujemy
na krótkiej mini-transkrypcji utworzonej do ćwiczenia. Nie uczymy się składni
Pythona, nazw typów danych ani gramatyki komunikatów błędów. Kod jest widocznym
wykonaniem procedury: uczestnik ma umieć powiedzieć, po co procedura istnieje,
co powinna zachować, co można sprawdzić automatycznie i co nadal wymaga osądu
badacza.

Nie używamy klucza Gemini API. Kod powstaje w zintegrowanym panelu AI Colaba i
jest wklejany do jednej wskazanej komórki. Notebook zawiera też przygotowane
rozwiązanie awaryjne, więc można ukończyć ćwiczenie, gdy funkcja AI nie jest
dostępna.

Ten sam podział obowiązuje w głównej części Vibe Coding: kod nadal powstaje w
czacie Colaba, natomiast API służy wyłącznie do analizy ograniczonego pakietu
materiału. Jeden formularz przełącza Gemini i OpenAI bez zmiany dalszych
komórek; dostępny jest też bezkosztowy tryb `mock`. Wywołania API są domyślnie
wyłączone i wymagają jawnej zgody uczestnika.

## Dane i prywatność

Do panelu Gemini w tym module przekazujemy wyłącznie mini-transkrypcję
ćwiczeniową, a nie warsztatowy korpus PREWORK. Google informuje, że podczas
korzystania z generatywnych funkcji Colaba może zbierać prompty, powiązany kod
i wyniki, a część materiału może być przeglądana przez ludzi. Dlatego nie
wklejamy danych osobowych, kluczy API ani niezanonimizowanych transkrypcji.
Zobacz [oficjalne FAQ Colaba](https://research.google.com/colaboratory/faq.html).
