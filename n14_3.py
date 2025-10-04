"""Примерное задание было взято из варианта решу ЕГЭ: https://inf-ege.sdamgia.ru/test?a=show_result&stat_id=23645942&retriable=1"""

for x in range(3000, 1, -1):
    t = 9 * 11**210 + 8 * 11**150 - x
    c = 0
    while t != 0:  # перевод в 11-ричную
        if t % 11 == 0:
            c += 1  # считаем нули
        t //= 11
    if c == 60:
        print(x)
        exit()
