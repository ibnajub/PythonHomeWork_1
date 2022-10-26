# Задание 2
#
# Написать функцию которая будет простое число возводить в квардрат.
#
# Необходимо возвести в квадрат все простые числа в списке используя функцию map

def sqe(x: int):
    '''sqe int'''
    return x * x


def prostie_chisla(x: int):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


spis = [1, 2, 3, 4, 5, 7, 10,11]

print(list(range(2, 3)))
print(spis)
print(tuple(map(prostie_chisla, spis)))
print(list(map(sqe, filter(prostie_chisla, spis))))
