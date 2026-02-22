def f(start, end):
    if start == end: return 1
    if start < end or start == 13: return 0
    return f(start-1, end) + f(start-2, end) + f(start//3, end)

print(f(19, 6) * f(6, 4))