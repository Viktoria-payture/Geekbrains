"""
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def splitting(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Нельзя делить на ноль!"


first_number = int(input("Введите первое число: "))
second_number = int(input("Введите второе число: "))

print(splitting(first_number, second_number))
