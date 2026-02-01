f = {}

for n in range(1, 2025):
    if n == 1:
        f[n] = 1
    if n>1:
        f[n] = (n-1) * f[n-1]

print((f[2024] + 2 * f[2023])/f[2022])