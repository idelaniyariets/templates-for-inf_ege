from itertools import product

c = 0
for p in product("АГИЛМОР", repeat = 5):
    c += 1
    if c%2 == 0 and p[0] not in "ТР" and p.count("И") >= 2:
        print(c)