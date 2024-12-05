def parse_response(value):
    match value:
        # ТИП ОБЪЕКТА: МАППИНГ (СЛОВАРЬ)
        # ОБЯЗАТЕЛЬНО ДОЛЖНЫ БЫТЬ:
        # ключ 'key': 1000
        # могут прийти и другие пары ключ:значение, их запиши в словарь rest
        case {'key': 1000, **rest}:
            return rest['id']

        # ТИП ОБЪЕКТА: ПОСЛЕДОВАТЕЛЬНОСТЬ (ТАПЛ, ЛИСТ)
        # ОБЯЗАТЕЛЬНО ДОЛЖНЫ БЫТЬ:
        # переменная 'error'
        # некая переменная, значение которой необходимо присвоить переменной message
        # могут быть и ещё переменные, которые необходимо записать в список _ (их мы не будем использовать)
        case ('error', message) | ('error', message, *_):  # ждем два шаблона (отработает какой-то один)
            print(message)

        # ТИП ОБЪЕКТА: МАППИНГ (СЛОВАРЬ)
        # ОБЯЗАТЕЛЬНО ДОЛЖНЫ БЫТЬ:
        # ключ 'meta'
        # значение этого ключа необходимо присвоить переменной val
        # остальные пары ключ:значение необходимо записать в словарь rest
        # ГАРД if not rest СТАВИТ УСЛОВИЕ, что rest должен быть пустой
        case {'meta': val, **rest} if not rest:
            return val['id']

        # ТИП ОБЪЕКТА: МАППИНГ (СЛОВАРЬ) С ВЛОЖЕННОЙ ПОСЛЕДОВАТЕЛЬНОСТЬЮ (ТАПЛ, СПИСОК)
        # ВАЖНО ВСЕГДА ПОМНИТЬ, ЧТО МАППИНГ СРАВНИВАЕТСЯ МАТЧЕМ НЕСТРОГО, А ПОСЛЕДОВ-ТЬ - СТРОГО!!!
        # ОБЯЗАТЕЛЬНО ДОЛЖНЫ БЫТЬ: (смотри структуру)
        # текст ошибки мы присваиваем переменной error
        # значение allowed мы присваиваем переменной allowed
        case {'meta': {'code': _, 'error': error}, 'info': [{'allowed': allowed}, _]}:
            return f'{error}, {allowed}'

        # ТИП ОБЪЕКТА: ПОСЛЕДОВАТЕЛЬНОСТЬ (ТАПЛ, ЛИСТ)
        # ОБЯЗАТЕЛЬНО ДОЛЖНЫ БЫТЬ:
        # переменная х, которая должна соответствовать типу set (множество)
        # второй элемент нам не интересен - запиши его в переменную _
        # ГАРД if len(x) == 2 СТАВИТ УСЛОВИЕ, что во множестве х должно быть 2 элемента
        # возвращаться будет максимальное значение из множества, в котором 2 элемента
        case (set() as x, _) if len(x) == 2:  # set() as x -> set(x) ...можно и так, и так написать
            return max(x)

        # ВО ВСЕХ ПРОЧИХ СЛУЧАЯХ:
        case _:
            print(f'Unknown value: {value}')


if __name__ == '__main__':
    first = {'key': 1000, 'id': 999, 'somekey': 12345}
    second = ['error', 'Slow network connection!', 123, 456]
    third = {'meta': {'id': 999}}
    forth = {'meta': {'code': 200, 'error': 'ParserError'}, 'info': [{'allowed': 'yes'}, 111]}
    fifth = ({10, 11}, 5)

    print(f"{parse_response(first)= }")
    print(f"{parse_response(second)= }")
    print(f"{parse_response(third)= }")
    print(f"{parse_response(forth)= }")
    print(f"{parse_response(fifth)= }")
    print(f"{parse_response(55)= }")