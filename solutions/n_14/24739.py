from string import printable

for x in printable[:21]:
    ex = int(f"ef{x}67", 21) + int(f"3h{x}4c", 21)
    if ex%20 == 0:
        print(int(ex/7))