'''(О. Лысенков) Сколько существует чисел, двенадцатеричная запись которых содержит 5 знаков и в которых не более двух раз нечетные цифры стоят рядом?'''
from itertools import product
from string import printable

c = 0
for p in product(printable[:12], repeat = 5):
    if sum([(int(p[i], 12) % 2 != 0 and int(p[i+1], 12) % 2 != 0 and int(p[i], 12)%2 !=0 and int(p[i+1], 12)%2 != 0) for i in range(len(p)-1)]) <= 2:
        c += 1
print(c)