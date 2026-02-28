from itertools import product
from string import printable

c = 0
for p in product(printable[:20], repeat = 5):
    if p[0] !=0:
        if sum([int(s, 20)%2 == 0 for s in p]) <= 3:
            if sum([int(s, 20)>9 for s in p]) >= 2:
                c += 1
print(c)