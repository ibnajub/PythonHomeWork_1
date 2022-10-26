
# Банкомат выдает сумму максимально возможными купюрами

nominal = [5,10, 20, 50, 100, 200, 500, 1000]

summa = 10995  # int(input())  требуемая сумма к выдаче

summOstatok = summa
summaResultDict = {}    #результат в словарь
nominalDlina = len(nominal) - 1


while nominalDlina >= 0:    # обход списка номиналов с конца
    # print( nominal[nominalDlina] )
    tekNominal = nominal[nominalDlina]
    while summOstatok - tekNominal >= 0:    # минусуем тек номинал и пишем рез в словарь
        summOstatok -= tekNominal
        dictItemName = "Номинал выдачи " + str(tekNominal)
        if summaResultDict.get(dictItemName) == None :
            summaResultDict[dictItemName] =  tekNominal
        else:
            summaResultDict[dictItemName] += tekNominal

    nominalDlina -= 1

print("Запрошено:", summa,", Не выдано:", summOstatok,", Выдано купюр:", summaResultDict)