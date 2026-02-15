def f(d,n):
    for d in range(d, int(n**0.5)+1):
        if n%d == 0:
            return [d] + f(d, n//d)
    return [n]
c = 0
for x in range(15381264, 10**10):
    res = f(2, x)
    if all([str(res[i]).count("1") == 1 for i in range(len(res))]) and len(res) == 3:
        print(x, max(res))
        c += 1
    if c == 5:
        break