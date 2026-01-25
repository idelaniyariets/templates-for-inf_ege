from itertools import product

k = 0

for p in product("ЁЛОЧЩЬ", repeat = 6):
    p = "".join(p)
    k+=1
    if "Ь" in p:
        if p[0] != "Ь":
            if sum(p.count(c) for c in "ЛЧЩЬ") <= 2:
                print(k)