class ExistingCashierSystem:
    def process_order(self):
        return "Processing Order in existing cashier system."
    
class NewPaymentAdapter:
    def __init__(self, existing_cashier_system):
        self.existing_cashier_system = existing_cashier_system
    
    def process_order_with_new_payment(self):
        return f"{self.existing_cashier_system.process_order()} and using new payment method."
    
existing_cashier = ExistingCashierSystem()
adapter = NewPaymentAdapter(existing_cashier)

print(adapter.process_order_with_new_payment)