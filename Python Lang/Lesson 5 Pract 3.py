# Задание 3
#
# Вспоминаем работу с файлом. Есть файл, в котором много англоязычных текстовых строк. Считаем частоту встретившихся слов в файле, но через функции и map, без единого цикла!
import functools

filename = "Lesson 5 Pract 3.txt"
fileP = open(filename, 'r')

findText = "in"

#  если писать свою функцию то будет проблема тк ей некак передать 2 аргумент findText
# s.split().count(findText) - конвертит строку  в список слов list, а потом сразу же считает сколько раз
# встретилось слово в списке

print("Проверка, список строк с количеством повторений слова - "
      + str(list(map(lambda s: s.split().count(findText), fileP))))

fileP.seek(0)  # после print ставим курсор в начало файла иначе ошибка тк fileP спозиционировался на конец файла

# сворачиваем список через reduce
print(functools.reduce(lambda x, y: x + y, list(map(lambda s: s.split().count(findText), fileP))))

fileP.close()
