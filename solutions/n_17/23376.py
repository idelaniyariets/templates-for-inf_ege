s = [int(s) for s in open("17_23376.txt")]
maxe = 0
for el in s:
    if len(str(abs(el))) == 5 and abs(el)%100 == 37 and el > maxe:
        maxe = el
print(maxe)

res = []
for i in range(len(s)-1):
    pair = [s[i], s[i+1]]
    if (len(str(abs(pair[0]))) == 5)^(len(str(abs(pair[1]))) == 5):
        if sum(pair)**2  >= maxe**2:
            res.append(sum(pair))
print(len(res), max(res))