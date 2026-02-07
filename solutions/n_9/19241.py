def ch(ln):
    n = []
    for el in ln:
        n.append(ln.count(el))
    if n.count(3) == 6 and n.count(1) == 1:
        return True
    else:
        return False

def fn(ln):
    se = 0
    ss = 0
    for el in ln:
        if ln.count(el) == 3:
            se+=int(el)
        if ln.count(el) == 1:
            ss = int(el)
    return se/6 < ss

file = open("9_19241.txt")
s = []
for line in file:
    s.append(line.split())

for line in s:
    if ch(line):
        if fn(line):
            print(s.index(line)+1)