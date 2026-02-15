from re import *

m = 0
s = open("24_23424.txt").readline().strip()
reg = "[AEIOUY][0-9]*[AEIOUY]"
h = [x.group() for x in finditer(reg, s)]

for wd in h:
    if wd[0] == wd[-1]:
        m = max(m, len(wd))

print(m)