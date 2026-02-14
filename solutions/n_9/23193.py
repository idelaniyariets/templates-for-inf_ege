s = [line.strip().split() for line in open("9_23193.txt")]
def chpovt(line):
    c = set()
    for el in line:
        c.add(line.count(el))
    pr = 1
    for el in c:
        pr *= el
    if pr == 3:
        return True
    else:
        return False

def f(line):
    sp = 0
    nel = 0
    for el in line:
        if line.count(el) == 1:
            sp += int(el)
        else:
            nel = int(el)
    if nel > sp/5:
        return True

c = 0
for line in s:
    c += 1
    if chpovt(line) and f(line):
        print(c)
