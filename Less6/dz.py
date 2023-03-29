# task 1
# func = lambda x = int(input()): print('even') if x % 2 == 0 else print('not even')
# func()
# task 2
# list_ = [1, 6, 67, 2, 5, 6]
# print(list_)
# task 2
# transfer_str = list(map(lambda num: str(num), list_))
# print(transfer_str)
# task 3
# tuple_ = ['aba', 'acc', 'coc', 'kek']
# polimor_tuple = tuple(filter(lambda x: x[::-1] == x, tuple_))
# print(polimor_tuple)
# task 4
# from datetime import datetime
# import time
#
#
# def wrapper(func):
#     def inner(*args, **kwargs):
#         star = datetime.now()
#         e = func(*args, **kwargs)
#         time.sleep(1)
#         end = datetime.now() - star
#         return e, str(end)
#
#     return inner
#
#
# @wrapper
# def summa(a, b):
#     return a + b
#
#
# print(summa(5, 5))
# task 5
def el_check(el):
    if isinstance(el, list):
        for e in el:
            el_check(e)
    else:
        if el[0] == '-' and el[1:].isdigit():
            print(f"Вы ввели отрицательное целое число {el}")
        elif '.' in el and el[0] != '-':
            first, second = el.split('.')
            if first.isdigit() and second.isdigit():
                print(f"Вы ввели дробное число {el}")
        elif el[0] == '-' and '.' in el:
            first, second = el[1:].split('.')
            if first.isdigit() and second.isdigit():
                print(f"Вы ввели отрицательное дробное число {el}")
        elif el.isdigit():
            print(f"Вы ввели положительное целое число {el}")
        else:
            print(f"Вы ввели некоректное число {el}")


el_check(['123', '-123', '12.3', 'asdasdweq', '-12.3'])
