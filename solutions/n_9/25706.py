s = [line.strip().split() for line in open("files/9_25706.txt")]

c = 0
for line in s:
    print(line)
    if sum([int(x) for x in line])%min([int(x) for x in line]) == 0 or sum([int(x)%3 == 0 for x in line]) >= 4:
        c += 1
print(c)