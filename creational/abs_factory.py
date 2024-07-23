from abc import ABC, abstractmethod

class Chair(ABC):
    @abstractmethod
    def sit_on(self):
        pass
    

class ModernChair(Chair):
    def sit_on(self):
        return "Sitting on a modern chair."
    
class VictorianChair(Chair):
    def get_title(self):
        return "Sitting on a Victorian chair."
    
class FurnitureFactory(ABC):
    @abstractmethod
    def create_chair(self):
        pass
    
    
class ModernFurnitureFactory(FurnitureFactory):
    def create_chair(self):
        return ModernChair()
    
class VictorianFurnitureFactory(FurnitureFactory):
    def create_chair(self):
        return VictorianChair()
    
def order_furniture(factory):
    chair = factory.create_chair()
    return chair.sit_on()

modern_factory = ModernFurnitureFactory()
victorian_factory = VictorianFurnitureFactory()

print(order_furniture(modern_factory))
print(order_furniture(victorian_factory))
