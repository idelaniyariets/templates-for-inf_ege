def to3(n):
    s = ""
    while n>0:
        s = str(n%3) + s
        n //= 3
    return s

def f(n):
    tn = to3(n)
    if n%4 == 0:
        tn += "00"
    else:
        tn += to3(n//4 * 4)
    return int(tn, 3)

for n in range(1, 300):
    if f(n) < 50:
        print(n)