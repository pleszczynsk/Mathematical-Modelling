# Model DLA - Symulacja
# Autor: Paweł Leszczyński
# Inspiracja: DLA Cluster autorstwa OrionPaxxx:
# https://github.com/OrionPaxxx/computational_physics/blob/master/f/DLA%20cluster.py

import random
import matplotlib.pyplot as plt


class Clusters:
    #Constructor with basic parameters - array size, number of cells, empty table initialization
    def __init__(self, size=800, number=10000):
        self.s = size
        self.n = number
        self._fig = [[0] * self.s for i in range(self.s)]

    def growth(self):
        # Initialize a cluster with a point in the center on the array
        self._fig[int(self.s / 2)][int(self.s / 2)] = 1
        counter = 0
        # Main loop creating the cluster
        while counter < self.n:
            tempx = random.randint(0, self.s - 1)
            tempy = random.randint(0, self.s - 1)
            if tempx == 0:
                continue
            elif tempx == self.s - 1:
                continue
            elif tempy == 0:
                continue
            elif tempy == self.s - 1:
                continue
            self._fig[tempx][tempy] = 1
            if self._fig[tempx - 1][tempy] == 1:
                continue
            elif self._fig[tempx + 1][tempy] == 1:
                continue
            elif self._fig[tempx][tempy - 1] == 1:
                continue
            elif self._fig[tempx][tempy + 1] == 1:
                continue
            # Walk
            while True:
                self._fig[tempx][tempy] = 0
                temp = random.random()
                if temp < 0.25:
                    tempx -= 1
                elif 0.25 < temp < 0.5:
                    tempy -= 1
                elif 0.5 < temp < 0.75:
                    tempx += 1
                elif temp > 0.75:
                    tempy += 1
                self._fig[tempx][tempy] = 1

                if tempx == 0:
                    self._fig[tempx][tempy] = 0
                    break
                elif tempx == self.s - 1:
                    self._fig[tempx][tempy] = 0
                    break
                elif tempy == 0:
                    self._fig[tempx][tempy] = 0
                    break
                elif tempy == self.s - 1:
                    self._fig[tempx][tempy] = 0
                    break

                if self._fig[tempx - 1][tempy] == 1:
                    counter += 1
                    break
                elif self._fig[tempx + 1][tempy] == 1:
                    counter += 1
                    break
                elif self._fig[tempx][tempy - 1] == 1:
                    counter += 1
                    break
                elif self._fig[tempx][tempy + 1] == 1:
                    counter += 1
                    break

        # Searching for cluster's endpoints to calculate the radius

        end_up = False
        end_down = False
        x_index_up = 0
        x_index_down = 0
        y_index_left = len(self._fig)
        y_index_right = 0

        # Up
        for (index_1, cell_1) in enumerate(self._fig):
            if end_up:
                break
            for (index_2, cell_2) in enumerate(self._fig[index_1]):
                if cell_2 == 1:
                    x_index_up = index_1
                    end_up = True
                    break
        # Down
        for (index_1, cell_1) in enumerate(self._fig):
            if end_down:
                break
            for (index_2, cell_2) in enumerate(self._fig[-index_1]):
                if cell_2 == 1:
                    x_index_down = -index_1 % len(self._fig)
                    end_down = True
                    break
        # Left & Right
        for (index_1, cell_1) in enumerate(self._fig):
            for (index_2, cell_2) in enumerate(self._fig[index_1]):
                if cell_2 == 1:
                    if index_2 < y_index_left:
                        y_index_left = index_2
                    if index_2 > y_index_right:
                        y_index_right = index_2
        radius = max((x_index_down - x_index_up), (y_index_right - y_index_left))/2
        print(radius)

    def show(self):
        for i in range(self.s):
            for j in range(self.s):
                if self._fig[i][j] == 1:
                    plt.plot(i, j, 'g.')
                    plt.xlim(0, self.s)
                    plt.ylim(0, self.s)
        plt.grid(False)
        plt.axis('off')
        plt.title('Zlepek DLA dla %.f cząsteczek' % self.n)
        plt.show()


a = Clusters()
a.growth()
a.show()
