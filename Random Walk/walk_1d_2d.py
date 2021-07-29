# Autor - Paweł Leszczyński
import random
import numpy
import matplotlib.pyplot as plt


def spacer_losowy1d(liczba_krokow):
    x = 0
    tab_1d = [x]
    for i in range(liczba_krokow):
        x += random.randint(-1, 1)
        tab_1d.append(x)

    plt.plot(tab_1d, linewidth=0.3)
    plt.xlabel("Liczba kroków")
    plt.ylabel("Współrzędna x")
    plt.title("Spacer losowy 1D - %1.0f kroków" % liczba_krokow)
    plt.show()


def spacer_losowy2d(liczba_krokow):
    x = 0
    y = 0
    tab_2d_x = [x]
    tab_2d_y = [y]
    for i in range(liczba_krokow):
        x += random.randint(-1, 1)
        y += random.randint(-1, 1)
        tab_2d_x.append(x)
        tab_2d_y.append(y)

    plt.plot(tab_2d_x, tab_2d_y, linewidth=0.3)
    plt.annotate(". Początek", (0, 0), color="black")
    plt.xlabel("Współrzędna x")
    plt.ylabel("Współrzędna y")
    plt.title("Spacer losowy 2D - %1.0f kroków" % liczba_krokow)
    plt.show()


spacer_losowy1d(10000)
spacer_losowy2d(10000)
