
def fact(n):
    data = 1
    for i in range(1, n + 1):
        data *= i
        yield data


esc = 0
while esc != 1:
    print("Введите факториал числа")
    n = int(input())
    for el in fact(n):
        print(el)
    print("Выйти из программы? 0/1")
    esc = input()