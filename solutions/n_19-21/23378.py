def f(s,m):
    if s <= 27: return m%2 == 0
    if m == 0: return 0
    h = [f(s-3, m-1), f(s-6, m-1), f(s//3, m-1)]
    return any(h) if m%2 != 0 else all(h)

print("19", [s for s in range(28, 300) if not(f(s,1)) and f(s, 2)])
print("20", [s for s in range(28, 300) if not(f(s, 1)) and f(s, 3)])
print("21", [s for s in range(28, 300) if (f(s, 2) or f(s, 4)) and not(f(s, 2))])