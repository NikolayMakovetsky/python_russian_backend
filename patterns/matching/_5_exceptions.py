from collections import namedtuple

PI = 3.14

Const = namedtuple('Const', ['value'])
pi = Const(value=3.14)


def some1(x):
    """Хотим сверить константу с передаваемым значением"""
    match x:
        # case PI:  # питон пытается здесь создать новую переменную PI -> ОШИБКА
        #     print(f'{x}')
        case _:
            print(f'ValueError 1')


def some2(x):
    match x:
        case pi.value:  # если тут есть точка, то паттерн работает как нам и нужно
            print(f'pi.value=({pi.value}) равна по значению x=({x})')
        case _:
            print(f'ValueError 2')


def some3(x):
    match x:
        case z if z == PI:  # такая запись позволяет работать с контантой безо всяких точек (взлом системы)
            print(f'Константа PI=({PI}) равна по значению x=({x})')
        case _:
            print(f'ValueError 3')


if __name__ == '__main__':
    some1(3.14)
    some2(3.14)
    some3(3.14)
