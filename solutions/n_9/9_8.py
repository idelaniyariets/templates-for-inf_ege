f = open('files/9_8.csv')

a = []
for line in f.readlines():
    a.append(list(map(int, line.split(','))))

st = 0
res = []
for mas in a:
    st += 1
    povt = [x for x in mas if mas.count(x) == 2]
    nepovt = [x for x in mas if mas.count(x) == 1]
    if len(povt) == 6 and len(nepovt) == 2:
        if (max(povt) - min(povt))**2 > 2*(nepovt[0]**2 + nepovt[1]**2):
            res = st
print(res)