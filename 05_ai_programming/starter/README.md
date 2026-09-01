# Fallback: Walidator Książki

Ten skrypt jest gotowym punktem startowym, gdy grupa utknie podczas pracy z
Codexem. Sprawdza podstawowy kontrakt `T -> S -> F -> D`.

```bash
python 05_ai_programming/starter/validate_codebook.py \
  01_data/codebook/codebook_prekariat_final.csv
```

Po rozpakowaniu handoffu ten sam skrypt możesz uruchomić na własnym wyniku:

```bash
python 05_ai_programming/starter/validate_codebook.py \
  06_outputs/uczestnicy/AI_QDA_Workshop/04_candidate_codebook.csv
```

Najpierw uruchom go bez zmian. Potem poproś Codexa o jedną małą modyfikację,
korzystając z gotowego punktu rozszerzenia
`find_unmapped_candidate_codes` i testu w `tests/`.

1. Opisz kontrakt funkcji bez składni Pythona: wejście, wynik, przypadek
   zwykły i brzegowy oraz zakaz przypisywania rodzica.
2. Poproś Codexa o implementację tylko tej funkcji i usunięcie dekoratora
   `skip` z jednego testu.
3. Uruchom `python -m unittest discover -s 05_ai_programming/starter/tests`.
4. Przeczytaj rekordy wskazane przez funkcję. Test nie ocenia trafności
   interpretacji i nie może zmienić `candidate` na `accepted`.
