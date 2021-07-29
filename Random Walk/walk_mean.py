import random
import numpy
import matplotlib.pyplot as plt
from collections import Counter


def spacer_losowy1d(liczba_krokow):
    x = 0
    tab_1d = [x]
    for i in range(liczba_krokow):
        x += random.randint(-1, 1)
        tab_1d.append(x)
    return abs(tab_1d[-1])  # ostatni element listy, w jakiej odległości było od punktu początkowego


def srednia_spacerowa(ilosc_probek):
    tab_dane = []
    for i in range(ilosc_probek):
        print(i)
        tab_dane.append(spacer_losowy1d(1000))
    w = Counter(tab_dane)
    plt.bar(w.keys(), w.values())
    plt.title("Histogram końcowych odległości spacerów 1D o tysiącu krokach\n - dla %1.0f spacerów" % ilosc_probek)
    plt.xlabel("Końcowe odległości spacerów (wartość bezwzględna współrzędnej x)")
    plt.ylabel("Ilość spacerów kończących się daną odległością w próbie")
    plt.show()


srednia_spacerowa(100000)