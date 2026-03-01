'''
№ 23747 Демоверсия 2026 (Уровень: Базовый)

Откройте файл электронной таблицы, содержащей в каждой строке семь натуральных чисел. Определите сумму чисел в строке с наибольшим номером, для которой выполнены оба условия:
– в строке есть одно число, которое повторяется трижды, остальные четыре числа различны;
– среднее арифметическое неповторяющихся чисел строки не больше повторяющегося числа.
В ответе запишите только число.'''
lines = [line.strip().split() for line in open("files/9_23747.txt")]

def product(line):
#функция для нахождения произведения
#чисел в массиве. для решения
    p = 1
    for element in line:
        p *= int(element)
    return p

def check_repeats(line):
#поиск повторяющихся чисел
    counts = []
    for element in line:
        counts.append(line.count(element))
    if product(counts) == 3**3: #здесь возводим число повторений в эту же степень
        return True
    else:
        return False

def f(line):
#ситуативная функция для второго условия
#ее может и не быть
    summ = 0
    num = 0
    for element in line:
        if line.count(element) == 3:
            num = int(element)
        else:
            summ += int(element)
    if summ/4 <= num:
        return True
    else:
        return False

#решение по условию задачи
c = 0
res = {}
for line in lines:
    c += 1
    if check_repeats(line) and f(line):
        res[c] = sum([int(x) for x in line])

print(res[max(res)])