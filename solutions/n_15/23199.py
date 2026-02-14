def f(x,a,y):
    return (x*y > a) or (x > y) or (11 > x)

for a in range(300):
    if all([f(x,a,y) for x in range(300) for y in range(300)]):
        print(a)
