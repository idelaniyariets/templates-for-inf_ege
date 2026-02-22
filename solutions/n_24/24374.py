s = open("files/24_24374.txt").readline().strip()
m = l = c = 0
ans = []
for r in range(2, len(s)-1):
    if s[r].isdigit() and s[r-1].isalpha() and s[r-2].isalpha():
        c += 1
    if s[r-1].isdigit() and s[r].isalpha() and s[r+1].isdigit():
        l = r+1
        while s[l].isdigit():
            l += 1
        c = 0
    while c>80:
        l += 1
        if s[l].isdigit():
            while s[l].isdigit():
                l += 1
            c -= 1
    if c == 80:
        m = max(m, r-l+1)
print(m)
'''я слишком глуп для этого. не работает'''