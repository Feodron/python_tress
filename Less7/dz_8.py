# import csv
# import json
#
# file = open('hello.txt')
# # тут работаем с файлом
# file.close()
#
# with open('hello.txt') as file:
#     # тут работаем с файлом
#     pass
#
# file.read()
# 1. после with писать самому file.close()
# 2. мы не можем работать с фалом вне блока with

# первое задание
# var1 = '1'
# var2 = '1'
# var3 = '1'
# var4 = '1'
# with open('new_file.txt', 'w') as file:
#     file.write(var1 + '\n')
#     file.write(var2 + '\n')
# with open('new_file.txt', 'a') as file:
#     file.write(var3 + '\n')
#     file.write(var4 + '\n')
# второе задание
#
# my_dict = {
#     123456: ('name', 12),
#     122445: ('name', 12),
#     123564: ('name', 12),
#     111116: ('name', 12),
#     123452: ('name', 12),
#     122456: ('name', 12),
# }
# with open('dict.json') as file:
#     json.dump(my_dict, file)
# 3

import csv
import random

with open('dict.json') as file:
    json_data = json.load(file)

with open('result.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(['id', 'name', 'age', 'phone'])
    for item_key in json_data:
        writer.writerow([item_key, json_data[item_key][0], json_data[item_key][1], random.randint(1, 10)])

