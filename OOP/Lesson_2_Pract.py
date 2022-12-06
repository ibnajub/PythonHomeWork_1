# 1. Створити клас Employee.
# 2. Конструктор має приймати наступні аргументи: ім’я, ЗП за один робочий день.
# 3. Створити метод work(self, …) який повертає строку “I come to the ofﬁce.”
# 4. Створити класи Recruiter та Developer, які наслідують клас Employee.
# 5. Перевизначити методи work  в класах R та D, щоб вони повертали значення:
# a. “I come to the ofﬁce and start to coding.” - для Developer
# b. “I come to the ofﬁce and start to hiring.” - для Recruiter
# 6. Перевизначити методи  __str__, щоб они повертали строку: “Посада: Ім’я”
# 7. Зробити можливим порівнювати Employee по рівню ЗП.
# 8. Створити метод check_salary(self, days), який розраховує ЗП за передану кількість днів.
# 9. ** Зробити можливим, щоб метод check_salary рахував ЗП з початку місяця до поточного дня,
# не враховуючи вихідні дні.
# 10. Додати в конструктор класу Developer атрибут tech_stack (список з назвами технологій).
# 11. Для класу Developer зробити порівняння за кількістю технологій.
# 12. Зробити можливим операцію додавання об’єктів класу Developer. Результатом має бути
# новий об’єкт
# В якому name = name1 + ‘ ’ + name2, a tech_stack - список з технологій двох об’єктів (тільки
# унікальні значення), ЗП - більша з двох.
# 13. Залити на git.
# 14. Відправити посилання @ivnuk.


import datetime


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def work(self):
        return "I come to the office."

    def check_salary(self, days_date=None):

        if isinstance(days_date, int):
            return days_date * self.salary
        else:
            if isinstance(days_date, datetime.datetime):
                day_now = days_date
            else:
                day_now = datetime.date.today()

            sum_days = 0
            for d in range(0, day_now.day):
                date_iter = day_now - datetime.timedelta(days=d)
                if date_iter.isoweekday() < 6:
                    sum_days += 1

            return sum_days * self.salary

    # ---compare salary-----------
    def __lt__(self, other):
        return self.salary < other.salary

    def __le__(self, other):
        return self.salary <= other.salary

    def __gt__(self, other):
        return self.salary > other.salary

    def __ge__(self, other):
        return self.salary >= other.salary

    def __eq__(self, other):
        return self.salary == other.salary

    def __ne__(self, other):
        return self.salary != other.salary
    # --------------


class Recruiter(Employee):
    def __str__(self):
        return 'Recruiter : ' + self.name

    def work(self):
        return super().work()[:-1] + " and start to hiring."


class Developer(Employee):
    def __init__(self, name, salary, tech_stack):
        super().__init__(name, salary)
        self.tech_stack = tech_stack

    def __str__(self):
        return 'Developer : ' + self.name

    def __add__(self, other):
        return Developer(name=self.name + ' ' + other.name
                         , salary=max(self.salary, other.salary)
                         # все что уникально в двоих списках
                         # ,list(set(de_Dmitro.tech_stack) ^ set(de_Petro.tech_stack))

                         #  сложить списки и убрать дубли , похоже это нужно в задании
                         , tech_stack=list(set(self.tech_stack) | set(other.tech_stack)))

    def work(self):
        return super().work()[:-1] + " and start to coding."

    # ---compare tech_stack-----------
    def __lt__(self, other):
        return len(self.tech_stack) < len(other.tech_stack)

    def __le__(self, other):
        return len(self.tech_stack) <= len(other.tech_stack)

    def __gt__(self, other):
        return len(self.tech_stack) > len(other.tech_stack)

    def __ge__(self, other):
        return len(self.tech_stack) >= len(other.tech_stack)

    def __eq__(self, other):
        return len(self.tech_stack) == len(other.tech_stack)

    def __ne__(self, other):
        return len(self.tech_stack) != len(other.tech_stack)
    # --------------


if __name__ == '__main__':
    re_Artem = Recruiter('Artem', 100)
    print(re_Artem)
    print(re_Artem.work())

    de_Petro = Developer('Petro', 200, ['python', 'java'])
    print(de_Petro)
    print(de_Petro.work())

    re_Ira = Recruiter('Ira', 1100)
    print(re_Artem > re_Ira)

    print("sallary - ", re_Artem.check_salary(days_date=11))
    # current date
    print("sallary - ", re_Artem.check_salary())
    print("sallary - ", re_Artem.check_salary(datetime.datetime(2022, 11, 2)))

    de_Dmitro = Developer('Dmitro', 200, ['python', 'java', 'C++'])
    print(de_Dmitro)
    print(de_Dmitro > de_Petro)

    de_new_my_add = de_Petro + de_Dmitro
    print(de_new_my_add)
