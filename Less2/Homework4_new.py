print("Выберете и напишите страну, что бы узнать ее столицу:")
print("Belarus,Poland,GreatBritain: ")
dictionary = {'Belarus': 'Minsk', 'Poland': 'Warsaw', 'GreatBritain': 'London'}
a = input()
if a == "Belarus":
    print(dictionary['Belarus'])
elif a == "Poland":
    print(dictionary['Poland'])
elif a == "GreatBritain":
    print(dictionary['GreatBritain'])
else:
    print('Этой странны нету в библиотеке')
