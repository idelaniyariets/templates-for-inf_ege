def f(d, n):
    for d in range(d, int(n**0.5)+1):
        if n%d == 0:
            return [d] + f(d, n//d)
    return [n]

c = 0
for x in range(2142578, 10**100):
    r = f(2, x)
    if len(r) == 2 and sum(r)%2 != 0:
        c += 1
        print(x, max(r))
    if c == 5:
        break