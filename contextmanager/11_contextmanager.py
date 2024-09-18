# Урок от Python Russian

# Контекстный менеджер - это способ высвободить ресурсы автоматически
# (не отвлекаясь на них)
# Чтобы файл был закрыт автоматически, даже если мы забыли его закрыть методом close 

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



if __name__ == "__main__":
    resource = Resource()
    resource.open(1, 2, 3)
    resource.action()
    raise ValueError("STOP") # Непредвиденное исключение не позволяет закрыться ресурсу
    resource.close()