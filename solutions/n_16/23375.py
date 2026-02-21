f = {}
g = {}

for i in range(43000):
    if i <= 9:
        g[i] = 3 * i
    else:
        g[i] = g[i-4] + 2

for n in range(43000, 3, -1):
    f[n] = g[n-1] + g[n-3]

print(f[42999])