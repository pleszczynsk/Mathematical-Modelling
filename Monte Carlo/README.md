# Modele Matematyczne

### #5 - Monte Carlo

#### Python/C++

#### monte_carlo_pi:

Oblicz przybliżenie liczby 𝛑  z dokładnością przynajmniej do 3. miejsca po przecinku używając algorytmu Monte Carlo.

###### Wynik dla INTERVAL = 1000

``````
Przybliżenie liczby pi przy N = 1000000 :  3.141996
Dokładne przybliżenie liczby Pi do porównania: 3.14159265359
``````

Liczba 𝛑 została obliczona z dokładnością do 3 miejsc po przecinku po zastosowaniu metody Monte Carlo z N = 1.000.000


#### monte_carlo_rounding_error:

Generowanie wykresu błędu otrzymanego przybliżenia w zależności od liczby N. Wynik w pliku .png o tej samej nazwie.

#### monte_carlo_rand(), monte_carlo_random():

Sprawdzenie błędu względnego przybliżenia Monte Carlo pomiędzy Mersenne-Twister z random() Pythona a rand() z C++.
Procedura: Wygenerowanie danych z rand() do pliku .txt (C++) -> wygenerowanie danych z random(), wczytanie pliku z danymi z rand() i porównanie obu na wykresie (Python) 

Wynik w pliku monte_carlo_rands.png



