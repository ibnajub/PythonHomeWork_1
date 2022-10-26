# Банкомат выдает сумм мелкими, но не больше 10 штук каждой мелкой купюры

nominal = [5, 10, 20, 50, 100, 200, 500, 1000]

summa = 10995  # int(input())  требуемая сумма к выдаче

maxKupurNominala = 10
summOstatok = summa
summaResultDict = {}  # результат в словарь, учимся работать с словарями, в реальности результат должен падать в БД
summVidano = 0  # для сверки что все ок

for tekNominal in nominal:  # обход списка номиналов с начала
    # print( tekNominal )
    tekKupurNominala = maxKupurNominala  # пересоздаем счетчик макс выдачи
    # минусуем тек номинал и пишем рез в словарь , учитываем счетчик выдачи купюр
    while summOstatok - tekNominal >= 0 and tekKupurNominala > 0:
        summOstatok -= tekNominal
        dictItemName = "Номинал выдачи " + str(tekNominal)
        if summaResultDict.get(dictItemName) == None:
            summaResultDict[dictItemName] = tekNominal
        else:
            summaResultDict[dictItemName] += tekNominal
        tekKupurNominala -= 1
        summVidano += tekNominal  # для сверки что все ок


print("Запрошено:", summa, ", Не выдано:", summOstatok, "Выдано купюрами:", summVidano, " Проверка: ",
      summOstatok + summVidano)
print("Выдано купюр:", summaResultDict)
