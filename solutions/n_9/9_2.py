f = open('files/9_2.csv')

a = []
for line in f.readlines():
    a.append(list(map(int, line.split(','))))

f.close()

strok = 0
for mas in a:
    s = set(mas)
    temp = sorted(mas)
    print(temp)
    if len(s) == len(mas) and sum(temp[3:]) <= sum(temp[:3]):
        strok += 1

print(strok)
