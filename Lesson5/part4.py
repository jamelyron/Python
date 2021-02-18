
ru_ru = {'One': 'Odin', 'Two': 'Dva', 'Three': 'Tri', 'Four': 'Chetyre'}
my_list = []
my_file = open("part4.txt", 'r')
for el in my_file:
    data = el.split(" - ")
    if data[0] in ru_ru:
        my_list.append(ru_ru[data[0]] + ' - ' + data[1])

data_file = open("part4_2.txt", "w")
data_file.writelines(my_list)
my_file.close()
data_file.close()
