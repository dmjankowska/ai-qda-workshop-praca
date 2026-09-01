# Ćwiczenia: GitHub, Colab i Gemini

## Ćwiczenie 1: znajdź swoje miejsce pracy

1. Otwórz swoje prywatne repo i publiczny wzorzec w dwóch kartach.
2. Wskaż właściciela każdego repozytorium.
3. Otwórz historię commitów w prywatnym repo.
4. Dokończ zdanie: „commit zapisuje ..., ale nie zapisuje ...”.

**Kontrola:** potrafisz wrócić do strony prywatnego repo bez linku od
prowadzącego.

## Ćwiczenie 2: nazwij potrzebną procedurę

W notebooku 00 wybierz jedną sytuację z pracy badawczej:

- chcesz podzielić rozmowę na jednostki, zachowując kolejność, źródło i
  dokładny tekst;
- chcesz oznaczyć przypadki niejednoznaczne, które badacz powinien obejrzeć;
- chcesz ustalić, które wywiady przeszły dany etap, a które jeszcze nie.

Nie proponuj kodu. Opisz:

1. problem, który procedura ma rozwiązać;
2. materiał wejściowy;
3. rezultat, który ma być widoczny po jej wykonaniu;
4. warunki możliwe do sprawdzenia automatycznie;
5. decyzję, której nie należy oddawać programowi.

**Kontrola:** inna osoba potrafi na podstawie opisu powiedzieć, czemu służy
procedura, choć nie zna Pythona.

## Ćwiczenie 3: od procedury do jednej funkcji

Otwórz notebook 01. Najpierw obejrzyj mini-transkrypcję i nazwij najważniejsze
ryzyko przygotowania jej do dalszego kodowania. Następnie uzupełnij kartę
procedury zwykłym językiem.

Przygotowana komórka Colaba dołączy informacje implementacyjne, takie jak
nazwa funkcji i układ tabeli. Porównaj dwie części powstałego promptu:

- **Twoją część:** cel, rezultat, warunki kontroli i granice automatyzacji;
- **część techniczną:** interfejs potrzebny, aby funkcja pasowała do notebooka.

Przekaż cały prompt Gemini, poproś o jedną funkcję i wklej ją do wskazanej
komórki. Uruchom przygotowaną listę kontroli.

Jeżeli któraś kontrola nie przechodzi, nie diagnozuj składni. Przekaż Gemini:

```text
Oto kontrakt procedury, kod funkcji oraz lista kontroli z jednym nieudanym
warunkiem. Popraw tylko tę funkcję. Nie zmieniaj danych ani kontroli. Najpierw
nazwij, którego wymagania procedura nie spełnia, a potem zwróć pełny kod.
```

**Kontrola:** tekst i kolejność źródłowa pozostają niezmienione, każda jednostka
ma stabilny identyfikator, a niejednoznaczna etykieta trafia do przeglądu.

## Ćwiczenie 4: zmień wymaganie, nie buduj nowego projektu

Porównaj dwa sposoby obsługi nieznanej etykiety mówcy:

- program automatycznie uznaje ją za wypowiedź uczestnika;
- program zapisuje `needs_review` i pozostawia rozstrzygnięcie badaczowi.

Wybierz rozwiązanie adekwatne do celu kodowania i uzasadnij wybór. Następnie
zmień w karcie procedury tylko to jedno wymaganie, poproś Gemini o odpowiednią
aktualizację funkcji i ponownie obejrzyj wynik kontroli.

**Decyzja badacza:** zapisz, jakie informacje byłyby potrzebne, aby później
rozstrzygnąć niejednoznaczną etykietę w całym korpusie. Zielona kontrola
techniczna nie rozstrzyga, która interpretacja mówcy jest trafna.

## Ćwiczenie 5: zapis i commit

1. Uruchom notebook od początku.
2. Obejrzyj zapisane tabele i decyzje badacza.
3. Ustaw `PUBLISH_RESULTS_TO_GITHUB=True` i sprawdź status `pushed` albo
   `up_to_date`.
4. Zapisz kopię notebooka w prywatnym repo przez
   **Plik -> Zapisz kopię w GitHubie**.
5. Na GitHubie znajdź produkty w `00_github_colab/outputs/`, notebook oraz oba
   commity.

**Exit ticket:** wskaż jeden element, który powinien znaleźć się w Git, jeden
pełny log API pozostający domyślnie poza repozytorium oraz jedną decyzję,
której nie można zastąpić kontrolą techniczną.
