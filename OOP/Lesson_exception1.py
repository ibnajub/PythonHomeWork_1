# 1. Додати до класу Employee методи save_email(self) та validate(self) та атрибут email
# 2. Створити виняток EmailAlreadyExistsException
# 3. Метод save_email має викликатись в кінці методу __init__ та записувати email в файл emails.txt
# 4. Метод validate має перевіряти чи існує імейл в файлі. Якщо імейл вже існує, то викликати помилку
# EmailAlreadyExistsException
# 5. В головному файлі програми (app.py або main.py) весь код, який знаходиться в блоці
# if __name__ == ‘__main__’ перенести в нову функцію main() і викликати цю функцію в
# name == main блоці.
# 6. Огорнути виклик функції main() в блок try/except.
# У разі виникнення винятку EmailAlreadyExistsException записати в файл logs.txt повідомлення у
# вигляді: %дата% %час% | %traceback%


import Lesson_2_Pract
import expection_class


class Employee_exp(Lesson_2_Pract.Employee):
    def __init__(self, name, salary, email):
        super().__init__(name, salary)
        self.email = email
        self.save_email()

    def save_email(self):
        self.validate()
        with open('emails.txt', 'a+') as fl:
            fl.write(f'{self.email}' + '\n')

    def validate(self):
        with open('emails.txt', 'r') as fl:
            for i in fl:
                if self.email in i.split():
                    raise expection_class.EmailAlreadyExistsException()


def main():
    exp_emp = Employee_exp('Artem', '1000', 'sasss@gmail.com')
    print(exp_emp)


if __name__ == '__main__':
    main()
