from string import printable

for x in printable[:30]:
    ex = int(f"7{x}A9F", 30) + int(f"1B3{x}", 30)
    if ex % 29 == 0:
        print(ex // 29)
        break