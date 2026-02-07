f = {}

for n in range(13767):
    if n<5:
        f[n] = n
    else:
        f[n] = 2*n * f[n-4]
print((f[13766]- 9 * f[13762])/f[13758])