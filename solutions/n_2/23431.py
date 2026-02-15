from itertools import product, permutations


def f(x,y,w,z):
    return (not(y <= x)) or (z <= w) or (not z)

for x1,x2,x3,x4,x5,x6,x7 in product([0,1], repeat = 7):
    t = (
    (x1,0,x2,x3,0),
    (0,1,x4,x5,0),
    (1,x6,x7,0,0)
    )
    if len(t) == len(set(t)):
        for p in permutations("xyzw"):
            if all(f(**dict(zip(p,l))) == l[-1] for l in t):
                print(*p)