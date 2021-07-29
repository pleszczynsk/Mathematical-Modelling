# Autor - Paweł Leszczyński
import random
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt


def spacer_losowy3d(liczba_krokow):
    x = 0
    y = 0
    z = 0
    tab_3d_x = [x]
    tab_3d_y = [y]
    tab_3d_z = [z]
    for i in range(liczba_krokow):
        x += random.randint(-1, 1)
        y += random.randint(-1, 1)
        z += random.randint(-1, 1)
        tab_3d_x.append(x)
        tab_3d_y.append(y)
        tab_3d_z.append(z)

    ax = plt.axes(projection='3d')
    ax.plot3D(tab_3d_x, tab_3d_y, tab_3d_z, linewidth=0.5)
    ax.text(0, 0, 0, ". Początek", color="black")
    ax.set_xlabel("Współrzędna x")
    ax.set_ylabel("Współrzędna y")
    ax.set_zlabel("Współrzędna z")
    plt.show()


spacer_losowy3d(10000)
