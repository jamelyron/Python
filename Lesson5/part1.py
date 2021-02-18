
my_list = []
while True:

    data = input("Введите данные: ")
    if not data:
        exit()
    else:
        newData = data + '\n'
        my_list.append(newData)

    my_file = open('part1.txt', 'w')
    my_file.writelines(my_list)
    my_file.close()