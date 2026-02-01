from itertools import product, permutations, repeat


def f(x,y,z,w):
    return (w <= (not(z <= x))) or y

for x1,x2,x3,x4,x5,x6,x7 in product([0,1], repeat = 7):
    t = (
        (1,x1,x2,x3,0),
        (0,1,0,x4,0),
        (x5,0,x6,x7,0)
    )
    if len(t) == len((set(t))):
        for p in permutations("xyzw"):
            if all(f(**dict(zip(p, l))) == l[-1] for l in t):
                print(*p)