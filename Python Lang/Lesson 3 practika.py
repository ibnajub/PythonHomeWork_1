import sys

# -----------------------------------------------------------------------
# Написать программу, которая выводит саму себя

filename = sys.argv[0]
# далее открываем файл на чтение (опция 'r')
f = open(filename, 'r', encoding="utf-8") # в файле теперь file descriptor
for line in f: # для каждой строки в файле
	print(line, end="")
f.close() # закрытие файла

# -----------------------------------------------------------------------
# Написать программу, которая выводит саму себя задом наперед

f = open(filename, 'r', encoding="utf-8") # в файле теперь file descriptor
spis = f.readlines()
spis.reverse()
for i in spis:
    print(i[::-1], end="")

# через seek чето нифига так и не получилось ((
# f.seek(0,2) # в конец строки
# size = f.tell() #размер вроде бы
# seek_adres = size-1
# while seek_adres > 0:
#     f.seek(seek_adres,0)
#     print( f.read(1) )
#     seek_adres -= 1
f.close() # закрытие файла