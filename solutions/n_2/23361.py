from itertools import product, permutations


def f(x,y,w,z):
    return (not(y <= (x == z))) and (w <= x)

for x1,x2,x3,x4,x5,x6,x7 in product([0,1], repeat = 7):
    t = (
    (x1,0,0,x2,1),
    (0,x3,0,x4,1),
    (x5,1,x6,x7,1)
    )

    if len(t) == len(set(t)):
        for p in permutations("xywz"):
            if all(f(**dict(zip(p, l))) == l[-1] for l in t):
                print(*p)