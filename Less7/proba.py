def func_decarator(func):
    def wrapper():
        print('что-то делаем перед функции')
        funс()
        print('что-то делаем после функции')

    return wrapper()


def some_func():
    print('Вызываем функции add')


f = func_decarator(some_func)
f()