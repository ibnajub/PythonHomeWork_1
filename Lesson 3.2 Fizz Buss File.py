# Написать fizzbuzz для 20 троек чисел, которые записаны в файл. Читаете из файла первую строку, берете из нее числа,
# считаете для них fizzbuzz, выводите, повторяете со всеми остальными строками.

import random

# create file
# создаем файл с 20 строками рандомных чисел
filename = "Lesson 3.2 Fizz Buss File.txt"
f = open(filename, 'w')  # в файле теперь file descriptor
sVal = ""
for i in range(0, 20):
    sVal += str(random.randint(1, 100)) + " " + str(random.randint(1, 100)) + " " + str(random.randint(1, 100)) + "\n"

f.write(sVal)
f.close()  # закрытие файла

# чтение файла и обработка его в физ басс
f = open(filename, 'r')  # в файле теперь file descriptor
for line in f:  # для каждой строки в файле
    print("старт физ басс для чисел - " + line, end="")
    fizbus_list = line.split()
    if len(fizbus_list) != 3:
        continue

    # fizz buzz ----START
    fizz = int(fizbus_list[0])
    buzz = int(fizbus_list[1])
    fizz_buzz = int(fizbus_list[2])

    result_fizz_buzz = ""
    for i in range(1, fizz_buzz + 1):
        if (i >= fizz and (i % fizz == 0)) and (i >= buzz and (i % buzz == 0)):
            result_fizz_buzz += "FB"
        elif (i >= fizz) and (i % fizz == 0):
            result_fizz_buzz += "F"
        elif (i >= buzz) and (i % buzz == 0):
            result_fizz_buzz += "B"
        else:
            result_fizz_buzz += str(i)

        if i < fizz_buzz:
            result_fizz_buzz += " "
    print(result_fizz_buzz)
# fizz buzz ----Finish

f.close()  # закрытие файла
