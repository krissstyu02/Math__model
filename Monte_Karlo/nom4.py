import math
import random
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp


def find_ff(xx_i,yy_i):
    ff = [None]*(len(xx_i))
    for i in range(len(xx_i)):
        if xx_i[i]>0:
            ff[i] = np.arctan(yy_i[i]/xx_i[i])
        elif xx_i[i]<0:
            ff[i] = np.arctan(yy_i[i] / xx_i[i]) + np.pi
        elif yy_i[i]>0 and xx_i[i] == 0:
            ff[i] = np.pi/2
        elif yy_i[i] < 0 and xx_i[i] == 0:
            ff[i] = -np.pi/2
        else:
            ff[i] = 0
    return ff

def find_r(xx_i,yy_i):
    r = [None]*(len(xx_i))
    for i in range(len(xx_i)):
        r[i] = np.sqrt((xx_i[i]**2) + (yy_i[i]**2))
    return r

def M(r,ff,p_func):
    m = 0
    for i in range (len(r)):
        if r[i] < p_func(ff[i]):
            m += 1
    return m

out_x = []
out_y = []
in_x = []
in_y = []

A =22
B = 2

fi = np.arange(0, 2*math.pi, 0.05) # угол fi от 0 до 2pi с шагом 0.05
p_func =  lambda fi:(np.sqrt((A*(np.cos(fi)*np.cos(fi))) + (B*(np.sin(fi)*np.sin(fi)))))#p(fi) =
x1 = lambda fi:p_func(fi)*np.cos(fi) #x1 =
y1 = lambda fi:p_func(fi)*np.sin(fi) #y1 =



N = 1000
amin=min(x1(fi))
amax=max(x1(fi))
bmin=min(y1(fi))
bmax=max(y1(fi))
a=amax
b=bmax

xx_i=np.random.uniform(amin, amax, N)
yy_i=np.random.uniform(bmin, bmax, N)

ff = find_ff(xx_i,yy_i) # ffi

r = find_r(xx_i,yy_i) # r

m = M(r,ff,p_func)
print('M =',m)
s_func = lambda fi: p_func(fi)**2
s3 = round(1/2*sp.integrate.quad(s_func, 0,2*math.pi )[0], 3)
print('S=',s3)


s1 = (m/N)*a*b*4
print('Приближенная S(M/N) =',round(s1,3))

ss = math.pi/2*(A+B)
print('Приближенная S(через А и В) = ',round(ss,3))


for i in range(len(r)):
    if r[i] < p_func(ff[i]):
        in_x.append(xx_i[i])
        in_y.append(yy_i[i])
    else:
        out_x.append(xx_i[i])
        out_y.append(yy_i[i])



plt.plot(x1(fi),y1(fi), lw=3)
plt.axis('equal')
plt.scatter(in_x, in_y, s=10, c="red")
plt.scatter(out_x, out_y, s=10, c="black")
plt.show()