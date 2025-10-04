"""Примерное задание было взято из варианта решу ЕГЭ: https://inf-ege.sdamgia.ru/test?a=show_result&stat_id=23645942&retriable=1"""


def f(start, end):
    if start > end or start == 14:
        return 0
    if start == end:
        return 1
    else:
        return f(start + 1, end) + f(start + 2, end)


print(f(2, 9) * f(9, 18))
