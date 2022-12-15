# Создать словарь оценок предполагаемых студентов (Ключ - ФИ студента, значение - список оценок студентов). Найти самого успешного и самого отстающего по среднему баллу.

gurnalOcenki = {"Петров Вася": [10,12,5,6,7,3], "Петров Миша": [10,12,12,10,12], "Иванова Маша": [10,12,5,6,7,4]}
# gurnalOcenki = {"Петров Вася": [10,12,5,6,7,3] }
# gurnalOcenki = { }


# sredneeStudentDict = { }
# resultDict = {}
# averagetList = []

valMax = 0
keyMax = ""

valMin = 0
keyMin = ""

# итератор от словаря
# for student in gurnalOcenki:
#     srednBal = sum( gurnalOcenki[student] ) / len(gurnalOcenki[student])

# итератор ключь-значение
first_iter = True
for student, ocenki in gurnalOcenki.items():
    srednBal = sum(ocenki) / len(ocenki)
    print(student, srednBal)
    # resultDict[student] = srednBal
    # averagetList.append(srednBal)
    if valMax < srednBal:
        valMax = srednBal
        keyMax = student
    if first_iter:
        valMin = valMax
        first_iter = False

    if valMin > srednBal:
        valMin = srednBal
        keyMin = student

# averagetList.sort()

print("Max:", keyMax, valMax)
print( "Min:", keyMin, valMin)
# print(invert_gurnalOcenki)





