
data = {}
with open("part6.txt", "r", encoding='utf-8') as my_file:
    my_list = [line.split() for line in my_file]
    for el in my_list:
        num = 0
        for elem in el:
            try:
                num += int(elem)
            except:
                continue
        data[el[0]] = num
print(data)