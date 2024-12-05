"""
Задача: написать ф-ю, которой на вход приходит полное имя студента.
Прийти оно может в формате строки, кортежа, списка или словаря

Ф-я должна вернуть 'Error' если данные неверные или их недостаточно (или наоборот слишком много)
Если все хорошо, то она должна вернуть нам строку в стиле:
'Фамилия: ___, Имя: ___, Отчество: ___'
"""


def parse_names(value: str | tuple | list | dict) -> str:
    match value:
        # если value - некая последовательность из 3-х элементов (tuple, list + все наследники sequence)
        # то мы можем сразу её распарсить:
        # surname, name, second_name == (surname, name, second_name) == [surname, name, second_name]
        # Здесь [] - не список, а () - не тапл. Это просто варианты синтаксиса распаковки в матчинге
        # ТАКЖЕ ВАЖНО: В ПОСЛЕДОВАТЕЛЬНОСТЯХ ПРИ ПРОВЕРКЕ СТРУКТУРЫ БЕРУТСЯ СТРОГО ВСЕ ЭЛЕМЕНТЫ
        case surname, name, second_name:  # ПРОВЕРКА ТИПА И СТРУКТУРЫ
            return f"Фамилия: {surname}, Имя: {name}, Отчество: {second_name}"

        # если пришел некий mapping (а самый известный mapping - это словарь):
        # ТАКЖЕ ВАЖНО: В МАППИНГЕ ПРИ ПРОВЕРКЕ СТРУКТУРЫ СРАВНИВАЮТСЯ ТОЛЬКО ТЕ КЛЮЧИ, КОТОРЫЕ ВЫ УКАЗАЛИ
        case {'surname': surname, 'name': name, 'second_name': second_name} if len(
            value) == 3:  # ПРОВЕРКА ТИПА И СТРУКТУРЫ
            return f"Фамилия: {surname}, Имя: {name}, Отчество: {second_name}"

        # если пришла некая строка:
        # если str() == True, то тогда уже проверяется то, что написано после ГАРДА if
        case str() if len(value.split()) == 3:  # ПРОВЕРКА ТИПА И СТРУКТУРЫ ... if - это 'гард' (ограничитель)
            # isinstance/type нам использовать не нужно...сразу пишем str() и питон все поймёт...
            surname, name, second_name = value.split()
            return f"Фамилия: {surname}, Имя: {name}, Отчество: {second_name}"

        # во всех прочих случаях:
        case _:
            return "Error"


def parse_names_2(value: str | tuple | list | dict) -> str:
    match value:
        # В БЛОКАХ CASE ПРОИСХОДИТ ПРИСВАИВАНИЕ ПЕРЕМЕННЫХ !!!
        case surname, name, second_name:
            pass
        case {'surname': surname, 'name': name, 'second_name': second_name} if len(value) == 3:
            pass
        case str() if len(value.split()) == 3:
            surname, name, second_name = value.split()
            pass
        case _:
            return "Error"
    # ПЕРЕМЕННЫЕ surname, name, second_name ДОСТУПНЫ И ВНЕ БЛОКА match !!!
    return f"Фамилия: {surname}, Имя: {name}, Отчество: {second_name}"


if __name__ == '__main__':
    assert parse_names(('Иванов', 'Пётр')) == "Error"
    assert parse_names(('Иванов', 'Пётр', 'Семёнович')) == "Фамилия: Иванов, Имя: Пётр, Отчество: Семёнович"
    assert parse_names(['Иванов', 'Пётр', 'Семёнович']) == "Фамилия: Иванов, Имя: Пётр, Отчество: Семёнович"
    assert parse_names({'surname': 'Иванов',
                        'name': 'Пётр',
                        'second_name': 'Семёнович'}) == "Фамилия: Иванов, Имя: Пётр, Отчество: Семёнович"

    assert parse_names("Иванов Пётр Семёнович") == "Фамилия: Иванов, Имя: Пётр, Отчество: Семёнович"
    assert parse_names("Иванов Пётр Семёнович 122") == "Error"
    assert parse_names(['Иванов', 'Пётр']) == "Error"
    assert parse_names(['Иванов', 'Пётр', 'Пётр', 'Пётр']) == "Error"
    assert parse_names({'a': 'Иванов', 'b': 'Пётр', 'c': 'Семёнович'}) == "Error"
    assert parse_names({'surname': 'Иванов',
                        'name': 'Пётр',
                        'second_name': 'Семёнович',
                        'salary': 100_000}) == "Error"

    assert parse_names_2(('Иванов', 'Пётр')) == "Error"
    assert parse_names_2(('Иванов', 'Пётр', 'Семёнович')) == "Фамилия: Иванов, Имя: Пётр, Отчество: Семёнович"
    assert parse_names_2(['Иванов', 'Пётр', 'Семёнович']) == "Фамилия: Иванов, Имя: Пётр, Отчество: Семёнович"
    assert parse_names_2({'surname': 'Иванов',
                          'name': 'Пётр',
                          'second_name': 'Семёнович'}) == "Фамилия: Иванов, Имя: Пётр, Отчество: Семёнович"

    assert parse_names_2("Иванов Пётр Семёнович") == "Фамилия: Иванов, Имя: Пётр, Отчество: Семёнович"
    assert parse_names_2("Иванов Пётр Семёнович 122") == "Error"
    assert parse_names_2(['Иванов', 'Пётр']) == "Error"
    assert parse_names_2(['Иванов', 'Пётр', 'Пётр', 'Пётр']) == "Error"
    assert parse_names_2({'a': 'Иванов', 'b': 'Пётр', 'c': 'Семёнович'}) == "Error"
    assert parse_names_2({'surname': 'Иванов',
                          'name': 'Пётр',
                          'second_name': 'Семёнович',
                          'salary': 100_000}) == "Error"
