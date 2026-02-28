def f(d, n):
    for d in range(d, int(n**0.5)+1):
        if n%d == 0:
            return [d] + f(d, n//d)
    return [n]

def isp(n):
    if int(str(n)) == int(str(n)[::-1]):
        return True
    else:
        return False
c = 0
for x in range(3502101, 10**100):
    dt = f(2, x)
    if len(dt) == 4 and sum([len(str(x)) == 2 and isp(x) for x in dt]) >= 1:
        c += 1
        print(x, max(dt))
    if c == 5:
        break