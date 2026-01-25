def f(n):
    n = bin(n)[2:]
    if sum(int(a) for a in n) % 2 == 0:
        n = n+"0"
        n = list(n)
        n[1] = "0"
        n[0] = "1"
    else:
        n = n+"1"
        n = list(n)
        n[0], n[1] = "1","1"
    return int("".join(n), 2)

for x in range(500):
    if f(x)>367 and x%2 != 0 and f(x)%2 == 0:
        print(x)
        break