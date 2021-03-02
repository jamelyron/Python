
class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"оклад": int(wage), "премия": int(bonus)}


class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return f'Имя сотрудника: {self.surname} {self.name}'

    def get_total_income(self):
        return f'Доход с учетом премии: {self._income["оклад"] + self._income["премия"]}'


print("Введите Имя")
name = input("")
print("Введите Фамилию")
surname = input("")
print("Введите Должность")
position = input("")
print("Введите Оклад")
wage = input("")
print("Введите Премию")
bonus = input("")
letsgo = Position(name, surname, position, wage, bonus)
print(letsgo.get_full_name())
print(letsgo.get_total_income())


'''Не понял, зачем нужна должность в этой программе'''