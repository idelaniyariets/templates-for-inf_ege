"""Примерное задание было взято из варианта решу ЕГЭ: https://inf-ege.sdamgia.ru/test?a=show_result&stat_id=23645942&retriable=1"""

P_start, P_end = 25, 64
Q_start, Q_end = 40, 115
# Находим пересечение P и Q
n_start = max(P_start, Q_start)
n_end = min(P_end, Q_end)
# Длина отрезка A должна быть вне пересечения
length_A1 = n_start - P_end  # A после P
length_A2 = Q_start - n_end  # A перед Q
print("Наименьшая возможная длина отрезка A:", abs(min(length_A1, length_A2)))
