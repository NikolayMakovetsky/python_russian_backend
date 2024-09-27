from enum import Enum

#  Теперь мы хотим упростить код так, чтобы при работе с данным модулем,
#  программисту нужно было вносить ВСЕ ИЗМЕНЕНИЯ ТОЛЬКО В ОДНОМ МЕСТЕ

class TrafficLight(Enum):
    # Связываем цвет светофора с тем действием, которое может осуществляться
    RED = 'stop'
    GREEN = 'go'
    YELLOW = 'wait'  # Все изменения вносятся только здесь


def allowed_action(traffic_light: TrafficLight) -> str:
    # Благодаря Enum реализация максимально упростилась
    return traffic_light.value


if __name__ == '__main__':
    # Любая константа в Enum это имя и значение
    print(TrafficLight.RED)
    print(TrafficLight.RED.name)
    print(TrafficLight.RED.value)
    print()
    print(allowed_action(TrafficLight.RED))
    print(allowed_action(TrafficLight.GREEN))
    print(allowed_action(TrafficLight.YELLOW))

