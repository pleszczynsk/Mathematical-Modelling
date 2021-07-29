# Modele Matematyczne

### #4 - Symulacja epidemii - model SIR

#### Python

*Prosty model epidemii*
*Model składa się z N osób w jednym z trzech stanów zarażone (I), narażone na zarażenie (S) oraz ozdrowieńcy (R). Osoby poruszają się np. w spacerze losowym lub po trajektoriach prostych. W jednostce czasu mogą one zmienić swój stan:- S→I w przypadku kontaktu (kolizja lub mała odległość) z prawdopodobieństwem p1- I→R z prawdopodobieństwem p2.*

##### Scenariusz:

Testy zostały przeprowadzone na 1000 obiektach ("osobach")  rozproszonych i poruszających się losowo po powierzchni 20x20 jednostek. W pierwszym kroku zostaje zarażona losowa "osoba", symulacja kończy się po czasie 100 kroków.

##### Uwagi:

- Jednostki oznaczone jako martwe nadal poruszają się w symulacji - są jednak wyłączone z wszelkiej interakcji z innymi jednostkami. Uznałem, iż szkoda zasobów na dodatkowe sprawdzanie w funkcji ruchu czy jednostka jest martwa, zwłaszcza że zmiana byłaby stricte kosmetyczna.
- Wykresy R są oznaczone jako "zmarli" - mogą oczywiście również oznaczać tych którzy wypracowali odporność na zagrożenie.

Wyniki, w zależności od przyjętych prawdopodobieństw każdego stanu, dostępne w plikach 1-4.png, animacje symulacji dostępne w plikach .mp4 . Porównanie z danymi z Wikipedii dostępne w plikach wiki.png oraz sym_wiki.png .