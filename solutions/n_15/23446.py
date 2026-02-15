def f(x,a,y):
    return (x > 67) or (y >= x) or (3 * x - y < a)

for a in range(1, 300):
    if all([f(x,a,y) for x in range(300) for y in range(300)]):
        print(a)
        break