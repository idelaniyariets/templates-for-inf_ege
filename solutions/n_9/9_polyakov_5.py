'''(ЕГКР-2025) В файле электронной таблицы 9-257.xls в каждой строке записаны семь натуральных чисел. Определите сумму чисел в строке таблицы с наименьшим номером, содержащей числа, для которых выполнены оба условия:
– в строке все числа расположены в порядке убывания;
– среднее арифметическое минимального и максимального чисел строки больше среднего арифметического оставшихся её чисел.
В ответе запишите только число.'''
s = [line.strip().split() for line in open("files/9-257.txt")]

def f(ln):
    if all([int(ln[i]) > int(ln[i+1]) for i in range(len(ln)-1)]):
        return True
    else:
        return False

def g(ln):
    ln = [int(el) for el in ln]
    m = [max(ln), min(ln)]
    c  = [x for x in ln if x != max(ln) and x!= min(ln)]
    if sum(m)/len(m) > sum(c)/len(c):
        return True
    else:
        return False

res = []
c = 0
for line in s:
    c += 1
    if f(line) and g(line):
        print(line)
        res.append([c, sum([int(x) for x in line])])
print(min(res))