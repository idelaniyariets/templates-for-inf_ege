'''№ 17641 Основная волна 19.06.24 (Уровень: Гроб)

Текстовый файл состоит из десятичных цифр, знаков «+» и «*» (сложения и умножения). Определите максимальное количество символов в непрерывной последовательности, являющейся корректным арифметическим выражением с целыми неотрицательными числами (без знака), значение которого равно нулю. В этом выражении никакие два знака арифметических операций не стоят рядом, порядок действий определяется по правилам математики. В записи чисел отсутствуют незначащие (ведущие) нули.

В ответе укажите количество символов.'''
from re import *
#def shunting_yard(ex:list):
#    prec = {
#        "+":1, "-":1,
#        "*":2, "/":2,
#        "^":3
#    }
#
#    lt_assoc = {
#        "+":True, '-':True,
#        "*":True, "/":True,
#        "^":False
#   }
#
#    output = []
#   stack = []
#
#   for token in ex:
#       if token.isdigit():
#           output.append(token)
#       elif token in prec:
#          while (stack and stack[-1] in prec and ((lt_assoc[token] and prec[stack[-1]] >= prec[token]) or (not lt_assoc[token] and prec[stack[-1]] > prec[token]))):
#               output.append(stack.pop())
#           stack.append(token)
#       elif token == "(":
#           stack.append(token)
#       elif token == ')':
#            while stack and stack[-1] != "(":
#                output.append(stack.pop())
#            stack.pop()
#
#    while stack:
#        output.append((stack.pop()))
#
#   return output
def ch(n):
    n = list(n)
    b = []
    l = 0
    for r in range(len(n)):
        if n[r] in "*+":
            b.append("".join(n[l:r]))
            b.append(n[r])
            l = r + 1
        if r == len(n)-1:
            b.append("".join(n[l:r+1]))
    return b
s = open("24_17641.txt").readline().strip()
num = r"(([1-9][0-9]*)|([0]))"
reg = fr"{num}[+*]{num}(?:[+*]{num})*"
h = [x.group() for x in finditer(reg, s)]
print(h[:10])
res = [h[a] for a in range(len(h)) if eval("".join(ch(h[a]))) == 0]
print(len(sorted(res, key = len)[-1]))
'''я может потом допилю, но это реально жопа. press f тем, кто сдавал в 2024'''