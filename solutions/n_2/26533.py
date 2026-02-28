from itertools import product, permutations

def f(x,y,z,w):
    return ((x and (y or w)) <= (z and y)) and x

for x1,x2 in product([0,1], repeat = 2):
    t = (
    (1,0,0,x1,1),
    (1,x2,0,1,1),
    (1,0,1,1,1)
    )

    if len(t) == len(set(t)):
        for p in permutations("xyzw", r=4):
            if all(f(**dict(zip(p, l))) == l[-1] for l in t):
                print(*p)