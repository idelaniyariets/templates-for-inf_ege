f = open("24_22446.txt").readline().strip()
l = m = s = 0
for r in range(2, len(f)):
    if f[r-2: r+1] == "LND":
        s += 1
    while s > 10000:
        if f[l:l+3] == "LND":
            s -= 1
        l += 1
    if s<=10000:
        for l1 in range(l, r):
            if f[l1] == f[r]:
                m = max(m, r-l1+1)
                break
print(m)