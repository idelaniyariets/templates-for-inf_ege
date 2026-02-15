def f(x):
    n = x
    tn = ""
    while x>0:
        tn = str(x%3) + tn
        x //= 3
    if n % 3 == 0:
        tn = "1" + tn + "02"
    else:
        ost = (n%3)*3
        tost = ""
        while ost > 0:
            tost = str(ost % 3) + tost
            ost //= 3
        tn += tost
    return int(tn, 3)

for n in range(300):
    if f(n) < 199:
        print(n)