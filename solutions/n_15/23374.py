def f(x,a,y):
    return (x < a) and (y < 3*a) or (2*x + y > 128)

for a in range(1, 300):
    if all([f(x,a,y) for x in range(1, 300) for y in range(1, 300)]):
        print(a)
        break