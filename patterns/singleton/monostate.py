# Алекс Мартелли: при работе с синглтон нам ведь по сути не нужен один и тот же
# объект, нам нужно одно и тоже состояние. И он предложил паттерн Monostate!

class Singleton:
    instance = None

    def __new__(cls):
        if Singleton.instance is None:
            Singleton.instance = super().__new__(cls) 
            Singleton._do_work(Singleton.instance)    
        return Singleton.instance 

    def _do_work(self):
        print("Do some hard work")
        self.data = 101


class Monostate:
    _shared_state = {} # распределенное состояние

    def __init__(self):
        """хотя сами объекты будут разные, но 
        атрибуты всех созданных объектов будут одними и теми же"""
        self.__dict__ = self._shared_state
        if not self._shared_state:
            print("Do some hard work")
            self.data = 101

if __name__ == "__main__":
    first = Monostate()
    print(first)
    second = Monostate()
    print(second)
    print(first is second) # False (Объекты разные)
    print("-------------")
    print(first.data)
    first.data = 102
    print(second.data)

