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
    def __int__(self, t_melting, t_boiling):
        self.t_melting = t_melting
        self.t_boiling = t_boiling

    def convert_state(self, temp):
        if temp < self.t_melting:
            return 'solid'
        if temp > self.t_boiling:
            return 'vapour'
        return 'liquid'

    def convert_temp(self, temp, scale='C'):
        if scale == 'K':
            return temp - 273
        if scale == 'F':
            return (temp - 32) * 5 \ 9
        return temp


if __name__ == '__main__':
    fe = Ellem()
    # print(fe.)
