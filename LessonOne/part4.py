# Вводим число
inp = input("Введите число: ")
r = -1
i = 0
# Перебираем цифры в числе, находим максимальное
for i in inp:
    while int(i) > r:
        r = int(i)
print(r)
