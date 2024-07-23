class SingleItemOrder:
    def calculate_total(self):
        return 5
    
class CompositeOrder:
    def __init__(self):
        self.orders = []
        
    def add_order(self, order):
        self._orders.append(order)
        
    def calculate_total(self):
        total = 0
        for order in self._orders:
            total += order.calculate_total()
        return total
    
item_order1 = SingleItemOrder()
item_order2 = SingleItemOrder()

composite_order = CompositeOrder()
composite_order.add_order(item_order1)
composite_order.add_order(item_order2)

print(composite_order.calculate_total())
