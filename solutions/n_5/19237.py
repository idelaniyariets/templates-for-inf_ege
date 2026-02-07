def to3(x):
    s = ""
    while x>0:
        s = str(x%3) + s
        x //= 3
    return s

def f(n):
    n3 = to3(n)
    if n%3 == 0:
        n3 = n3+n3[-2:]
    if n%3 != 0:
        sm = to3(sum(int(x) for x in n3))
        n3 = n3 + sm
    return int(n3, 3)

for a in range(1, 500):
    if f(a) > 220 and f(a)%2 == 0:
        print(f(a))
        break