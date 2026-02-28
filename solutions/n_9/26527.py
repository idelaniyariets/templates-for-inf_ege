s = [line.strip().split() for line in open("files/9_26527.txt")]

def pr(line):
    p = 1
    for el in line:
        p *= int(el)
    return p

def chpovt(ln):
    s = []
    for el in ln:
        s.append(ln.count(el))

    if pr(s) == 3**3:
        return True
    else:
        return False

def f(line):
    s = 0
    c = 0
    for el in line:
        if line.count(el) == 3:
            c = int(el)
        else:
            s += int(el)

    if s/5 <= c:
        return True
    else:
        return False

c = 0
d = {}
for line in s:
    c += 1
    if chpovt(line):
        if f(line):
            d[c] = [sum([int(x) for x in line])]

print(d.get(max(d)))