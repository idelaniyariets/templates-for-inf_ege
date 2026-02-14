def f(n):
    s = ""
    while n>0:
        s = str(n%9) + s
        n //= 9
    return s.count("0")


for x in range(3000):
    ex = 9**150 + 9**30 - x
    if f(ex) == 122:
        print(x)
        break