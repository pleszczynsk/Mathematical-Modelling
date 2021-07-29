import random
import numpy

def spacer_losowy1d(liczba_krokow):
    x = 0
    for i in range(liczba_krokow):
        x += random.randint(-1, 1)
    if x == 0:
        return True


def spacer_losowy2d(liczba_krokow):
    x = 0
    y = 0
    for i in range(liczba_krokow):
        x += random.randint(-1, 1)
        y += random.randint(-1, 1)
    if x == 0 and y == 0:
        return True
    else:
        return False


def spacer_losowy3d(liczba_krokow):
    x = 0
    y = 0
    z = 0
    for i in range(liczba_krokow):
        x += random.randint(-1, 1)
        y += random.randint(-1, 1)
        z += random.randint(-1, 1)
    if x == 0 and y == 0 and z == 0:
        return True
    else:
        return False


def prawdopodobienstwo_spacerowe(ilosc_probek):
    d1 = 0
    d2 = 0
    d3 = 0
    for i in range(ilosc_probek):
        if spacer_losowy1d(1000):
            d1 += 1
        if spacer_losowy2d(1000):
            d2 += 1
        if spacer_losowy3d(1000):
            d3 += 1
    print("Prawdopodobieństwa powrotu do początku:\n1D: ",numpy.divide(d1,ilosc_probek),"\n2D: ",numpy.divide(d2,ilosc_probek),"\n3D: ",numpy.divide(d3,ilosc_probek))


prawdopodobienstwo_spacerowe(100000)
