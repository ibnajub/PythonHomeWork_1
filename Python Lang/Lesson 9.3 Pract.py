# Задача 3. Файл-тест. Есть файл, в котором хранятся числа в следующем формате:
#
# 2 4 5;3 2
# 3 2 1;2 0
# 6 5 2 1 2;3 1
# .....
# Цифры до точки с запятой надо суммировать, потом делить на их количество. В первой строке сумма будет 11, разделить на
# их количество, т.е. на 3, получается 3 целых и в остатке 2. Аналогичным образом во второй строке 6 делим на три, ровно
# два и в остатке ноль, в третьей строке сумма 16, на 5 делим, получаем 3 и 1 в остатке. Вот так:
#
# 2 4 5;3 2                 2+4+5/3 = 3, в остатке 1
# 3 2 1;2 0                 3+2+1/3 = 2, в остатке 0
# 6 5 2 1 2;3 1         6+5+2+1+2/5 = 3, в остатке 1
# .....
# Задача: проверить каждую строку файла, если строка записана верно, вывести ее и после написать True, если строка не
# верна, вывести результат с пометкой False.
import functools
filename = "Lesson 9.3 Pract.txt"
# чтение файла и обработка его в физ басс
f = open(filename, 'r')  # в файле теперь file descriptor
for line in f:  # для каждой строки в файле
    stroka0 = line.split(';')
    stroka_left =  stroka0[0].split()
    stroka_left_summ = functools.reduce(lambda x, y: int(x)+int(y) ,stroka_left )
    stroka_rez = list(map(int, stroka0[1].split()))
    stroka_rez_calc_1 = (stroka_left_summ) // len(stroka_left)
    stroka_rez_calc_2 = (stroka_left_summ) % len(stroka_left)
    if (stroka_rez_calc_1 == stroka_rez[0] and stroka_rez_calc_2 == stroka_rez[1]):
        print( stroka_left, 'True')
    else:
        print(stroka_rez_calc_1,stroka_rez_calc_2 ,'False')
    # udachno = True if (stroka_rez_calc_1 == stroka_rez[0] and stroka_rez_calc_2 == stroka_rez[1]) else False
    # print(udachno)

f.close()  # закрытие файла


# вариант саши
import pathlib

def filedata(file):
    if pathlib.Path(file).exists():
        with open(file) as f:
            for line in f.readlines():
                l = ''.join([x.strip() for x in line if x !=' '])
                before, after = l.split(';')
                sum_res = sum([int(x) for x in before])
                if sum_res // int(len(before)) == int(after[0]) and sum_res % int(len(before)) == int(after[-1]):
                    print(f'{before};{after} => true')
                else:
                    print(f'{before};{after} => false')
    else:
        file = input('File doesnt exist, Enter correct file name: ')
        filedata(file)

file = 'test.txt'
filedata(file)