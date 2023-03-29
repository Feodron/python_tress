# dz
# lambda number: 'четное' if number % 2 == 0 else 'нечетное'
# print(list(map(lambda number: 'четное' if number % 2 == 0 else 'нечетное',[2, 3, 4, 5])))
#
# numbers = [1, 2, 3, 4]
# print(list(map(lambda number: str(number), numbers)))
#
# strings = ('oko', 'helli', 'ervre', ' by')
# print(list(filter(lambda string: string == string[::-1], strings)))

# TDD - test driven development


# test_cases = [
#     '1', '-1', '0.1', '-0.1', '.1', '-.1', '0'
#     'a', '', '1aq', '--1', '1-', '1..1', '0.1a', '12 12', '-a12', '..1', '-...'
# ]
#
#
# def analyze_str(num_str: str) -> int | float | None:
#     if num_str.isdigit():
#         print(f'полложительное целое {num_str}')
#         return int(num_str)
#     cleaned_num_str = num_str.replace('-', '', 1).replace('.', '', 1)
#     if not cleaned_num_str.isdigit() or ('-' in num_str and num_str != '-'):
#         print(f'некорретное число {num_str}')
#         return None
#     if '.' in num_str:
#         num_type = 'дробное'
#         num = float(num_str)
#     else:
#         num_type = 'целое'
#         num = int(num_str)
#     if num >= 0:
#         num_sign = 'положительное'
#     else:
#         num_sign = 'отрицательное'
#     print(f'{num_sign} {num_type} {num_str}')
#     return num
#
#
# def analyze_str2(num_str: str) -> int | float | None:
#     if num_str.isdigit():
#         print(f'полложительное целое {num_str}')
#         return int(num_str)
#     cleaned_num_str = num_str.replace('-', '', 1).replace('.', '', 1)
#     if not cleaned_num_str.isdigit() or ('-' in num_str and num_str != '-'):
#         print(f'некорретное число {num_str}')
#         return None
#     if '.' in num_str and num_str[0] == '-':
#         print(f'отрицательное дробное {num_str}')
#     if num_str[0] == '-':
#         print(f'отрицательное целое {num_str}')
#         return int(num_str)
#     print(f'положительное дробное {num_str}')
#     return float(num_str)

# for num_str in test_cases:   # 1 способ
#     print(analyze_str(num_str))

# print(list(map(analyze_str, test_cases)))   # 2 способ

# print([analyze_str2(num_str) for num_str in test_cases])    # № 3 способ
############################################################################################
#from functools import wraps
#from typing import Callable
#
#
# def validate_one_int_arg(func: Callable) -> Callable:
#     @wraps(func)
#     def inner(number: int) -> any:   # заменяет декора
#         if type(number) != int:
#             print('Ошибка! Введенные данные не являются числом')
#             return
#         return func(number)
#     print('Выполняем код функции validate_one_int_arg')
#     return inner    # inner - это объект типа функции(в нашеи случае это is_even)
#
#
# @validate_one_int_arg
# def is_even(number: int) -> bool | None:
#     return number % 2 == 0


# @validate_one_int_arg
# is_even = validate_one_int_arg(is_even)
# print(type(is_even))


# print(is_even(2))
# print(is_even('12'))
# print(is_even(3))


# def print_func_call_time(func: Callable) -> Callable:
#     print(f'Вызываем функцию {func.__name__}в {datetime.datetime.now()}')
#     return func


# @print_func_call_time  # Время выполнение этой строки
# def print_numbers():
#     for num in range(10):
#         print(num, end=" ")
#     print()


# print_numbers()
# print_numbers()
# print_numbers()
######################################################################


#def cache(func: Callable) -> Callable:
#    print('Создаем пустой словарь...', end=' ')
#    cached_data = {} # вложенная для inner (или enclosing область видимости )
#    print('Создали')
#    @wraps(func)
#    def inner(*args, **kwargs):
#        # {(2, 3): 5, (3, 3): 6, ...}
#        print(f'{cached_data}')
#       if args in cached_data:
#            return cached_data[args]
#       result = func(*args, **kwargs)
#        cached_data[args] = result
#       return result
#    return inner


# @cache
# def add(a: int, b: int) -> int:
#     print('Выполняем тело функции add')
#     return a + b
#
#
# @cache
# def print_nums(n: int) -> None:
#     print('Делаем что-то сложное, делаем долго..')


# print(add(2, b=3))  # здесь выполняем тело функции add
# print(add(3, 3))  # здесь выполняем тело функции add
# print(add(2, 3))  # здесь берем значение готовое из словаря
#
# print_nums(2)
# print_nums(1)
# print_nums(3)


# cache_data = {}
# nums = [1, 2]  # unhachable
# cache_data[nums] = 'список'
# print(cache_data)

# print(hash(1))
# print(hash(2))
# print(hash('s'))
# print(hash([1, 2]))


# Кодировки и файлы
# s = 'a'
# symbol_code = ord(s)
# print(symbol_code)
# print(chr(symbol_code))
# print(chr(12786))

file = open('hello.txt')
# file_text = file.read(5)  # прочитать 5 символов из файла
# print(file_text)

#
# for row in file:
#     print(f'прочитали строку: {row}')

# print(file.readline())
# print(file.readline())
# print(file.readline())

file.close()

#  контекстный  менеджер
with open('hello.txt') as file:
    file_text = file.read()
    print(file_text)

print('вышли из контекстного менеджера')
file.read(5)
