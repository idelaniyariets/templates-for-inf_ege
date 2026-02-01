s = [int(x) for x in open("17_24973.txt")]
mn = 0
res = []

for i in sorted(s[::]):
    if len(str(i)) == 3 and i%100 == 10:
        mn = i
        break

for i in range(len(s)-1):
    pair = [s[i], s[i+1]]
    if (len(str(pair[0])) == 5 or len(str(pair[1])) == 5) and len(str(pair[0])) != len(str(pair[1])):
        if sum(pair)%mn == 0:
            res.append(sum(pair))
print(len(res), max(res))