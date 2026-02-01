g = {}
f = {}

for n in range(2027):
    if n<10:
        g[n] = n+10
    if n>= 10:
        g[n] = g[n-3] + 2

for n in range(3, 2026):
    f[n] = g[n] + g[n-1] + g[n-2] + g[n-3]

print(g[2026]*f[2025])