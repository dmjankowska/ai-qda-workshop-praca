# Soczewka Kodowania Korpusu PREWORK

## Logika Trzech Przejść

1. **Oznacz relewantny fragment.** Najpierw wskaż dokładne zdania, w których
   uczestnik mówi o doświadczeniu prekaryjnym albo o jego związku z pracą,
   biografią, sprawstwem, zasobami lub zaangażowaniem.
2. **Zakoduj opisowo.** Kod D odpowiada na pytanie: **„O czym mówi ten
   fragment?”**. Jest krótką, gerundialną i procesualną parafrazą bliską danym.
   Nie ma osobnej definicji ani kryteriów: jego znaczenie tworzą nazwa, cytat i
   memo przypisania.
3. **Koduj na wyższych poziomach.** Kod F odpowiada na pytanie: **„Jaki
   ważniejszy wzorzec, mechanizm, proces, relację lub kategorię analityczną
   reprezentują te obserwacje?”**. Jest selektywny i syntetyzujący znaczenia
   obserwacji (nie oparty na danych syntetycznych), ale nadal
   zakotwiczony w kodach D i ich fragmentach. F otrzymuje uzasadnienie
   analityczne, granicę i przypadki negatywne. Pełne definicje oraz kryteria
   włączenia i wyłączenia powstają dopiero w operacyjnych kartach S.

## Co Jest Relewantne

Soczewka obejmuje doświadczenia niepewności zatrudnienia, dochodu, czasu pracy,
praw i kontroli nad pracą; bezrobocie i przejścia zawodowe; interpretowanie
kariery i przyszłości; indywidualne i zbiorowe odpowiedzi; mobilizowanie więzi
i zasobów; konsekwencje dla życia poza pracą; oraz aktywność obywatelską, jeśli
tekst wiąże ją z doświadczeniem prekaryjności.

Nie trzeba użyć słowa „prekaryjność”. Relewantna może być konkretna sytuacja,
ocena, konsekwencja, strategia lub ograniczenie. Relewantne są też kontrasty:
stabilność, poczucie bezpieczeństwa albo brak oczekiwanego związku, jeśli
odnoszą się do problemu badawczego.

Nie koduj automatycznie całej biografii. Ogólna informacja o rodzinie,
edukacji, hobby, poglądach lub pracy pozostaje poza analizą, dopóki fragment
nie wnosi czegoś do problemu PREWORK. Pytania prowadzącego, potwierdzenia i
noty techniczne nie są doświadczeniami uczestnika.

## Dyscyplina Interpretacji

- Soczewka problemu badawczego wybiera materiał, ale nie dostarcza gotowych
  kodów ani oczekiwanego mechanizmu.
- Najmniejszą jednostką decyzji jest wskazany fragment zdań, nie cała tura.
  Jedna dłuższa wypowiedź może zawierać kilka kodów D albo tylko jeden krótki
  fragment relewantny.
- Kod D nie powinien być szerszy niż cytat i nie powinien brzmieć bardziej
  akademicko niż dane. Nazwa jest procesualną parafrazą, nie mini-teorią.
- Kod F musi wnosić zysk analityczny ponad zmianę nazwy kodów D. Podobieństwo
  słów i częstość pomagają wybrać materiał do porównania, ale nie uzasadniają
  kategorii.
- Jeżeli relewancja fragmentu albo wspólny sens kodów pozostaje niejasny,
  zachowaj identyfikator i ustaw `needs_review`. Nie twórz kategorii-worka dla
  domknięcia tabeli.
- Każda decyzja ma pozostać odtwarzalna przez `interview_id`, `turn_id`,
  `sentence_id`, cytat i offsety. Kontekst przypadku pomaga interpretować, lecz
  sam nie jest dowodem kodu.
