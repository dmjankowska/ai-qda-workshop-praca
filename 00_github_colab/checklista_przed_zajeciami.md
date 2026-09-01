# Checklista Przed Zajęciami

Przeznacz na nią 20-30 minut przed spotkaniem. Nie pracujesz jeszcze z danymi
badawczymi.

Jeżeli przygotowujesz środowisko po raz pierwszy, zacznij od pełnego
[handoutu przedwarsztatowego](../handout_przedwarsztatowy.md). Ta strona jest
jego skróconą kontrolą końcową.

## Konto GitHub

- zaloguj się lub utwórz konto;
- potwierdź adres e-mail;
- otwórz repozytorium `caqdastm/ai_qda-workshop-1u`;
- wybierz **Use this template** i utwórz nowe repo z widocznością **Private**;
- utwórz ograniczony fine-grained token z dostępem wyłącznie do tego repo i
  uprawnieniem **Contents: Read and write**.

## Konto Google I Colab

- zaloguj się na konto Google;
- otwórz [Google Colab](https://colab.research.google.com/);
- sprawdź, czy możesz utworzyć pusty notebook i uruchomić `print("OK")`;
- sprawdź, czy w interfejsie notebooka widzisz ikonę Gemini lub panel AI.
- dodaj w Colab Secrets `AI_QDA_REPOSITORY` w formacie `login/nazwa-repo` oraz
  `GITHUB_TOKEN`; włącz ich dostęp dla notebooka startowego.

Dostęp do funkcji AI zależy między innymi od wieku konta i dostępności usługi.
Brak panelu Gemini nie blokuje warsztatu: notebook 01 ma rozwiązanie bazowe,
a kod można też uzyskać w zwykłym czacie Gemini.

## Jeżeli Bierzesz Udział W Vibe Codingu

- przygotuj co najmniej jeden klucz: `GEMINI_API_KEY` albo `OPENAI_API_KEY`;
  jeżeli nie chcesz używać API, wybierz podczas zajęć tryb `mock`;
- nie wpisuj klucza do komórki — dodaj go pod właściwą nazwą w Colab
  `Secrets`;
- wybór Gemini/OpenAI zmienia się w jednym formularzu i nie wymaga zmiany
  dalszych komórek; przy OpenAI zdecydujesz też o wartości `store`;
- tryb `mock` sprawdza przepływ i testy, ale nie tworzy wyniku analitycznego;
- wywołania API uruchamiaj dopiero po sprawdzeniu limitu wywołań i zaznaczeniu
  jawnej zgody w notebooku.

## Bezpieczeństwo

- nie wklejaj do Gemini kluczy API ani danych logowania;
- nie wpisuj `GITHUB_TOKEN` do komórki, promptu, adresu repo ani commita;
- podczas modułu zerowego używaj wyłącznie mini-transkrypcji ćwiczeniowej z notebooka;
- upewnij się, że komórka infrastruktury pokazuje tryb
  `participant_repository`, nie `public_demo`;
- po warsztacie możesz unieważnić token bez usuwania prywatnego repo i jego historii.

Zgłoś prowadzącemu przed zajęciami, jeśli nie możesz wykonać któregoś z tych
kroków.
