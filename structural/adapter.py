class ExistingCashierSystem:
    def process_order(self):
        return "Processing Order in existing cashier system."
    
    def calculate(self):
        return 123000
    
class NewPaymentAdapter:
    def __init__(self, existing_cashier_system):
        self.existing_cashier_system = existing_cashier_system
    
    def process_order_with_new_payment(self):
        return f"{self.existing_cashier_system.process_order()} and using new payment method."
    
    def calculate(self):
        n = self.existing_cashier_system.calculate()
    
        # Convert to string with commas as thousand separators
        rupiah_str = "{:,}".format(n)
        
        # Replace commas with dots
        rupiah_str = rupiah_str.replace(",", ".")

        # Add "Rp" at the beginning
        return "Rp " + rupiah_str
    
existing_cashier = ExistingCashierSystem()
adapter = NewPaymentAdapter(existing_cashier)

print(adapter.calculate())
