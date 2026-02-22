s = open("files/24_24745.txt").readline().strip()
l = m = c = 0
for r in range(1, len(s)):
    c += (s[r-1] == s[r])
    while c > 100000:
        c -= (s[l] == s[l+1])
        l += 1
    if c == 100000:
        m = max(m, r-l+1)
print(m)