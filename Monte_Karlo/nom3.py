import math
import random
import matplotlib.pyplot as plt
from matplotlib.patches import *
from matplotlib.patches import Rectangle
import numpy as np
import scipy.stats as sps

x_inside = []
y_inside = []
x_outside = []
y_outside = []

def M(x_,y_,r):
    m = 0
    for i in range (len(y_)):
        if ((x_[i] - r)**2 + (y_[i]-r)**2 < r**2):
            m += 1
            x_inside.append(x_[i])
            y_inside.append(y_[i])
        else :
            x_outside.append(x_[i])
            y_outside.append(y_[i])
    return m


N = 100
R = 12

rand_pos=(2*R) * np.random.random_sample(2*N)
x_rand=rand_pos[0:N-1]
y_rand=rand_pos[N:2*N-1]


m = M(x_rand,y_rand,R)
print('Количество точек внутри круга M =',m)

s = (m/N)*4*(R**2)
print('Площадь круга S =',round(s,2))
p = round((m/N)*4,3)
print('Значение pi =',p)


fi = np.arange(0, 2*p, 0.01) # угол fi от 0 до 2pi с шагом 0.01
plt.plot( (R+R*np.cos(fi)), (R+R*np.sin(fi)), lw=3)
plt.scatter(x_inside, y_inside, s=10, c="red")
plt.scatter(x_outside, y_outside, s=10, c="black")
plt.axis('equal')
plt.show()