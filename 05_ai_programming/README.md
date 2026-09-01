# Ścieżka 4: AI Programming For QDA

**Środowisko:** lokalne repozytorium, Codex i Python.

Punktem wejścia jest lokalny klon **prywatnego repo uczestnika**, w którym
notebooki zachowały produkty w `00_github_colab/outputs/` i
`04_vibe_coding/outputs/`. Nie zaczynaj tej części od czystego publicznego
wzorca, ponieważ nie zawiera on decyzji ani kandydackiej książki danej osoby.

Ta część nie buduje drugiego pipeline'u. Uczestnik bierze cztery karty
procedur i kandydackie artefakty z Vibe Codingu, odtwarza ich zależności,
sprawdza kontrakty oraz wykonuje jedną małą, testowalną zmianę z Codexem.

To nadal warsztat o kodowaniu AI_QDA: adaptujemy sposób wyboru jednostek,
kodowania D, budowy F/S/T i kontroli śladu w danych. Nie przenosimy do niego
celów ani produktów analizy tematycznej. Wspólna z drugim warsztatem jest
struktura uczenia: badacz opisuje model i cel, model proponuje kod, test
sprawdza zachowanie techniczne, a badacz ocenia sens analityczny.

## Cel 4 Godzin

Po bloku uczestnik potrafi:

- wskazać zależności między plikami procesu;
- zwalidować hierarchię `T -> S -> F -> D` i ślad cytatów;
- odróżnić wynik sample od referencyjnego full;
- rozpoznać potrzebną procedurę przed nazwaniem zmiany technicznej;
- wykonać, sprawdzić i zapisać małą zmianę w Git;
- rozpisać punkty przyszłego workflow agentowego bez budowania pełnego agenta.

## Przebieg

1. **Inwentaryzacja:** odtwórz z kart i artefaktów przepływ jednostki → D → F → S/T.
2. **Walidacja:** sprawdź ID, rodziców, wymagane pola S, puste definicje D i
   możliwość powrotu od cytatu do tekstu.
3. **Mikrofunkcja:** nazwij problem pipeline'u, opisz potrzebną procedurę,
   poproś Codexa o implementację gotowego punktu rozszerzenia i odblokuj test.
4. **Transfer:** wypełnij brief adaptacji, nazwij role, punkty kontroli badacza
   i zapisz commit.

Pełny scenariusz znajduje się w
[przejscie_z_vibe_coding.md](przejscie_z_vibe_coding.md).
Gdy grupa utknie przy walidatorze, może zacząć od działającego
[fallbacku](starter/README.md) i poprosić Codexa o jedną małą rozbudowę.

**Rezultat:** nie „gotowy system agentowy”, lecz repozytorium, w którym
uczestnik rozumie przepływ danych, potrafi przełożyć cel metodologiczny na
małą funkcjonalność i ma pierwszą zweryfikowaną zmianę lokalną.
