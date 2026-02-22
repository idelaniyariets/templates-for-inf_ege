s = [int(a) for a in open("files/17_25725.txt")]

d3 = len([(a for a in s if a%3 == 0)])
res = []

for i in range(len(s)-1):
    pair = [s[i], s[i+1]]
    if sum(pair) > d3:
        if (pair[0]<0 and pair[1]%2 == 0)^(pair[0]%2 == 0 and pair[1]<0):
            res.append(sum(pair))

print(len(res), max(res))