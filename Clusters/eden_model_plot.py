import matplotlib.pyplot as plt

x1_x = [500,1000,1500,2000,2500,3000,3500,4000,4500,5000,5500,6000,6500,7000,7500,8000,8500,9000,9500,10000]
x1_y = [15,20,27,28,32,34,37,39,40,46,44,48,50,51,52,55,57,57,59,65]
x2 = [22,31,39,45,50,55,59,63,70,70,74,77,81,84,87,89,92,95,97,100]

plt.plot(x1_x,x1_y, label = 'Promień')
plt.plot(x1_x,x2, label = 'N^1/d, d=2')
plt.legend()
plt.show()