profit = int(input("Введите выручку"))
loss = int(input("Введите издержки"))
if profit < loss:
    print("Фирма работает в убыток")
elif profit == loss:
    print('Фирма отработала в "0"' )
elif profit > loss:
    print("Фирма работает прибыльно")
    renta = (profit-loss)/profit
    print("Рентабильность составила:", renta)
    people = int(input("Введите количество сотрудников"))
    print("Прибль фирмы, в расчете на сотрудника:", (profit-loss)/people )