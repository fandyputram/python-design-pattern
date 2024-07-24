class PaymentDono:
    def getBalance(self):
        return 125000

class PaymentOpo:
    def getBalance(self):
        return "Rp, 1.250.000"
    
class NewPaymentAdapter:
    def __init__(self, payment):
        self.payment = payment
    
    def getBalance(self):
        rupiah_str = self.payment.getBalance()
        # Remove the "Rp" prefix and any whitespace
        cleaned_str = rupiah_str.replace("Rp", "").replace(" ", "")
        # Remove any commas and dots
        cleaned_str = cleaned_str.replace(".", "").replace(",", "")
        # Convert to integer
        amount = int(cleaned_str)
        return amount

paymentDono = PaymentDono()
paymentOpo = PaymentOpo()


print(paymentDono.getBalance())
print(paymentOpo.getBalance())
#print(paymentDono.getBalance() + paymentOpo.getBalance()) # Error since int + string

adapter = NewPaymentAdapter(paymentOpo)
print(adapter.getBalance())
print(paymentDono.getBalance() + adapter.getBalance())
