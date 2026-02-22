s = open("files/24_19254.txt").readline().strip()
l = m = c = 0

for r in range(4, len(s)):
    if s[r-3:r+1] == "FSRQ":
        c+=1
    while c>80:
        c-= s[l:l+4] == "FSRQ"
        l += 1
    if c == 80:
        m = max(m, r - l + 1)
print(m)