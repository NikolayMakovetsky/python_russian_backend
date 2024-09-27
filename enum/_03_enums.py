from enum import Enum, auto

#  ENUM - КЛАСС ДЛЯ РАБОТЫ С НЕСКОЛЬКИМИ КОНСТАНТАМИ, СВЯЗАННЫМИ ПО СМЫСЛУ

class TrafficLight(Enum):  # класс Enum уже содержит нужные нам методы
    # Здесь обязательно прописываются константы, перегружать или писать свои методы необязательно
    RED = auto()
    GREEN = auto()
    YELLOW = auto()  # "заглушка" auto означает что значение константы м.б. любым


def allowed_action(traffic_light: TrafficLight) -> str:

    if traffic_light == TrafficLight.RED:
        return 'stop'
    elif traffic_light == TrafficLight.GREEN:
        return 'go'
    elif traffic_light == TrafficLight.YELLOW:
        return 'wait'


if __name__ == '__main__':
    # Ctrl+P дает увидеть программисту какие аргументы передаются в функцию
    # allowed_action(TrafficLight.)  # IDE, благодаря Enum, высветит подсказку программисту

    print(allowed_action(TrafficLight.RED))
    print(allowed_action(TrafficLight.GREEN))
    print(allowed_action(TrafficLight.YELLOW))
