
my_file = open('part2.txt', 'r')
data = my_file.readlines()
print(f'Количество строк - {len(data)}')
my_file.seek(0)
while True:
    i = 0
    for el in my_file:
        words = 0
        words += el.count(" ")
        words += 1
        i += 1
        if words == 1:
            print(f"{words} слово в {i} строке")
        elif words < 5:
            print(f"{words} слова в {i} строке")
        else:
            print(f"{words} слов в {i} строке")