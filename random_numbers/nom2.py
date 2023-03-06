import pandas as pd
import matplotlib.pyplot as plt

#Метод серединных произведений
count = 6
n = 4
yadro = 5167 #ядро
mnozh = 3729 #множитель

list_mnozh = []
list_prod = []
list_random = []

start = n // 2
stop = n + n // 2

for i in range(0, count):
    prod = yadro * mnozh
    if len(str(prod)) % 2 == 1:
        prod = '0' + str(prod)

    chislo_srez = int(str(prod)[start:stop])
    random = chislo_srez / (10 ** n)
    list_mnozh.append(mnozh)
    list_prod.append(prod)
    list_random.append(random)
    mnozh = int(str(prod)[n:]) #берем последние разряды

data = {'mnozh': list_mnozh, 'prod': list_prod, 'random': list_random}

df = pd.DataFrame(data=data)
print(df)

x=[0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]
df['random'].hist(bins=x)
x_ticks=[0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]
plt.xticks(ticks=x_ticks)
plt.xlim(0.0, 1.0)
plt.show()