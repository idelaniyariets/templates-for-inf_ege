def delt(n, m):
    if n%m == 0:
        return True
    else:
        return False

def f(x, a):
    return delt(x, 56) <= ((not(delt(x,a))) <= (not(delt(x, 120))))

for a in range(1, 1000):
    if all(f(x,a) == 1 for x in range(1, 1000)):
        print(a)