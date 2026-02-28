s = [int(x) for x in open("files/17_26523.txt")]

mix = 10**10

for el in s:
    if el > 0:
        if len(str(el)) == 4 and el%100 == 30 and el < mix:
            mix = el

res = []
for i in range(len(s) - 2):
    t = [s[i], s[i+1], s[i+2]]
    if sum([len(str(abs(x))) == 4 and x%2 == 0 for x in t]) == 2 and sum(t) > mix:
        res.append(sum(t))

print(len(res), max(res))