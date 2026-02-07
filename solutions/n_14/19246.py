from string import printable


for x in printable[:25]:
    ex = int(f"11353{x}12", 25) + int(f"135{x}21", 25)
    if ex%24 == 0:
        print(int(x, 25), ex//24)