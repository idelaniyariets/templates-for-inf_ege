f = open('files/9_1.csv')

a = []
for line in f.readlines():
    a.append(list(map(int, line.split(','))))


res = {}

for mas in a:
   cnt = 0
   povt = 0
   for el in mas:
    if mas.count(el) == 3:
        cnt += 3
        povt = el
    elif mas.count(el) != 1:
        cnt = 10000
        continue
    
    if cnt == 3 and (sum(mas)-3*povt) / (len(mas)-3) < povt and max(mas) % min(mas) != 0:
        res[a.index(mas)+1] = sum(mas)

print(res)
print(max(res.values()))