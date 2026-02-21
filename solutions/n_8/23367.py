from itertools import product

cn = 0
for p in product("0123456", repeat = 5):
    if p[0] != "0" and p.count("6") == 1 and all([p[i] != p[i+1] for i in range(len(p)-1)]):
        cn += 1
print(cn)