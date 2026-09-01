# Progresja: Od Promptu I MAXQDA Do Pipeline'u

Uczestnicy mają już dwa doświadczenia: książkę dla sampla tworzoną w rozmowie
z AI oraz kodowanie korpusu w MAXQDA. Vibe Coding nie powtarza tych zadań.
Przesuwa pytanie z „czy AI potrafi kodować?” na „jak zapisać i sprawdzić
kolejne decyzje jako powtarzalny proces?”.

## Od Rezultatu Do Mechanizmu

Moduł zaczyna się od pełnego wyniku: książki `T -> S -> F -> D`, jednej
prześledzonej gałęzi i grafu relacji F-F/T-T. Następnie uczestnicy odtwarzają
podstawową logikę na trzech wywiadach:

```text
zobacz rezultat
  -> nazwij cel i potrzebną procedurę
  -> zapisz wejścia, artefakt, kontrolę i decyzję badacza
  -> zachowaj strukturę tekstu
  -> wybierz relewantne fragmenty i utwórz D
  -> porównaj D i utwórz F
  -> zbuduj operacyjne S i oszczędne T
  -> zwaliduj lokalnie z Codexem
```

## Co Zmienia Się Między Blokami

| Blok | Dominujące pytanie | Produkt |
| --- | --- | --- |
| Moduł zerowy | Jak uruchomić, sprawdzić i trwale zapisać mały krok napisany z Gemini? | Prywatne repo z szablonu, dwa notebooki, testy oraz osobne commity produktów i notebooka. |
| AI Prompting | Jak sformułować dobre zadanie analityczne? | Prompt i robocze kody dla próbki. |
| MAXQDA | Jak kodować i porównywać propozycje w CAQDAS? | System kodów, memos i doświadczenie kontroli. |
| Vibe Coding | Jak w czacie Colaba zamienić procedury w małe funkcje, a przez API porównać decyzje analityczne? | Podstawowy pipeline sample i książka T-S-F-D. |
| Codex | Jak uruchomić, zwalidować i zmienić projekt lokalnie? | Test, jedna zmiana, konfiguracja i commit. |

## Schemat Uczenia

Każdy blok zachowuje cykl z `resources/LS CAQDAS - Schemat uczenia.md`: cel,
pierwsza próba, demonstracja, zadanie, prezentacja, feedback, poprawa i
transfer. Demonstracja pokazuje tylko artefakt potrzebny do bieżącego kroku,
nie całe zaplecze autorskie.

## Warsztat A Skalowanie

Na zajęciach priorytetem jest szybka pętla: instrukcja i kod w czacie Colaba,
dwa synchroniczne wywołania analityczne przez wymienny adapter API oraz mały
sample. Pełny przebieg wymaga innych kompromisów:
retrievalu, harmonizacji, checkpointów, pracy asynchronicznej, kosztowych
limitów i głębszego audytu. Uczestnik rozumie ich funkcję, ale ich nie
implementuje ani nie otrzymuje dostrojonego generatora.

Rozwiązania skalujące są omawiane dopiero po zrozumieniu podstawowego
workflow. Embeddingi pomagają dobrać kandydatów do porównania, cache ogranicza
powtarzanie kosztownych obliczeń, Flex i wykonanie asynchroniczne zmieniają
koszt oraz czas oczekiwania, a checkpointy pozwalają wznowić przebieg. Żaden z
tych mechanizmów nie rozstrzyga relewancji, trafności kodu ani granic kategorii.

## Most Do Myślenia Agentowego

Po czterech etapach można nazwać role przyszłego workflow: `Corpus Loader`,
`Unitizer`, `Relevance Selector`, `Descriptive Coder`, `Category Curator`,
`Evidence Checker`, `Human Review Gate`, `Audit Reporter` i `Exporter`.
Najważniejsze nie jest mnożenie agentów, tylko jawne wejścia, wyjścia,
walidacje oraz decyzje, które pozostają po stronie badacza.
