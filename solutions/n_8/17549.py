from itertools import product

c = 0

for p in product("КОСУФ", repeat = 5):
    c += 1
    if p.count("Ф") == 0 and p.count("У") == 2:
        print(c)