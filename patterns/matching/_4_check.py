def check(value: tuple):
    match value:
        case (name, _, salary) if name in ('John', 'Ana'):
            return salary
        case ('Helen', age, _):
            return age
        # str(something) означает, что последний элемент из 5 - это строка
        # и нужно значение этой строки присвоить переменной something
        case (_, _, _, _, str(something)):
            return f'Strange: {something}'
        case (*_, something) if len(value) == 6:
            return f'{something}'
        case tuple():
            return f'Unknown content: {value}'
        case _:
            print(f'ValueError: Expected a tuple!')


if __name__ == '__main__':
    first = ('Ana', 22, 100_000)
    second = ('Helen', 21, 100_000)
    third = (1, 2, 3, 4, 'Something new')
    fourth = (1, 2, 3, 4, 5, 'My message')
    fifth = (1, 2, 3, 4, 5, 6, 7, 8, 9, 'Chars')

    print(f'{check(first) = }')
    print(f'{check(second) = }')
    print(f'{check(third) = }')
    print(f'{check(fourth) = }')
    print(f'{check(fifth) = }')
    print(f'{check("qqq") = }')
