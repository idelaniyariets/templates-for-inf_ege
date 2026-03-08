'''(ЕГКР-2025) На числовой прямой даны два отрезка: B = [36; 75] и C = [60; 110]. Укажите наименьшую возможную длину такого отрезка A, что логическое выражение

¬(x ∈ A) → ((x ∈ B) ≡ (x ∈ C))
принимает значение 1 при любом значении переменной x.'''
def f(x,a,b,c):
    return (x not in a) <= ((x in b) == (x in c))

res = []
b = [x for x in range(36, 76)]
c = [x for x in range(60, 110)]
for a1 in range(300):
    for a2 in range(a1+1, 300):
        a = [x for x in range(a1, a2+1)]
        if all([f(x,a,b,c) for x in range(500)]):
            res.append(a2-a1+1)
print(min(res))