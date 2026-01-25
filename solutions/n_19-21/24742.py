def f(a,b,m):
    if a+b >= 841: return m%2 == 0
    if m == 0: return 0
    h = [f(a+20, b, m-1), f(a, b+20, m-1), f(a*3, b, m-1), f(a, b*3, m-1)]
    return any(h) if m%2 != 0 else all(h)

print("19",[s for s in range(1, 805) if f(36,s,2)])
print("20", [s for s in range(1, 805) if not(f(36, s, 1)) and f(36, s, 3)])
print("21", [s for s in range(1, 805) if f(36, s, 2) or f(36, s, 4) and (not(f(36, s, 1)))])