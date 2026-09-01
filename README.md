# AI QDA Workshop

Publiczne materiały dla osób uczestniczących w warsztacie wykorzystania AI i
dużych modeli językowych w jakościowej analizie danych. Warsztat pokazuje
cztery sposoby organizowania i wspierania tego samego procesu kodowania: od
kontrolowanej rozmowy z modelem, przez pracę w programie CAQDAS, po
prototypowanie prostego workflow i jego lokalne uruchomienie.

Pełny układ zajęć znajduje się w
[`harmonogram_warsztatu_AI_QDA.md`](harmonogram_warsztatu_AI_QDA.md).

## Zacznij tutaj

1. Co najmniej dzień przed zajęciami wykonaj
   [`handout przedwarsztatowy`](handout_przedwarsztatowy.md).
2. Na końcu sprawdź krótką
   [`checklistę techniczną`](00_github_colab/checklista_przed_zajeciami.md).
3. Utwórz z tego publicznego wzorca własne repo przez **Use this template** i
   ustaw jego widoczność na **Private**.
4. Skonfiguruj dwa sekrety Colaba: `AI_QDA_REPOSITORY` oraz `GITHUB_TOKEN`,
   zgodnie z
   [`instrukcją prywatnego workspace`](00_github_colab/instrukcja_konto_fork_colab.md).
5. Jeżeli nie znasz GitHuba lub Colaba, zacznij od
   [`00_github_colab/`](00_github_colab/).
6. Opis i materiały wspólnego korpusu znajdują się w
   [`01_data/prekariat/`](01_data/prekariat/).
7. Przed częścią Vibe Coding obejrzyj
   [referencyjną książkę kodową i graf relacji](01_data/codebook/).

Publiczne repo jest czystym wzorcem. Notebooki zapisują sprawdzone produkty do
`outputs/` w prywatnym repo uczestnika. Kolejny notebook może dzięki temu
odczytać wyniki poprzedniego po uruchomieniu w świeżym runtime Colaba, a Codex
może później pracować na lokalnym klonie tej samej historii.

## Cztery ścieżki pracy

| Ścieżka | Środowisko | Na czym polega praca badacza | Rola AI | Główny rezultat |
| --- | --- | --- | --- | --- |
| 1. AI Prompting for QDA | ChatGPT lub Gemini | Badacz definiuje problem, jednostkę analizy, kontekst, kolejne kroki instrukcji, format odpowiedzi i kryteria oceny. | Model odpowiada na kontrolowane instrukcje i proponuje kandydackie rezultaty wymagające oceny. | Sprawdzony prompt analityczny, procedura pracy na próbce i kryteria oceny odpowiedzi AI. |
| 2. AI-assisted QDA Coding | MAXQDA z funkcjami AI oraz ChatGPT | Badacz pracuje z segmentami korpusu, porównuje kodowanie człowieka i AI, rozwija system kodów i zapisuje memos. | AI wspiera kodowanie i porządkowanie materiału, ale nie zatwierdza kodów ani interpretacji. | Zakodowany projekt MAXQDA, uporządkowany system kodów, memos i decyzje badacza. |
| [3. Vibe Coding for QDA](04_vibe_coding/) | Google Colab, Gemini i prywatne repo GitHub | Badacz przekłada procedurę analityczną na dane wejściowe, wyniki, etapy, kontrole i punkty decyzyjne. Na próbce buduje małe fragmenty kodu oraz zapisuje kolejne artefakty. | Czat pomaga tworzyć uruchamialny kod. Wyniki modelu pozostają propozycjami do przeglądu. | Prototyp workflow na próbce, trwałe produkty etapów, proste statystyki i porównanie z wynikiem pełnego korpusu. |
| [4. AI Programming for QDA](05_ai_programming/) | Prywatne repo, Codex i Python | Badacz klonuje własną pracę, poznaje strukturę projektu, uruchamia walidator i wykonuje jedną kontrolowaną zmianę. | Codex pomaga czytać pliki, uruchamiać testy i implementować zmianę według kontraktu. | Walidacja wyniku, prosty test, commit i zrozumienie możliwości dalszego rozwoju. |

Każda ścieżka pracuje na tym samym problemie badawczym i rozwijanej książce
kodowej, ale inaczej rozkłada pracę między badacza, model i oprogramowanie.
Kontrola techniczna nie oznacza, że kod lub kategoria są trafne analitycznie.

## Otwórz notebooki w Colabie

[![Notebook 00: start](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/caqdastm/ai_qda-workshop-1u/blob/main/00_github_colab/00_start_here_github_colab.ipynb)
[![Notebook 01: Gemini](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/caqdastm/ai_qda-workshop-1u/blob/main/00_github_colab/01_colab_gemini_vibe_coding.ipynb)

[![Vibe 1: jednostki tekstu](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/caqdastm/ai_qda-workshop-1u/blob/main/04_vibe_coding/01_od_transkrypcji_do_jednostek.ipynb)
[![Vibe 2: kodowanie opisowe](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/caqdastm/ai_qda-workshop-1u/blob/main/04_vibe_coding/02_od_relewantnego_fragmentu_do_kodu_D.ipynb)
[![Vibe 3: kodowanie zogniskowane](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/caqdastm/ai_qda-workshop-1u/blob/main/04_vibe_coding/03_od_kodow_D_do_wzorcow_F.ipynb)
[![Vibe 4: książka kodowa](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/caqdastm/ai_qda-workshop-1u/blob/main/04_vibe_coding/04_od_wzorcow_do_ksiazki_TSFD.ipynb)

Odznaki zawsze otwierają publiczny wzorzec. Do właściwej pracy otwieraj
notebook z prywatnego repo przez **Plik → Otwórz notatnik → GitHub**. Komórka
GitHub publikuje wybrane produkty, natomiast zmieniony notebook zapisujesz
osobno przez **Plik → Zapisz kopię w GitHubie**.

## Struktura repozytorium

```text
00_github_colab/          wprowadzenie oraz outputs pierwszych procedur
01_data/                  wspólny korpus i referencyjna książka kodowa
02_ai_prompting/          miejsce na materiały AI Prompting for QDA
03_ai_assisted_coding/    miejsce na materiały AI-assisted QDA Coding
04_vibe_coding/           notebooki, helper i trwałe outputs etapów 01-04
05_ai_programming/        wprowadzenie do Codexa, walidatora i testów
06_outputs/               dodatkowe wyniki pracy grupowej
```

Materiały do ścieżek `02` i `03` zostaną uzupełnione po synchronizacji części
przygotowywanej przez współautora.

## Zasady pracy

- Nie nadpisuj danych źródłowych w `01_data/`.
- Najpierw uruchamiaj kod na małej próbce i czytaj wynik.
- Publikuj tylko sprawdzone produkty z katalogów `outputs/` prywatnego repo.
- Pełne logi `*_prompt_runs.jsonl` pozostaw domyślnie poza commitem.
- Nie umieszczaj w Git kluczy API, haseł, tokenów ani danych wrażliwych.
- Traktuj wyniki AI jako propozycje. O trafności kodu i kategorii decyduje badacz.

Repozytorium zawiera wyłącznie materiały uczestnika. Kod procedur autorskich,
logi modeli, materiały recenzenckie i pełne zaplecze analityczne nie są tutaj
publikowane.
