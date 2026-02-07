def f(x,a,y):
    return (x-(3*y) < a) or (y>400) or (x>56)

for a in range(500):
    if all([f(x,a,y) for x in range(1, 500) for y in range(1, 500)]):
        print(a)
        break