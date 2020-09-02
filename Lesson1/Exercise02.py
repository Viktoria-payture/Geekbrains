entered_value = int(input("Введите время в секундах: "))

# 1 час = 3600 секунд
hours = entered_value // 3600
reminder = entered_value % 3600  # остаток в секундах
minutes = reminder // 60
seconds = reminder % 60

input(f"Время: {hours:02}:{minutes:02}:{seconds:02}")
