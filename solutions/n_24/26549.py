''''''
s = open('files/24_26549.txt').readline().strip()
l = m = c = k = 0
for r in range(3, len(s)):
    c += s[r] == "Y"
    k += s[r-3:r+1] == "2025"
    while k > 50:
        k -= s[l:l+4] == "2025"
        l += 1
    if c >= 140 and k == 50 and s[r-3:r+1] == "2025":
        m = max(m, r-l+1)
print(m)