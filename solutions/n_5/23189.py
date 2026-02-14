def f(n):
    bn = bin(n)[2:]
    if n%3 == 0:
        bn = bn+bn[-3]+bn[-2]+bn[-1]
    else:
        bn = bn + bin((n%3)*3)[2:]
    return int(bn,2)

for x in range(5, 300):
    if f(x) <= 130:
        print(x)