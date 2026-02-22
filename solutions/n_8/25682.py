from itertools import product

c = 0
for p in product("ЁЛОЧЩЬ", repeat = 6):
    c += 1
    if p[0] != "Ь" and p.count('Ь')>0 and p.count("Л") + p.count("Ч") + p.count("Щ") <= 2:
        print(c)