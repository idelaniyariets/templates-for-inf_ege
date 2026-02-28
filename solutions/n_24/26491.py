from re import *

s = open("files/24_26491.txt").readline().strip()
reg = r"[1-9][0-9]*[+*][1-9][0-9]*(?:[*+][1-9][0-9]*)*"
h = [x.group() for x in finditer(reg, s)]
hh = [x for x in h if eval(x)%2 == 0]
print(len(sorted(hh, key=len)[-1]))
#это неправильно, задача - гроб