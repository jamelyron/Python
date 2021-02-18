from random import randrange
import re

my_file = open("part5.txt", 'w')
my_list = [randrange(500) for i in range(randrange(25))]
my_file.write(str(my_list))
print(f"Файл записан - {my_list}")
my_file.close()

my_file = open('part5.txt', 'r')
summa = my_file.read()
summa = re.findall(r'[+-]?\d+', summa)
summa = [int(x) for x in summa]
result = 0
for i in summa:
    result += i
print(f"Сумма чисел в файле - {result}")
my_file.close()

