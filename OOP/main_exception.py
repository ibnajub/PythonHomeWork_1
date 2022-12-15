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


import Lesson_exception1 as lesson_exception
import expection_class

try:
    lesson_exception.main()
#     если писать "as ex", то "ex" это будет объект класса, а если без него
#     except lesson_exception.EmailAlreadyExistsException:  -- это класс(!), а не объект(!)
except expection_class.EmailAlreadyExistsException as ex:
    with open('logs.txt','a+') as fl:
        fl.write(f"{ex.date} | "
                 f"{ex.traceback}" +'\n' )
except Exception:
    pass
else :
    pass

