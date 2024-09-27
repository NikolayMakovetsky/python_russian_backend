
# ПРОБЛЕМА 1)
# Необходимо донести пользователю какие именно варианты строк
# можно передавать в функцию для ее корректной работы
# Важно то, что мы не хотим бросать исключения внутри функции или делать доп проверки,
# но мы хотим сразу подсказать пользователю как корректно ее использовать


def allowed_action(traffic_light: str) -> str:
    #  Вар.1) Можно аннотировать ф-ю но далеко не факт что пользователь прочтет это описание
    """
    Функция описывает ответное действие на входящий сигнал светофора
    На вход ожидается один из вариантов: "red", "green", "yellow"
    """
    if traffic_light == 'red':
        return 'stop'
    elif traffic_light == 'green':
        return 'go'
    elif traffic_light == 'yellow':
        return 'wait'


if __name__ == '__main__':
    print(allowed_action('red'))
    print(allowed_action('green'))
    print(allowed_action('yellow'))
    print(allowed_action('RED'))  # пример некорректного ввода пользователем
