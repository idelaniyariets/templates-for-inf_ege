from itertools import product

k = 0

for p in product("АВНРЬЯ", repeat = 5):
    sp = "".join(p)
    k += 1
    if sp[0] != "Я":
        if sp.count("Ь")<=1:
            if not("ЯЯ" in sp):
                print(k)