# Практика
# Створити клас, який буде описувати властивості хімічного елементу.
# 1. Для класу має бути описаний метод __init__(...), який приймає два параметри:
# температура плавлення та температура кипіння.
# 2. В класі має бути описаний метод, який в якості аргумента отримує температуру (в градусах
# цельсія) та повертає строку, яка відповідає агрегатному стану речовини при цій
# температурі.
# 3. * Додати в клас метод, який приймає в якості аргументів температуру (число) та назву
# шкали виміру (“C” / “F” / “K”) та конвертує її в градуси цельсія.
# 4. * Зробити можливим передавати температуру та шкалу в метод з п.2


class Ellem:
    def __init__(self, t_melting, t_boiling):
        self.t_melting = t_melting
        self.t_boiling = t_boiling

    def convert_state(self, temp, t_melting = None, t_boiling= None):
        # запихнуть в def не дает так написать -- t_melting =self.t_melting
        # NameError: name 'self' is not defined
        t_melting = t_melting if t_melting != None else self.t_melting
        t_boiling = t_boiling if t_boiling != None else self.t_boiling
        if temp < t_melting:
            return 'solid'
        if temp > t_boiling:
            return 'vapour'
        return 'liquid'

    def convert_temp(self, temp, scale='C'):
        if scale == 'K':
            return temp - 273
        if scale == 'F':
            return (temp - 32) * 5 / 9
        return temp


if __name__ == '__main__':
    fe = Ellem(0, 100)
    print(fe.convert_state(-100))
    print(fe.convert_temp(100, 'K'))
    print(fe.convert_state(-100, -1000,100))
