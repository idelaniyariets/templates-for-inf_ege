def fd(d,n):
    for d in range(d, int((n**0.5))+1):
        if n%d == 0:
            return [d] + fd(d, n//d)
    return [n]

c = 0
for x in range(1324728, 2**100):
    n = fd(2, x)
    if len(n) == 2:
        if str(n[0]).count("5") == 1 and str(n[1]).count("5") == 1:
            c += 1
            print(x, max(n))
    if c == 5:
        break