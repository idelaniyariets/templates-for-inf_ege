f = open('files/9_9.csv')

a = []
for line in f.readlines():
    a.append(list(map(int, line.split(','))))

st = 0
for mas in a:
    zamet = [x for x in mas if x > sum(mas)/len(mas)]
    chet = [x for x in zamet if x % 2 == 0]
    nechet = [x for x in zamet if x % 2 != 0]

    chet1 = [x for x in mas if x % 2 == 0]
    nechet1 = [x for x in mas if x % 2 != 0]
    if len(chet) < len(nechet) and sum(chet1) > sum(nechet1):
        st += 1
f.close()

print(st)