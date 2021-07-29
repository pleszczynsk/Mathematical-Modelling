#   Autor- Paweł Leszczyński
#   Inspiracja - #1 Wykład 'Jak znaleźć liczbę 𝛑 (pi) na ulicy?': https://www.youtube.com/watch?v=tisBkdxzM94
#                #2 GeeksforGeeks, 'Estimating the value of Pi using Monte Carlo': https://www.geeksforgeeks.org/estimating-value-pi-using-monte-carlo/

import random
import matplotlib.pyplot as plt
from math import pi

INTERVAL = range(1, 100, 1)
tab_pi = []
for i in INTERVAL:
    circle_points = 0
    square_points = 0
    for j in range(i ** 2): # N = possible x values * possible y values
        rand_x = random.uniform(-1, 1)
        rand_y = random.uniform(-1, 1)
        # Distance of (x,y) from origin using circle equation
        origin_dist = rand_x ** 2 + rand_y ** 2
        if origin_dist <= 1:
            circle_points += 1
        square_points += 1
    tab_pi.append([square_points, (abs(pi-(4 * circle_points / square_points))/pi)])
plt.figure()
plt.title('Wykres błędu otrzymanego przybliżenia od liczby N')
plt.xlabel('N')
plt.ylabel('Błąd względny przybliżenia')
plt.plot(*zip(*tab_pi))
plt.plot()
plt.show()
