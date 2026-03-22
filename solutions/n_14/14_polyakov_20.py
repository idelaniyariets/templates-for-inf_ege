def f(ex):
    c = 0
    while ex > 0:
        if ex%5 == 4:
            c += 1
        ex //= 5
    return c

res = []
s = 5**2025 + 5**400
for x in range(10, 70001):
    ex = s - x
    res.append([f(ex), x])
print([r for r in res if r == max(res)])
#поляков гнида, руками как то надо решать
#это просто слишком долго работает