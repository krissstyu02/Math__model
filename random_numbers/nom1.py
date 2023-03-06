import pandas as pd
import matplotlib.pyplot as plt

# Метод серединных квадратов
count = 100 #количество чисел
n = 4 #длина
chislo = 7153

list_chislo = []
list_kvadrat = []
list_random = []

start = n // 2
stop = n + n // 2

for i in range(count):
    kvadrat = chislo * chislo
    if len(str(kvadrat)) % 2 == 1:
        kvadrat = '0' + str(kvadrat)

    chislo_srez = int(str(kvadrat)[start:stop]) #отделяем середину
    random = chislo_srez / (10 ** n)
    list_chislo.append(chislo)
    list_kvadrat.append(kvadrat)
    list_random.append(random)
    chislo = chislo_srez

data = {'chislo': list_chislo, 'kvadrat': list_kvadrat, 'random': list_random}

df = pd.DataFrame(data=data)
print(df)

#строим диаграммы с количеством промежутков 100
x=[0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]
df['random'].hist(bins=x)
x_ticks=[0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]
plt.xticks(ticks=x_ticks)
plt.xlim(0.0, 1.0)
plt.show()