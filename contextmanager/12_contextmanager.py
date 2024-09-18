# Урок от Python Russian

from contextlib import contextmanager

# По сути менеджер контекста - это возможность спрятать блок try/except/finally
# А внутри мы можем прописывать любую нужную нам логику обработки
# И необязательно открывать файл, обращаться к БД и так далее
# Мы можем делать что-то другое, что нам необходимо... 

class Resource:
    def __init__(self):
        self.opened = False
    
    def open(self, *args):
        print(f"Resource was opened with args: {args}")
        self.opened = True
    
    def close(self):
        print("Resource was closed")
        self.opened = False
    
    def __del__(self):
        if self.opened:
            print(f"Memory leak detected! Resource was not closed") # leak = утечка
    
    def action(self):
        print("Do smth with resource")

# ПЕРВЫЙ СПОСОБ (ФУНКЦИОНАЛЬНЫЙ) 
@contextmanager
def open_resource(*args):
    resource = None
    try:
        resource = Resource()
        resource.open(*args)
        yield resource # yield - это генератор, поэтому он
        # возвращает resource и останавливается в этом месте
        # возвращается он сюда либо если произошел выброс исключения,
        # либо если блок with завершился
    except Exception: # лучше прописывать более конкретное исключение
        # log
        raise # pass вместо raise Позволяет заблокировать уведомления об исключениях
    finally:
        if resource:
            resource.close()


# ВТОРОЙ СПОСОБ (КЛАССОВЫЙ)
class ResourceWorker():
    def __init__(self, *args):
        self.args = args
        self.resource = None
    
    def __enter__(self):
        self.resource = Resource()
        self.resource.open(*self.args)
        return self.resource # а не yeild
    
    def __exit__(self, exc_type, exc_value, exc_tb):
        if self.resource:
            self.resource.close()
        # return True # Позволяет заблокировать уведомления об исключениях


if __name__ == "__main__":

    # ПЕРВЫЙ СПОСОБ (ФУНКЦИОНАЛЬНЫЙ)
    # with open_resource(1, 2, 3) as res:
    #     res.action()
    #     raise ValueError("STOP")

    # ВТОРОЙ СПОСОБ (КЛАССОВЫЙ)
    with ResourceWorker(1, 2, 3) as res:
        res.action()
        raise ValueError("STOP")