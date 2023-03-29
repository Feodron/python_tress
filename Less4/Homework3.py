# 3*
# Сделать программу, в которой нужно будет угадывать число
import random
input_int = int(input("Введите любое число от 1 до 2: "))
numbers = [1, 2]
random_numbers = random.randint(1, 2)
if input_int == random_numbers:
    print('Вы угадали число')
else:
    print('Вы не угадали число')
