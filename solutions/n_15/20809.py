def f(x,a,b):
    return (x%a == 0) or ((x in b) <= (not(x%22 == 0)))

b = [s for s in range(60, 81)]

for a in range(1, 500):
    if all([f(x,a,b) for x in range(500)]):
        print(a)