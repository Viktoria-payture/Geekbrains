profit = int(input("Укажите размер выручки: "))
costs = int(input("Укажите размер издержек: "))

if profit > costs:
    print("Финансовый результат положительный. Рентабельность выручки: ", round(profit / costs, 2))
else:
    print("Финансовый результат отрицательный")

quantity = int(input("Введите количество сотрудников: "))
print("Прибыль фирмы в расчете на одного сотрудника: ", round(profit / quantity, 2), "руб.")
