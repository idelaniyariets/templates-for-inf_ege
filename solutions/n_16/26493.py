f = {}
g = {}

for n in range(55000, 0, -1):
    if n >= 52000:
        g[n] = n/10 + 30
    else:
        g[n] = g[n+1] - 0.5

for n in range(3, 12000):
    if n >= 67:
        f[n] = n
    else:
        f[n] = 3 * (g[n-2] - 1)

print(f[10007])