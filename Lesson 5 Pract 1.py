
# Задание 1
# Написать 2 функции. Первая функция будет принимать строку и приводить ее к нижнему регистру.
# Вторая функция будет принимать строку и проводить ее к верхнему регистру.
# После чего с помощью map применить ваши функции к списку строк. Отдельно каждую функцию к отдельному списку строк!

def low(Text: str):
    '''low dfdf'''
    return Text.lower()

def up(Text: str):
    '''up dsddd'''
    return Text.upper()

listText = ["sdDsDF","SDfcvdfDF"]
new_Text = list(map(low,listText))
new_Text1 = list(map(up,listText))
print(new_Text)
print(new_Text1)
