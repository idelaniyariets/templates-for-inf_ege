from math import ceil

def f(start, end):
    if start == end: return 1
    if start > end or start == 36: return 0
    return f(start+2, end) + f(start+5, end) + f(ceil(start*2.5), end)

print(f(5, 53) * f(53, 122))