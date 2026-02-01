file = [line.strip().split() for line in open("9_17863.txt")]

def chpovt(line):
    dts = []
    pv = 1
    for el in line:
        dts.append(line.count(el))
    for el in dts:
        pv *= int(el)
    if pv == 27:
        return True
    else:
        return False

def fsum(line):
    sm = 0
    pv = 0
    for el in line:
        if line.count(el) == 1:
            sm += int(el)
        if line.count(el) == 3:
            pv += int(el)
    if pv**2 > sm**2:
        return True
    else:
        return False

c = 0

for line in file:
    if chpovt(line):
        if fsum(line):
            c += 1

print(c)