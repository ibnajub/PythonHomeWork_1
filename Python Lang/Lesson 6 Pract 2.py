# Создать структуру данных для студентов из имен и фамилий, можно случайных. Придумать структуру данных, чтобы указывать
# , в какой группе учится студент (Группы Python, FrontEnd, FullStack, Java). Студент может учиться в нескольких группах. Затем вывести:
#
#     студентов, которые учатся в двух и более группах
#     студентов, которые не учатся на фронтенде
#     студентов, которые изучают Python или Java

manyKeys = {}
frontend = {}
learn_python_java = {}

klaswDict = {"Петров Вася": {'Python', 'FrontEnd'}, "Петров Миша": {'Python', 'Java'}, "Иванова Маша": {'FullStack'}}

for key, value in klaswDict.items():
    if len(value) > 1:
        manyKeys[key] = len(value)

    # чтоб не делать сравнение множеств два раза присвоим результат промеж перемен
    frontend1 = not {'FrontEnd'} & value
    if frontend1:
        frontend[key] = frontend1

    learn_python_java1 = {'Python', 'Java'} & value
    if learn_python_java1:
        learn_python_java[key] = learn_python_java1

print('студентов, которые учатся в двух и более группах- ', manyKeys)
print('студентов, которые не учатся на фронтенде- ', frontend)
print('студентов, которые изучают Python или Java- ', learn_python_java)
