# Model Edena - Symulacja
# Autor: Paweł Leszczyński

import math
import random
import matplotlib.pyplot as plt
import numpy as np

def Eden(num_of_cells):
    # creating a table of zeros for cells - manipulate divisions to "zoom in" on the model
    divisions = math.trunc(num_of_cells/70)
    cell_table = np.zeros((math.trunc(divisions), math.trunc(divisions)), dtype=int)
    # inserting a starting cell at the table center
    cell_table[math.trunc(len(cell_table)/2)][math.trunc(len(cell_table)/2)] = 1
    for i in range(1, num_of_cells):
        # table used to store cells that are avaliable to "plant" next cell
        avaliable_cells = []

        # cell picked randomly from avaliable cells
        picked_cell = []

        # using enumerate to get indexes of available cells
        for (index1, cell1) in enumerate(cell_table):
            for (index2, cell2) in enumerate(cell_table[index1]):
                if cell2 == 1:  # check if neighbouring cells are alive or not
                    if cell_table[index1][index2 + 1] == 0:
                        avaliable_cells.append([index1, index2 + 1])
                    if cell_table[index1][index2 - 1] == 0:
                        avaliable_cells.append([index1, index2 - 1])
                    if cell_table[index1 + 1][index2] == 0:
                        avaliable_cells.append([index1 + 1, index2])
                    if cell_table[index1 - 1][index2] == 0:
                        avaliable_cells.append([index1 - 1, index2])

        # picking a random cell from a list of avaliable cells
        picked_cell = random.choice(avaliable_cells)
        # inserting picked cell into a table of living cells
        cell_table[picked_cell[0]][picked_cell[1]] = 1

    #Searching for cluster's endpoints to calculate the diameter

    end_up = False
    end_down = False
    x_index_up = 0
    x_index_down = 0
    y_index_left = len(cell_table)
    y_index_right = 0

    # Up
    for (index_1, cell_1) in enumerate(cell_table):
        if end_up:
            break
        for (index_2, cell_2) in enumerate (cell_table[index_1]):
            if cell_2 == 1:
                x_index_up = index_1
                end_up = True
                break
    # Down
    for (index_1, cell_1) in enumerate(cell_table):
        if end_down:
            break
        for (index_2, cell_2) in enumerate(cell_table[-index_1]):
            if cell_2 == 1:
                x_index_down = -index_1 % len(cell_table)
                end_down = True
                break
    # Left & Right
    for (index_1, cell_1) in enumerate(cell_table):
        for (index_2, cell_2) in enumerate(cell_table[index_1]):
            if cell_2 == 1:
                if index_2 < y_index_left:
                    y_index_left = index_2
                if index_2 > y_index_right:
                    y_index_right = index_2

    radius = max((x_index_down-x_index_up), (y_index_right-y_index_left))/2
    print(radius)

    # Drawing
    plt.imshow(cell_table)
    plt.axis('off')
    plt.title("Model Edena dla %1.0f cząsteczek" % num_of_cells)
    plt.show()


Eden(10000)
