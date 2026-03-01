f = open('files/9_3.csv')

a = []
for line in f.readlines():
    a.append(list(map(int, line.split(','))))

res = 0
for mas in a:
    nech = 0
    chet = 0
    for el in mas:
        if el % 2 == 0:
            chet += 1
        else:
            nech += 1
    if nech == chet and mas == sorted(mas) and len(set(mas)) == len(mas):
        res = sum(mas)

f.close()
print(res)