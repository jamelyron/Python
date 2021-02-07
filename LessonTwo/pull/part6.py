stuff = []
esc = 0
insert = 1
analyt = 0
spy =[]
i = 1
while esc == 0:
    while insert == 1:
        print("Добавьте товар")
        print("Наименование:")
        name = input()
        print("Цена:")
        prise = int(input())
        print("Количество:")
        quantity = int(input())
        my_dict = {'Наименование': name, 'Цена': prise, 'Количество': quantity, '"ед"': 'шт.'}
        spy.append(my_dict)
        stuff.append(tuple([i, my_dict]))
        i += 1
        print("Добавить товар? 0/1")
        insert = int(input())
    j = 0
    for first in stuff[j:]:
        print(first)
        j += 1
    print("Запустить аналитику? 0/1")
    analyt = int(input())
    if analyt == 1:
        k = 1
        for val in stuff:
            for value in val[k:]:
                print(value)
                k += 2
# не успел доделать: в 1й части - уменьшить код, и 2 часть

    print("Выйти из программы? 0/1")
    esc = int(input())