"""
Реализовать функцию my_func(), которая принимает три позиционных аргумента
и возвращает сумму наибольших двух аргументов.
"""


def my_func(a, b, c):
    items = [a, b, c]
    items.remove(min(items))
    return sum(items)


first_number, second_number, third_number = int(input("Введите первое число: ")), int(
    input("Введите второе число: ")), int(input("Введите третье число: "))

print(my_func(first_number, second_number, third_number))
