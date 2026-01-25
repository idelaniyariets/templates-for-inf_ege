for x in "0123456789ABCDEFGHIJK":
    ex = int(f"EF{x}67", 21) + int(f"3H{x}4C", 21)
    if ex%20 == 0:
        print(x, ex//7)