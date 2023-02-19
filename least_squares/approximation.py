import matplotlib.pyplot as plt
import numpy as np
import math

def getMatrixMinor(m,i,j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

def getMatrixDeternminant(m):
    if len(m) == 2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]

    determinant = 0
    for c in range(len(m)):
        determinant += ((-1)**c)*m[0][c]*getMatrixDeternminant(getMatrixMinor(m,0,c))
    return determinant


def lin_func(x_,y_,n):
    m=[[sum(x_*x_),sum(x_),sum(x_*y_)],
  [sum(x_),n,sum(y_)]]
    m1=[[sum(x_*y_),sum(x_)],
    [sum(y_),n]]
    m2=[[sum(x_*x_),sum(x_*y_)],
  [sum(x_),sum(y_)]]
    aa=getMatrixDeternminant(m1)/getMatrixDeternminant(m)
    bb=getMatrixDeternminant(m2)/getMatrixDeternminant(m)
    return aa,bb

def step_func(x_,y_,n):
    m=[[sum(np.log(x_)*np.log(x_)),sum(np.log(x_)),sum(np.log(x_)*np.log(y_))],
  [sum(np.log(x_)),n,sum(np.log(y_))]]
    m1=[[sum(np.log(x_)*np.log(y_)),sum(np.log(x_))],
    [sum(np.log(y_)),n]]
    m2=[[sum(np.log(x_)*np.log(x_)),sum(np.log(x_)*np.log(y_))],
  [sum(np.log(x_)),sum(np.log(y_))]]
    aa=getMatrixDeternminant(m1)/getMatrixDeternminant(m)
    bb=getMatrixDeternminant(m2)/getMatrixDeternminant(m)
    return aa,bb

def kvad_func(x_,y_,n):
    m=[[sum((x_**4)),sum((x_**3)),sum((x_)**2),sum(x_**2*y_)],
  [sum((x_**3)),sum((x_)**2),sum(x_),sum(x_*y_)],
       [sum((x_)**2),sum(x_),n,sum(y_)]]
    m1 = [[sum(x_ ** 2 * y_), sum((x_ ** 3)), sum((x_) ** 2)],
         [sum(x_ * y_), sum((x_) ** 2), sum(x_)],
         [sum(y_), sum(x_), n]]
    m2 = [[sum((x_ ** 4)), sum(x_ ** 2 * y_), sum((x_) ** 2)],
         [sum((x_ ** 3)), sum(x_ * y_), sum(x_)],
         [sum((x_) ** 2),  sum(y_), n]]
    m3 = [[sum((x_ ** 4)), sum((x_ ** 3)), sum(x_ ** 2 * y_)],
         [sum((x_ ** 3)), sum((x_) ** 2),sum(x_ * y_)],
         [sum((x_) ** 2), sum(x_),  sum(y_)]]
    aa=getMatrixDeternminant(m1)/getMatrixDeternminant(m)
    bb=getMatrixDeternminant(m2)/getMatrixDeternminant(m)
    cc=getMatrixDeternminant(m3)/getMatrixDeternminant(m)
    return aa,bb,cc


def exponential_func(x_, y_, n):
    m = [[sum(x_ * x_), sum(x_), sum(x_ * np.log(y_))],
         [sum(x_), n, sum(np.log(y_))]]

    m1 = [[sum(x_ * np.log(y_)), sum(x_)],
          [sum(np.log(y_)), n]]

    m2 = [[sum(x_ * x_), sum(x_ * np.log(y_))],
          [sum(x_), sum(np.log(y_))]]

    aa = getMatrixDeternminant(m1) / getMatrixDeternminant(m)
    bb = getMatrixDeternminant(m2) / getMatrixDeternminant(m)
    return aa, bb

#входные данные
#x_=np.array([1,2,3,4,5,6])
#y_=np.array([1.0,1.5,3.0,4.5,7.0,8.5])
x_=np.array([2,4,6,8,10,12])
y_=np.array([1.08,0.36,0.21,0.12,0.09,0.04])
n=6

#линейная
aa,bb=lin_func(x_,y_,n)
y1=lambda x: aa*x_+bb
s1=sum(((aa*x_+bb)-y_)**2)
print("линейная функиця","a=",round(aa,2),"b=",round(bb,2),"s=",round(s1,2))
#степенная
aa1,bb1=step_func(x_,y_,n)
bet=math.e**bb1
y2=lambda x: bet*x**aa1
s2=sum((round(bet,2)*(x_**round(aa1,2))-y_)**2)
print("степенная функиця","a=",round(aa1,2),"b=",round(bet,2),"s=",round(s2,2))
#показательная
aa3,bb3=exponential_func(x_,y_,n)
bet2=math.e**bb3
y4=lambda x: bet2*math.e**(aa3*x)
s4=sum((round(bet2,2)*(math.e**(round(aa3,2)*x_))-y_)**2)
print("показательная функиця","a=",round(aa3,2),"b=",round(bet2,2),"s=",round(s4,2))
#квадратичная
aa2,bb2,cc2=kvad_func(x_,y_,n)
y3=lambda x: aa2*x**2+bb2*x+cc2
s3=sum((aa2*x_**2+bb2*x_+cc2-y_)**2)
print("квадратичная функиця","a=",round(aa2,2),"b=",round(bb2,2),"c=",round(cc2,2),"s=",round(s3,2))
#print("Минимальная суммарная погрешность у квадратичной  функции=",s3)
print("Минимальная суммарная погрешность у степенной функции=",s2,)
#рисуем
plt.scatter(x_, y_, s=10, c='black')
plt.plot(x_,y1(x_),c='blue')
plt.plot(x_,y2(x_),c='red')
plt.plot(x_,y3(x_),c='orange')
plt.plot(x_,y4(x_),c='green')
plt.legend(['points','y=ax+b','y=bet*x^a','y=bet*e^(ax)','y=ax2+bx+c'], loc=2)
plt.grid(True)
plt.show()
