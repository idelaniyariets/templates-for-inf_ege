def f(start, end):
    if start == end: return 1
    if start < end or start in [s for s in range(30, 46)]: return 0
    return f(start - 4, end) + f(start - 11, end) + f(start // 2, end)

print(f(120, 20))