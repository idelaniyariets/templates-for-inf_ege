f = open('files/9_7.csv')

a = []
for line in f.readlines():
    a.append(list(map(int, line.split(','))))
f.close()
res = 0
for mas in a:
    cnt = 0
    povt = 0
    for el in mas:
        if mas.count(el) == 3:
            cnt += 1
            povt = el
        elif mas.count(el) != 1:
            cnt = 1000
    if cnt == 3 and povt > ((sum(mas)-3*povt)/3):
        res = a.index(mas) + 1

print(res)