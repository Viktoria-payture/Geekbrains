"""
Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""


def user(
        name=None,
        surname=None,
        year=None,
        city=None,
        email=None,
        phone=None):
    return f"{name} {surname} {year} {city} {email} {phone}"

user_name = input("Введите Ваше имя: ")
user_surname = input("Введите Вашу фамилию: ")
user_year = int(input("Введите год рождения: "))
user_city = input("Введите город проживания: ")
user_email = input("Введите Ваш email: ")
user_phone = input("Введите Ваш номер телефона: ")

print(user(name=user_name, surname=user_surname, year=user_year, city=user_city, email=user_email, phone=user_phone))