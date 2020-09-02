numb = int(input("Введите число: "))
maximum = numb % 10
numb = numb // 10
while numb > 0:
    if numb % 10 > maximum:
        maximum = numb % 10
    numb = numb // 10

print("Самая большая цифра в введенном числе: ", maximum)
