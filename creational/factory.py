from abc import ABC, abstractmethod

class Book(ABC):
    @abstractmethod
    def get_title(self):
        pass
    

# Concrete
class Novel(Book):
    def get_title(self):
        return "Novel"

# Concrete   
class Biography(Book):
    def get_title(self):
        return "Biography"
    
class Bookstore(ABC):
    @abstractmethod
    def create_book(self):
        pass
    
    def order_book(self):
        book = self.create_book()
        return f"Ordered a {book.get_title()}."
    
class NovelStore(Bookstore):
    def create_book(self):
        return Novel()
    
class BiographyStore(Bookstore):
    def create_book(self):
        return Biography()
    
def purchase_book(store):
    return store.order_book()

novel_store = NovelStore()
biography_store = BiographyStore()

print(purchase_book(novel_store))
print(purchase_book(biography_store))
