from abc import ABC, abstractmethod

# Define an interface or abstract base class
class Toy(ABC):
    @abstractmethod
    def create(self):
        pass

# Implement concrete classes for each type of object
class Car(Toy):
    def create(self):
        return {"type": "car", "wheels": 4, "color": "red"}

class Doll(Toy):
    def create(self):
        return {"type": "doll", "hair_color": "blonde", "height": "12 inches"}

# Create a factory class
class ToyFactory:
    @staticmethod
    def create_toy(toy_type):
        if toy_type == "car":
            return Car().create()
        elif toy_type == "doll":
            return Doll().create()
        else:
            return None

# Usage
toy = ToyFactory.create_toy("car")
print(toy)  # Output: {'type': 'car', 'wheels': 4, 'color': 'red'}
