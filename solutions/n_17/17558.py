s = [int(x) for x in open("files/17_17558.txt")]

cn = len([x for x in s if x%32 == 0])
ans = []

for i in range(len(s)-1):
    pair = [s[i],s[i+1]]
    if pair[0]<0 or pair[1]<0:
        if sum(pair) < cn:
            ans.append(sum(pair))
print(len(ans), max((ans)))