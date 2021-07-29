#   Autor- Paweł Leszczyński
#   Uwaga: do poprawnego zapisania wizualizacji potrzebna jest biblioteka ffmpeg: https://www.ffmpeg.org/

from random import choice
from random import uniform
from random import random
import matplotlib
from matplotlib import pyplot as plt
from matplotlib import animation
from collections import defaultdict
matplotlib.use('Agg')

# Settings for recording

Writer = animation.writers['ffmpeg']
writer = Writer(fps=10, metadata=dict(artist='Paweł Leszczyński'))

class Citizen:  # Citizen class, with his coordinates, velocity, and information about infection
    def __init__(self, coords_x = 0.0, coords_y = 0.0, velocity = 0.0, cell = 'b'):
        self.coords_x = coords_x
        self.coords_y = coords_y
        self.velocity = velocity
        self.cell = cell


class Environment:  # Environment class
    def __init__(self, size_x, size_y, no_of_citizens, p1, p2):
        self.size_x = size_x
        self.size_y = size_y
        self.no_of_citizens = no_of_citizens
        self.p1 = p1
        self.p2 = p2

    #Creates citizens, infects one random citizen
    def initialize_environment(self):
        table_of_citizens = []
        for i in range(self.no_of_citizens):
            citizen = Citizen(uniform(0, self.size_x), uniform(0, self.size_y), uniform(0.5, 1.0))
            table_of_citizens.append(citizen)
        choice(table_of_citizens).cell = 'r'
        return table_of_citizens


#   Function finding duplicates in a given list; used for collision detection
def list_duplicates(table_rounded):
    temp = defaultdict(list)
    for i,j in enumerate(table_rounded):
        temp[j].append(i)
    return ((x, y) for x, y in temp.items() if len(y)>1)



def walk(table_env, enviro):
    #   Check for collisions & if any od the collided citizens are infected
    table_rounded = []
    for j in table_env:
        table_rounded.append((round(j.coords_x), round(j.coords_y)))
    #   If there are duplicates in the rounded list of coordinates,
    #   change the color of every cell in the same coords to red (infected),
    #   using given probability
    if len(table_rounded) != len(set(table_rounded)):
        for i, j in list_duplicates(table_rounded):
            infected = False
            for j_iter in j:
                if table_env[j_iter].cell == 'r':
                        infected = True
            if infected:
                for j_iter in j:
                    if random() <= env.p1:
                        if table_env[j_iter].cell != 'y':
                            table_env[j_iter].cell = 'r'


    # Movement

    for j in table_env:
        #   Move if citizen is not at the edge
        if enviro.size_x > j.coords_x > 0 and enviro.size_y > j.coords_y > 0:
            if random() > 0.50:
                j.coords_x += j.velocity
            else:
                j.coords_y += j.velocity
        #   If citizen is at the edge, change velocity
        else:
            j.velocity = -j.velocity
            if random() > 0.50:
                j.coords_x += j.velocity
            else:
                j.coords_y += j.velocity
    return table_env

#   Setting the environment: size_x, size_y, number of citizens,
#   probability of infection, probability of death

env = Environment(20, 20, 1000, 0.4, 0.04)
table = env.initialize_environment()

# Animation & plotting

fig = plt.figure()
fig, ax = plt.subplots(1, 2, figsize=(15, 5))
anim_table = []
susceptible = env.no_of_citizens
infected = 1
removed = 0
for i in table:
    x = i.coords_x
    y = i.coords_y
    c = i.cell
    anim_table.append((x, y, c))
anim_table = set(anim_table)
x, y, c = zip(*anim_table)
ax[0].set_xlim(0, env.size_x)
ax[0].set_ylim(0, env.size_y)
ax[0].set_title('Symulacja: %os osób,' % env.no_of_citizens + ' p1:%.2f' % env.p1 + ' ,p2:%.2f' % env.p2)
ax[0].set_xlabel('krok 1')
ax[1].set_ylim(0, env.no_of_citizens+10)
ax[1].set_title('Wykres symulacji')
ax[1].set_ylabel('liczba osób')
ax[1].set_xlabel('czas')
ax[1].legend(['Narażeni', 'Zarażeni', 'Zmarli'])
mat = ax[0].scatter(x, y, color=c), ax[1].plot(0, susceptible, 'b.', infected, 'r.', removed, 'y.')


def animate(frame):
    global table
    global env
    global mat
    table_colors = []
    table = walk(table, env)

    anim_table = []
    for i in table:
        x = i.coords_x
        y = i.coords_y
        c = i.cell
        # If cell is infected, and will pass probability check - mark as dead.
        if c == 'r':
            if random() <= env.p2:
                i.cell = 'y'
        table_colors.append(c)
        anim_table.append((x, y, c))

    susceptible = table_colors.count('b')
    infected = table_colors.count('r')
    removed = table_colors.count('y')

    anim_table = set(anim_table)
    x, y, c = zip(*anim_table)
    ax[0].clear()
    ax[0].set_title('Symulacja: %i osób,' % env.no_of_citizens + ' p1:%.2f' % env.p1 + ' ,p2:%.2f' % env.p2)
    ax[0].set_xlabel('krok '+str(frame+1))
    ax[1].set_ylim(0, env.no_of_citizens+10)
    ax[1].set_title('Wykres symulacji')
    ax[1].set_ylabel('liczba osób')
    ax[1].set_xlabel('czas')
    ax[1].legend(['Narażeni', 'Zarażeni', 'Zmarli'])
    mat = ax[0].scatter(x, y, color=c), ax[1].plot(frame, susceptible, 'b.', frame, infected, 'r.', frame, removed, 'y.')
    return mat


#  Control the number of steps using "frames" variable

ani = animation.FuncAnimation(fig, animate, frames=100, interval=50, repeat=False)
#plt.show()
ani.save('04-004.mp4', writer=writer)

