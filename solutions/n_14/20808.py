def to7(e):
    s = ""
    while e>0:
        s = str(e%7) + s
        e //= 7
    return s.count("0")

ans = []

for x in range(1, 2030):
    ex = 7**170 + 7**100 - x
    ans.append([to7(ex), x])

print(max(ans))