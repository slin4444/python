"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""
n = int(input(f'Введите число - '))
sum_n = n + int(str(n) * 2) + int(str(n) * 3)
print(f"Сумма равна - {sum_n}")
