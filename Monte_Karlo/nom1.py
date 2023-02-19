import math
import random
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches


def function(x_,n):
    y_1=10*x_/n
    y_2=10*((x_-20)/(n-20))+20
    return y_1,y_2


def s_tr(a,b):
    s=(1/2)*a*b
    return s


def M(y_nach1,y_nach2,y_random):
    m=0
    for i in range (len(y_random)):
        if y_nach2[i]<y_random[i]<y_nach1[i]:
            m+=1
    return m

x_outside = []
y_outside = []
x_inside = []
y_inside = []
def draw_points(arr_xx, arr_yy):
    # по условию определяем точки внутри/снаружи фигуры
    for i in range(0, N):
        f1, f2 = function(arr_xx[i],n)
        if f1 < arr_yy[i] < f2:
            x_inside.append(arr_xx[i])
            y_inside.append(arr_yy[i])
        else:
            x_outside.append(arr_xx[i])
            y_outside.append(arr_yy[i])



n=12
N=1000
k=1000

x_=np.random.uniform(0, 21, k)
x_[k-1]=21.6
y_1,y_2=function(x_,n)



amin=min(x_)
amax=max(x_)
bmin=min(min(y_1),min(y_2))
bmax=max(max(y_1),max(y_2))


a=round(amax,2)
b=round(bmax,2)
s=round(s_tr(a,b),2)

x_rand=np.random.uniform(0, a, N)
y_rand=np.random.uniform(0, b, N)
arr_random1,arr_random2=function(x_rand,n)
m=M(arr_random2,arr_random1, y_rand)


s_2=m/N
s_2=round(s_2*a*b,2)
del_x=round(math.fabs(s-s_2),2)
otn_x=round((del_x/s)*100)
print("a=", a)
print("b=", b)
print("S=",s)
print("M=",m)
print("Приближенная S=", s_2)
print("Абсолютная погрешность:", del_x)
print("Относительная погрешность:", otn_x,"%")

plt.plot(x_, y_1, 2, c="blue")
plt.plot(x_, y_2, 2, c="blue")
plt.plot([amin,amin],[bmin,bmax], 2, c="blue")
draw_points(x_rand,y_rand)

plt.scatter(x_inside, y_inside, s=10, c="red")
plt.scatter(x_outside, y_outside, s=10, c="black")
plt.show()
