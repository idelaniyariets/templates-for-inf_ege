def f(n, s):
    dt = []
    for i in range(n, s):
        if s%i == 0:
            dt.append(i)
    return sum(dt)

c = 0

for x in range(500000, 550000):
    if f(2, x)%10 == 9:
        print(x, f(2,x))
        c += 1
        if c == 5:
            break