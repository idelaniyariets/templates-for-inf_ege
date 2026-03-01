f = open('files/9_4.csv')

a = []
for line in f.readlines():
    a.append(list(map(int, line.split(','))))
f.close()

for mas in a:
    k1 = 0
    k2 = 0
    for el in mas:
        if el % 2 == 0:
            k1 += 1
        else:
            k2 += 1
    if k2 == k1 and len(set(mas)) == len(mas) and mas == sorted(mas):
        print(sum(mas))
        break