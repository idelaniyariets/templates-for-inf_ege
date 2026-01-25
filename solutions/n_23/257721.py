dl = [x for x in range(30, 46)]
def f(start, end):
    if start == end:
        return 1
    if start < end:
        return 0
    if start > end:
        return f(start-4, end) + f(start-11, end) + f(start//2, end)
    return None

print(f(120, 20) - f(120, 30))