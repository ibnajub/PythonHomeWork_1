# Третий уровень ("Мистер Буль. Джордж Буль!"):
#
# Решить задачу:
#
# Задача fizz-buzz:
#
# У вас есть три числа, они вводятся из консоли. Первое число называется fizz, второе называется buzz. До третьего
# необходимо досчитать от единицы. Считая, надо выводить число. Если число кратно fizz - надо выводить F вместо числа.
# Если число кратно buzz - надо выводить B вместо числа. Если число кратно и fizz и buzz, надо выводить FB.
# И так - пока не будет достигнуто третье введенное число.
#
# Пример условия и результата:
# Введены числа 2, 5, 18
# Вывод должен быть таким:
# 1 F 3 F B F 7 F 9 FB 11 F 13 F B F 17 F

# fizz buzz

print("input 1 number:")
fizz = int(input())

print("input 2 number:")
buzz = int(input())

print("input 3 number:")
fizz_buzz = int(input())

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
