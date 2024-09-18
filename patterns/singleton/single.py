

class Singleton:
    instance = None # ссылка на объект класса

    # используем метод __new__, т.к. в питоне при создании нового объекта
    # сначала вызывается именно __new__, который и создает объект, а после 
    # него вызывается уже __init___, который инициализирует атрибуты
    def __new__(cls):
        if Singleton.instance is None:
            Singleton.instance = super().__new__(cls) # Обращаемся к суперклассу object
                                                      # и через его метод __new__
                                                      # создаем объект класса Singleton
            Singleton._do_work(Singleton.instance)    # ВЫЗОВ ЗАЩИЩЕННОЙ ФУНКЦИИ
        return Singleton.instance # Если объект уже существует нам сразу вернут ссылку


    def _do_work(self):
        """Обращение к базам данных, парсинг сайтов,
        создание пула подключения к веб-драйверам"""
        print("Do some hard work")
        # parse, db, work with data/resources etc...
        self.data = 101
        

if __name__ == "__main__":
    first = Singleton()
    print(first)
    second = Singleton()
    print(second)
    print(first is second) # True (Объекты одинаковые)
    print("-------------")
    print(first.data)
    first.data = 102
    print(second.data)

    # При многопоточке важно предусмотреть блокировку, чтобы разные потоки
    # не выполнили один и тот же код, и не создали еще объектов