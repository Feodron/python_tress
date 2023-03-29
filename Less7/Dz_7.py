from datetime import datetime


def wrapper(func):
    def inner(*args, **kwargs):
        print(f'Функция add вызвана в {datetime.now()}')
        try:
            if args and kwargs:
                print(f'с позиционными параметрами {args} и с именнованными параметрами {kwargs}')
            elif kwargs:
                print(f'с именнованными параметрами {kwargs}')
            elif args:
                print(f'с позиционными параметрами {args}')
            return func(*args, **kwargs)
        except Exception:
            print('Вы не задали парамметры')

    return inner


@wrapper 
def add(a, b):
    pass


add(1, 2)
