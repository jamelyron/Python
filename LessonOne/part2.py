# вводим данные
inp=int(input("введите количество секунд"))
# расчет часов, минут, секунд
hour= inp//3600
minute=(inp//60)%60
second=inp%60
# узнаем, нужно ли добавить "0" для правильного вывода
if hour<10:
    hour='0'+str(hour)
else:
    hour=str(hour)
if minute<10:
    minute='0'+str(minute)
else:
    minute=str(minute)
if second<10:
    second='0'+str(second)
else:
    second=str(second)
# вывод данных
print(inp, "секунд =", hour+':'+minute+':'+second)