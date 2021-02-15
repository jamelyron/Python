
from sys import argv

name, work, cash, cookies = argv
try:
    result = (int(work) * int(cash)) + int(cookies)
    print(f"Зарплата сотрудника = {result}")

except Exception as e:
    print("Неверный формат")

