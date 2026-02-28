def f(ex):
    s = ""
    c = 0
    while ex!=0:
        if ex%25 == 0:
            c += 1
        ex //= 25
    return c

d = {}

for x in range(1, 231):
    ex = 64**678 + 55**123 - x
    d[x] = f(ex)

print(max(d.values()))
print(d.get(34))