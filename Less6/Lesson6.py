# dz


# def check_is_positive(num: int) -> bool:
#     if num > 0:
#         return True
#     else:
#         return False
#
#
# print(check_is_positive(int(input())))
#
#
# def check_is_positive(num: int) -> bool:
#     return num > 0
# #
#
# print(check_is_positive(int(input())))
################################################################


# def print_numbers(numbers: list) -> None:
#     for number in numbers:
#         result = 'положительное' if check_is_positive(number) else 'отрицательное'
#         print(f'{number}: {result}')
#         if check_is_positive(number):
#             print(f'{number}: положительное')
#         else:
#             print(f'{number}: отрицательное')


# print_numbers([-2, 1, 4, -5])
############################################################################################
import random
#
# print(random.randint(-10, 10))
# list_ = []
# n = 10
# for _ in range(n):
#     list_.append(random.randint(-10, 10))
# print(list_)
#
# list_ = [random.randint(-10, 10) for _ in range(n)]
# print(list_)

# symbol = ['a', 'g', '4', 'p', 'k']
# print([random.choice(symbol) for i in range(100)])
#
# random_dict = {s: random.randint(-10, 10) for s in symbol}
# print(random_dict)

# рекурсия
# def foo():
#     print('in foo')
#     foo()
#
#
# foo()


# 0, 1, 1, 2, 3, 5, 8, 13, ...
# 0, 1, ..., (n-1) + (n -2) - n-ый элемент
# def get_fib(n):
#     if n in {0, 1}:
#         return n
#     return get_fib(n - 1) + get_fib(n - 2)
#
#
# print(get_fib(0))
# print(get_fib(1))
# print(get_fib(5))
# print(get_fib(6))
# print(get_fib(7))
# print(get_fib(8))


# a = 'abcb'
# b = 'abc'
#
#
# def foo(a: str, b: str) -> bool:
#     if len(a) < len(b):
#         return foo(b, a)
#
#
# foo(b, a)


# dict_ = {'a': 1, 'b': 2, 'c': 3}


# def change_dict(dict: dict) -> dict:
#     new_dict = {}
#     for key in dict_:
#         print(dict_[key])
#         new_dict[dict_[key]] = key
#     return new_dict
#
#
# print(change_dict(dict_))
# dict_2 = {dict_[key]: key for key in dict_}
# print(dict_2)
###############################################
# 3! = 1 * 2 * 3

# def fact(number: int) -> int:
#     if number < 0:
#         return number
#     if number == 1 or number == 0:
#         return 1
#     return number * fact(number - 1)
#
#
# print(fact(0))
##################################################


# def add(a: int, b: int) -> int:
#     """Вовращает сумму двух чисел
#
#     :param a: Целое число
#     :param b: Целое число
#     :return: Сумму а и b
#     """
#     return a + b
#
#
# print(help(add))


# map, filter
# list_ = [-2, 4, 1, 12, -22]
# positive_list = [item for item in list_ if item > 0]
# print(positive_list)
# print(list_)
#
#
# def is_posotive(num: int) -> bool:
#     return num > 0
#
#
# positive_list2 = list(filter(is_posotive, list_))
# print(positive_list2)
#
# #lambda fuctions
# positive_list3 = list(filter(lambda num: num > 0, list_))
# print(positive_list3)
#
# print(list(filter(lambda num: num < 0, list_)))
# print(list(filter(lambda num: num % 2 == 0 and num > 0, list_)))
#
# new_list = []
# for num in list_:
#     if num % 2 == 0 and num > 0 and num % 3 == 0:
#         new_list.append(num)
# print(new_list)


# import random as r
#
# print(r.randint(-5, 5))

# list_ = [-2, 4, 1, 12, -22]
# print(list(map(lambda num: num ** 2, list_)))
# print(list(map(lambda num: num > 0, list_)))
#
# # num1, num2 = map(int, [input('первое число '), input('Второе число ')])
# # print(num1, num2, type(num1), type(num2))
#
# numbers_string = input('Введите числа через пробел: ')
# numbers = list(map(int, numbers_string.split()))
# print(numbers)

# legb
# local, enclosing, global, built-in


# def foo():
#
#     def inner():
#         print('in inner function')
#     return inner


# Closure, замыкание
# def add(a, b):
#     return a + b
#
# def add_one(a):
#     return 1 + a

# функция add высшего порядка
# def add(a):
#     def inner(b):
#         return a + b
#     return inner


# add_one = add(1)
# print(type(add_one))
# print(add_one(2))
# print(add_one(5))
#
#
# add_five = add(5)
# print(add_five(2))
# print(add_five(7))
import time
from functools import wraps
from typing import Callable


def decorator(func: Callable) -> Callable:
    @wraps(func) # сохраняем имя и документацию изначальной функции, для которой мы
    def inner(*args, **kwargs):
        print('до вызова функции add')
        time1 = time.time()
        result = func(*args, **kwargs) # вот тут мы вызываем функци, которую декорируем (в нашем случае это add)
        time2 = time.time()
        print(f'после вызова add, результат ={result}, время выполнения = {time2 - time1}')
        return result
    return inner


@decorator
def add(a, b):
    return a + b

@decorator
def print_list(list_: list):
    """Выводит список на консоль"""
    print(list_)


print_list([1, 2, 3])
print(print_list.__doc__)
print(print_list.__name__)

# add = decorator(add)  # @decorator
# print(add(2, 3))
# print(add.__name__)
# # print(add(2, 3))

# t1 = time.time()
# add(2, 3)
# print(time.time() - t1)


def add(*args):
    print(args)
    return sum(args)


# list_ = [2, 4, 1, 5]
# print(add(*list_))
