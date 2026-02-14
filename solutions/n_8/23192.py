from itertools import product

c = 0
for p in product("ЕИОРТЯ", repeat = 6):
    c += 1
    if c%2 != 0 and p[0] not in "РТЯ" and p.count("И") >= 2:
        print(c)