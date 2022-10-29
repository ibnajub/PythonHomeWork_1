# Задача 2. Бриллиант
#
# Входным данным является целое число. Необходимо:
#
# написать проверку, чтобы в работу пускать только положительные нечетные числа
# для правильного числа нужно построить бриллиант из звездочек или любых других символов и вывести его в консоли. Для числа 1 он выглядит как одна взездочка, для числа три он выглядит как звезда, потом три звезды, потом опять одна, для пятерки - звезда, три, пять, три, одна...


number_input = 25

def zvezda(number_):
    result = ''
    x = number_ - 1
    if number_ % 2 != 0 and number_ > 0:
        # for i in range(1, number_ + 1),  reversed( range(1, number_)  :
        for i in range(1, number_ + 1):
            if i % 2 != 0:
                res = int(i) * '*'
                probelov = int((number_ - i) / 2)
                # print(probelov * '.' + res + probelov * '.')
                result += probelov * '.' + res + '\n'
                # print(res,probelov)
        # нижняя часть звезды
        while x > 0:
            if x % 2 != 0:
                res = int(x) * '*'
                probelov = int((number_ - x) / 2)
                # print(probelov * '.' + res + probelov * '.')
                result += probelov * '.' + res + '\n'
            x -= 1
    return result


print(zvezda(number_input))
