#   Autor- Paweł Leszczyński
#   Inspiracja - #1 Wykład 'Jak znaleźć liczbę 𝛑 (pi) na ulicy?': https://www.youtube.com/watch?v=tisBkdxzM94
#                #2 GeeksforGeeks, 'Estimating the value of Pi using Monte Carlo': https://www.geeksforgeeks.org/estimating-value-pi-using-monte-carlo/

import random

INTERVAL = 1000

circle_points = 0
square_points = 0
for i in range(INTERVAL ** 2): # N = possible x values * possible y values
    rand_x = random.uniform(-1, 1)
    rand_y = random.uniform(-1, 1)
    # Distance of (x,y) from origin using circle equation
    origin_dist = rand_x ** 2 + rand_y ** 2
    if origin_dist <= 1:
        circle_points += 1
    square_points += 1
pi = 4 * circle_points / square_points

print("Przybliżenie liczby pi przy N = %i : " %square_points, pi)
print("Dokładne przybliżenie liczby Pi do porównania: 3.14159265359")