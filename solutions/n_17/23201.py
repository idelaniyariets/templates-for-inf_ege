s = [int(x) for x in open("files/17_23201.txt")]

minel = 105000
for el in s:
    if len(str(abs(el))) == 3 and el%10 == 7 and el < minel:
        minel = el

res = []
for i in range(len(s)-1):
    pair = [s[i], s[i+1]]
    if (len(str(pair[0])) == 3)^(len(str(pair[1])) == 3) and sum(pair) % minel == 0:
        res.append(sum(pair))
print(len(res), min(res))