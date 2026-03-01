f = open('files/9_5.csv')

a = []
for line in f.readlines():
    a.append(list(map(int, line.split(','))))
f.close()

res = 0
for mas in a:
    s = set(mas)
    if len(s) != 4:
        continue
    povt = set()
    for el in s:
        if mas.count(el) == 3:
            povt.add(el)
        elif mas.count(el) == 2:
            povt.add(el)
    if len(povt) == 0:
        continue
    s -= povt
    if sum(s) <= min(povt):
        res = min(mas)

print(res)
    