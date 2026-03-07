'''В файле электронной таблицы 9-249.xls в каждой строке записаны шесть натуральных чисел. Определите количество строк таблицы, содержащих числа, для которых выполнены следующие условия:
– в строке есть число, повторяющееся не меньше трёх раз;
– в строке есть число, не повторяющееся в этой строке;
– среднее арифметическое всех повторяющихся чисел строки (с учётом количества повторений) меньше среднего арифметического неповторяющихся чисел этой строки. В ответе запишите только число.'''
s = [line.strip().split() for line in open("files/9-249.txt")]

def check(ln):
    s = set()
    for el in ln:
        s.add(ln.count(el))
    if 1 in s and sum([el for el in s if el >= 3]) >= 1:
        return True
    else:
        return False

def f(ln):
    s = []
    c = []
    for el in ln:
        if ln.count(el) > 1:
            s.append(int(el))
        else:
            c.append(int(el))
    if sum(s)/len(s) < sum(c)/len(c):
        return True
    else:
        return False

c = 0
for line in s:
    if check(line) and f(line):
        c += 1
print(c)