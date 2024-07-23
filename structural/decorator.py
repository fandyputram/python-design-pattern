class BasicOrder:
    def calculate_total(self):
        return 10
    
class DiscountDecorator:
    def __init__(self, order):
        self._order = order
        
    def calculate_total(self):
        return self._order.calculate_total() * 0.9
    
basic_order = BasicOrder()
order_with_discount = DiscountDecorator(basic_order)

print(order_with_discount.calculate_total())