def f(n):
    c = n
    tn = ""
    while n>0:
        tn = str(n%3) + tn
        n //= 3
    if c%3 == 0:
        tn = "1"+tn+"02"
    else:
        ost = (c%3)*4
        tost = ""
        while ost > 0:
            tost = str(ost%3) + tost
            ost //= 3
        tn += tost
    return int(tn, 3)

for n in range(500):
    if f(n) < 100:
        print(n)