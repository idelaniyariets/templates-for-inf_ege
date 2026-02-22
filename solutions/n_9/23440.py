s = [x.strip().split() for x in open("files/9_23440.txt")]

def chpovt(ln):
    c = 0
    t = 0
    for el in ln:
        if ln.count(el) == 1:
            c += 1
        if ln.count(el) == 3:
            t += 1
    if c == 1 and t == 6:
        return True
    else:
        return False

c = 0
for line in s:
    if chpovt(line):
        if max([el for el in line if line.count(el) == 3]) > [el for el in line if line.count(el) == 1][0]:
            c += 1
print(c)