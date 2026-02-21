def f(exp):
    c = 0
    while exp != 0:
        if exp % 49 <= 9:
            c += 1
        exp //= 49
    return c
print(f(2*2401**525 + 3*343**524 - 4*49**523 + 5*49*522 - 6*7**521 - 35))