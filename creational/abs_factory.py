from abc import ABC, abstractmethod

# Define abstract base classes for the product families
class Chair(ABC):
    @abstractmethod
    def create(self):
        pass

class Table(ABC):
    @abstractmethod
    def create(self):
        pass

# Implement concrete classes for each type of product
class ModernChair(Chair):
    def create(self):
        return {"type": "chair", "style": "modern", "material": "plastic"}

class ModernTable(Table):
    def create(self):
        return {"type": "table", "style": "modern", "material": "glass"}

class VictorianChair(Chair):
    def create(self):
        return {"type": "chair", "style": "victorian", "material": "wood"}

class VictorianTable(Table):
    def create(self):
        return {"type": "table", "style": "victorian", "material": "wood"}

# Define an abstract factory interface
class FurnitureFactory(ABC):
    @abstractmethod
    def create_chair(self):
        pass

    @abstractmethod
    def create_table(self):
        pass

# Implement concrete factory classes for each family of products
class ModernFurnitureFactory(FurnitureFactory):
    def create_chair(self):
        return ModernChair().create()

    def create_table(self):
        return ModernTable().create()

class VictorianFurnitureFactory(FurnitureFactory):
    def create_chair(self):
        return VictorianChair().create()

    def create_table(self):
        return VictorianTable().create()

# Usage
def create_furniture_set(factory):
    chair = factory.create_chair()
    table = factory.create_table()
    return {"chair": chair, "table": table}

modern_factory = ModernFurnitureFactory()
victorian_factory = VictorianFurnitureFactory()

modern_furniture = create_furniture_set(modern_factory)
victorian_furniture = create_furniture_set(victorian_factory)

print(modern_furniture)
# Output: {'chair': {'type': 'chair', 'style': 'modern', 'material': 'plastic'}, 'table': {'type': 'table', 'style': 'modern', 'material': 'glass'}}

print(victorian_furniture)
# Output: {'chair': {'type': 'chair', 'style': 'victorian', 'material': 'wood'}, 'table': {'type': 'table', 'style': 'victorian', 'material': 'wood'}}
