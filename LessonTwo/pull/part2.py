
while True:
    try:
        print("Сколько элементов в списке?")
        mas = int(input())
        break
    except Exception as e:
        print("Неверный формат")

my_list = []
i = 0
j = 0
while i < mas:
    print("Введите", i+1, "значение списка")
    my_list.append(input())
    i += 1

if mas > 1:
    if mas % 2 == 0:
        while j < len(my_list):
            my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
            j += 2
    else:
        while j < len(my_list)-2:
            my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
            j += 2

print(my_list)
