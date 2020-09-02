first_day = int(input("Количество км в 1 день пробежки: "))
distance = int(input("Сколько км нужно пробежать: "))
day = 1
while first_day < distance:
    first_day = first_day + first_day * 0.1
    day += 1

print("Ответ: на ", day, "-й день спортсмен достиг результата — не менее ", distance, "км")
