'''№ 25355 ЕГКР 13.12.25 (Уровень: Базовый)
Алгоритм вычисления функций
F(n) и
G(n), где
n - целое число, задан следующими соотношениями:
F(n)=F(n−4)+3580, если n≥19;
F(n)=6×(G(n−7)−36), если n<19;
G(n)=n/20+28, если n≥248045;
G(n)=G(n+9)−4, если n<248045.
Чему равно значение функции
F(673)?'''
from functools import lru_cache
from sys import setrecursionlimit
setrecursionlimit(10000)
@lru_cache(None)
def f(n):
    if n >=19:
        return f(n-4) + 3580
    if n < 19:
        return 6*(g(n-7)-36)
@lru_cache(None)
def g(n):
    if n >= 248045:
        return n/20+28
    if n < 248045:
        return g(n+9) -4
for i in range(250000, 0, -1):
    g(i)
print(f(673))