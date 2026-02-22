'''№ 25361 ЕГКР 13.12.25 (Уровень: Базовый)

Текстовый файл состоит из десятичных цифр и заглавных букв латинского алфавита. Определите в прилагаемом файле максимальное количество идущих подряд символов, среди которых буква F встречается ровно 76 раз, чётная цифра встречается ровно один раз, искомая последовательность начинается с этой единственной чётной цифры.
В ответе запишите число - количество символов в найденной последовательности.
Для выполнения этого задания следует написать программу.'''
s = open("files/24_25361.txt").readline().strip()
l = m = c = ch = 0
for r in range(len(s)):
    c+=s[r]=="F"
    ch+=(s[r].isdigit() and int(s[r])%2==0)
    if ch>0:
        l = r
        c=0
        ch -= (s[l].isdigit() and int(s[l])%2==0)
    while c>76:
        l+=1
        c-=s[l]=="F"
    while not((s[l].isdigit() and int(s[l])%2==0)):
        l+=1
        c-=s[l]=="F"
    if c==76 and ch==0:
        m = max(m, r-l+1)
print(m)

s = open("24_25361.txt").readline()
m = 0
for l in range(len(s)):
    for r in range(l+m, len(s)):
        c = s[l:r+1]
        if c.count("F") == 76 and c[0] in "24680" and (c.count("2") == 1 or c.count("4") == 1 or c.count("6") == 1 or c.count("8") == 1 or c.count("0") == 1) and (c.count("2") + c.count("4") + c.count("6") + c.count("8") + c.count("0") == 1):
            m = max(m, len(c))
        else:
            break
print(m)