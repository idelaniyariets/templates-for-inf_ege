s = [int(x) for x in open("files/17_23447.txt")]

maxch = 0
for a in s:
    if len(str(abs(a))) == 4 and abs(a) % 100 == 39:
        if a > maxch:
            maxch = a

res = []
for i in range(len(s)-1):
    pair = [s[i], s[i+1]]
    if (len(str(abs(pair[0]))) == 4) ^ (len(str(abs(pair[1]))) == 4) and sum(pair)**2 <= maxch**2:
        res.append(sum(pair))
print(len(res), max(res))