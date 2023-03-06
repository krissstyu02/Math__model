import pandas as pd
import matplotlib.pyplot as plt


# линейный конгруэнтный метод
n = 4
count = 100

a_const = 1357
b_const = 5689
var = a_const

# 1377 взаимн прост с 5689
c_const = 1377

list_var = []
list_prod_plus = []
list_celoye = []
list_ostatok = []
list_random = []

for i in range(count):
    prod_plus = (a_const * var) + c_const
    celoye = prod_plus // b_const
    ostatok = prod_plus % b_const
    if len(str(ostatok)) < n:
        ostatok = int(str(ostatok) + '0' * (n - len(str(ostatok))))

    random = ostatok / (10 ** n)

    list_var.append(var)
    list_prod_plus.append(prod_plus)
    list_celoye.append(celoye)
    list_ostatok.append(ostatok)
    list_random.append(random)

    var = ostatok

data = {'var': list_var, 'prod_plus': list_prod_plus, 'celoye': list_celoye, 'ostatok': list_ostatok,
        'random': list_random}

df = pd.DataFrame(data=data)
print(df)

x=[0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]
df['random'].hist(bins=x)
x_ticks=[0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]
plt.xticks(ticks=x_ticks)
plt.xlim(0.0, 1.0)
plt.show()
