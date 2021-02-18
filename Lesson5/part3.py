

with open("part3.txt", "r") as my_file:
    cash = []
    man = []
    my_list = my_file.read().split('\n')
    for i in my_list:
        i = i.split()
        if int(i[1]) < 20000:
            man.append(i[0])
        cash.append(i[1])

math = sum(map(int, cash)) / (len(cash))
print(f'{man} имеет оклад меньше 20000')
print(f'Средний доход -  {math}')