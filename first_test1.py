def spam(number):
    '''Function should return something like this:
    spam(1);#bulochka
    spam(3);#bulochkabulochkabulochka
    But it is broken. Fix it please!

    Эта функция принимает числовой параметр. Должна вернуть строку, которая
    повторяется столько раз, сколько параметров передано. Она уже написана,
    но не работает. Любым способом заставьте ее работать.
    '''
    # 'bulochka' for i in range(number + 1)]
    return 'bulochka' * number


def my_sum(list_of_numbers):
    """Function receives a list with integer numbers,
    should return its sum as an integer. Do not use built in summarize functions.
    :param list

    Функция получает на вход массив чисел, должна вернуть сумму этих чисел.
    Не использовать встроенные функции суммирования.
    
    """
    pass
    #  ...wite your code here
    import functools
    return functools.reduce(lambda x, y: x+y , list_of_numbers )

def shortener(string ):
    """
    Function receives a long string with many words.
    It should return the same string, but words,
    larger then 6 symbols should be changed, symbols
    after the sixth one should be replaced by symbol *
    :param string
    :returns string

     Функция получает на вход длинную строку с множеством слов.
     Она должна вернуть ту же строку, но в словах, которые длиннее 6 символов,
     функция должна вместо всех символов после шестого поставить одну звездочку.
     Пример: Из слова 'verwijdering' должно получиться 'verwij*'


    """
    pass
    #  ...wite your code here
    # s =  (i[:6] + "*") for i in string.split()
    # for x in string.split()
    #     if len(x) > 6:
    #        x=
    #     ' '.join([(if len(x) > 6: (x[:6] + "*") else:  x)
    # s = (if len(x) > 6: (x[:6] + "*") else:  x)

    # res= ''
    # one = True
    # for x in string.split():
    #     if one:
    #         one = False
    #     else:
    #         res += ' '
    #     if len(x) > 6:
    #         res +=  x[:6] + "*"
    #     else:
    #         res +=  x


    # fun_i = lambda i: i[:6] + "*" if len(i) > 6 else i
    # return  ' '.join ( list( map(fun_i, string.split() ) ) )

    return  ' '.join ( [ ( (i[:6] + "*") if len(i) > 6 else i) for i in string.split()   ])


def compare_ends(words):
    """
    Function receives an array of strings.
    Please return number of strings, which
    length is at least 2 symbols and first character
    is equal to the last character

    Функция получает на вход массив строк. Вернуть надо количество строк,
    которые не короче двух символов и у которых первый и последний
    символ совпадают.

    """
    pass
    #  ...wite your code here
    # import functools
    res = 0
    for word in words:
        if len( word ) > 1 and  word[0]  == word[-1]:
           res += 1

    return res
