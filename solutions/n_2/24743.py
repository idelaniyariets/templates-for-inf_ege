from itertools import permutations, product

def f(x,y,w,z):
    return ((z<=x) and (x<=y)) or (w == (z or x))

for x1, x2, x3, x4, x5, x6, x7 in product([0,1], repeat = 7):
    t = (
        (1, x1, x2, x3, 0),
        (x4, x5, 1, 1, 0),
        (1, x6, x7, 1, 0)
    )

    if len(t) == len(set(t)):
        for p in permutations("xyzw", r=4):
            if all(f(**dict(zip(p, l))) == l[-1] for l in t):
                print(*p)
