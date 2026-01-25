f = {}
g = {}

for n in range(100000, 0, -1):
    if n<80000:
        g[n] = 5*n + g[n+4]
    else:
        g[n] = 2*n + 1

for n in range(7, 56000):
    if n>=14000:
        f[n] = f[n-7] + 3*n
    else:
        f[n] = g[n-3] + 3*n - 12

print(f[50000])