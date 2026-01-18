from itertools import product, permutations

def f(x,y,z,w):
    return ((x or y) <= z) or (y==w)

for x1, x2, x3, x4 in product([0,1], repeat = 4):
    t = (
        (0,1,x1,x2,0),
        (1,x3,1,0,0),
        (x4,1,1,0,0)
    )

    if len(t) == len(set(t)):
        for p in permutations("xyzw"):
            if all(f(**dict(zip(p, l))) == l[-1] for l in t):
                print(*p)