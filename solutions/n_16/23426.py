f = {}
g = {}

for n in range(25000):
    if n <= 20:
        g[n] = n
    else:
        g[n] = g[n - 2] + 1

for n in range(25000, 3, -1):
    f[n] = g[n - 3]

print(f[25000])