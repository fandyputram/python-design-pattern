class Singleton:
    _instance = None
    
    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance
    


obj1 = Singleton()
obj2 = Singleton()

print(obj1 is obj2)


class NotSingleton:
    
    def __new__(cls):
        return super(NotSingleton, cls).__new__(cls)
    
obj3 = NotSingleton()
obj4 = NotSingleton()

print(obj3 is obj4)