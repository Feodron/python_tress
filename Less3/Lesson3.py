# num = int(input())
# print(num)
# print(type(num))

# num = 5
# num = 2
# print(int(2.8))

# num = float(2)
# print(num)

# print(bool(1))
# print(bool(0))
# print(bool(0.0))
# print(bool(0.5))
# print(bool(int(0.5)))
# print(bool(256))
# print(bool(-256))

# print(bool('123'))
# print(bool(''))
# print(bool(' '))

# print(bool([1]))
# print(bool([]))
# print(bool([set()]))
# print(bool([0]))

# print((bool({'a': 1})))
# print(bool({}))

# num =1
# num1 = 2
# print(str(num) + str(num1))
# print(str(num) + str(num1))
# print(str([1, 2, 3]))

# list, tuple
# list_ = list("abc")
# print(id(list_))
# list_ = list({1, 2, 3})
# list_2 = list(list_)
# print(id(list_))
# list_2.append("d")
# print(list_)
# print(list_2)
#
# list_3 = list_2[:]
# print(list_3)
# print(id(list_3))

# tuple_ = tuple("123")
# tuple_2 = tuple({1: 'a', 2: 'b'})
# d = {1: 'a', 2: 'b'}
# print(d.keys())
# tuple_ = tuple(d)
# list_ = list(d)
# print(tuple_)
# print()
# Задание
# friends_phone_number = {
#     'Egor': 123,
#     'Liza': 555,
#     'Vanya': 908,
#     'Yana': 150,
# }
# friends_names = list(friends_phone_number)
# print(friends_names)
# del friends_names[1]
# friends_names.remove('Liza')
# friends_names.pop(1)
# print(friends_names)
# friends_names.append('Artem')
# print(friends_names)

# friends_names.insert(1, 'Artem')
# print(friends_names)
# friends_names[1] = 'Artem'
# print(friends_names)
# 8
# Есть массив чисел numbers = [5, 1, 2, 7, 4, 3, 8, 1, 10]. Нужно поменять местами первый и последний элементы.
# (двумя способами указать последний элемент).
# a = [5, 1, 2, 7, 4, 3, 8, 1, 10]
# b = 0
# a[-1], a[b] = a[b], a[-1]
# print(a)
# numbers = [5, 1, 2, 7, 4, 3, 8, 1, 10]
# print(numbers[0], numbers[-1])
# numbers[0], numbers[-1] = numbers[-1], numbers[0]
# print(numbers)
# tap = numbers[0]
# numbers[0] = numbers[-1]
# numbers[-1] = tap
# print(numbers)
# print(len(numbers) - 1)
# Задание закончились
# num = 1
# num_2 = 2
# print(num)
#
# string = "abc"
# string2 = "de"
# print(string + string2)
#
# list_ = [1, 2, 3]
# list_2 = [4, 5, 6]
# print(list_ + list_2)
#
#
# list_ = [1, 2, 3]
# list_2 = [1, 2, 3] * 2
# list_ *= 2
# print(list_)
# print(list_2)
#
# from copy import deepcopy
#
#
# list_ = [1, 2, [1]]
# list_3 = list_[:]
# list_4 = list(list_)
# list_2 = list_ * 2
# list_2 = list_ + deepcopy(list_)
# # print(list_)
# # print(list_2)
# # list_[2] += [5]
# list_[2].append(5)
# print('initial',list_)
# print('after append', list_2)

# string = "abc"
# friends = {'Liz', 'Ann'}
# string += friends

# list_ = ["1", "2", "a"]
# print("".join(list_))

# list_ = [1.4, 2.6]
# print(sum(list_))
# print(max(list_))
# print(min(list_))
# list_ = ['c', 'b', 'a']
# result = '-'.join(list_)
# hello_str = 'hello'
# result_ = 2 + 3
# list_ = [1, 2, 3]
# print(f'my join string is {result}')
# print(f'my join string is {list_} []I()')
#
# template = 'my join {} string is {} bla bla'
# print(template.format(result, "abc"))
# print(template.format("hello", "abc"))

#######################################
# if, elif, else
# num1 = int(input('num1: '))
# num2 = int(input('num2: '))

# is_bigger = num1 > num2
# print(is_bigger)

# and
# True and True = True
# True and False = False
# False and False = False
# False and True = False
# False and False = False
# False or True = True
# or
# True and False = True
# False or True = True
# True or True = True
# False or False = False
# False or False or True = True

# if (num1 > num2 and num1 < 0) and (num2 > 0):
#     print(f'{num1} bigger {num2}')
# elif num1 < num2:
#     print(f'{num1} smaller {num2}')
# else:
#     print(f'{num1} = {num2}')
# if num1 + num2 == 5:
#     print(f'{num1} + {num2} = 5')

# list_ = []
# result_str = str(list_) if list_ else "empty" # тенарный оператор

# if num:
#     result_str = str(num)
# else:
#     result_str = "empty"

# print(result_str)
# print(type(result_str))

# 2 (на if else)
# Напишите программу, которая запрашивает у пользователя два числа (x и y) и выводит на экран результат их сравнения.
#
# Если x больше y, то программа должна вывести сообщение "x больше y".
# Если x меньше y, то программа должна вывести сообщение "x меньше y".
# Если x равно y, то программа должна вывести сообщение "x равно y".
# Однако, если x и y кратны 2, то программа должна вывести дополнительное сообщение "Оба числа кратны 2".

# Task_Proba

# x = int(input("Выведите число x: "))
# y = int(input("Выведите число y: "))
# if x % 2 == 0 and y % 2 == 0:
#    print("Оба числа кратны 2")

# elif x % 2 != 0 and y % 2 != 0:
#    print('оба числа не картны 2')
# if x > y:
#    print('x больше y')
# elif x < y:
#    print('x меньше y')
# elif x == y:
#    print("x равно 0")


