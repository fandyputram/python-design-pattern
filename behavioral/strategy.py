from abc import ABC, abstractmethod

# Define the interface for the strategy
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

# Implement concrete strategies
class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid {amount} via credit card")

class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid {amount} via PayPal")

class BankTransferPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid {amount} via bank transfer")

# Context that uses the strategy
class PaymentContext:
    def __init__(self, strategy):
        self._strategy = strategy

    def set_strategy(self, strategy):
        self._strategy = strategy

    def make_payment(self, amount):
        self._strategy.pay(amount)

# Example usage
credit_card_strategy = CreditCardPayment()
paypal_strategy = PayPalPayment()
bank_transfer_strategy = BankTransferPayment()

payment_context = PaymentContext(credit_card_strategy)
payment_context.make_payment(100)

payment_context.set_strategy(paypal_strategy)
payment_context.make_payment(50)

payment_context.set_strategy(bank_transfer_strategy)
payment_context.make_payment(75)

payment_context.make_payment(75)

payment_context.make_payment(75)

payment_context.make_payment(75)

payment_context.make_payment(75)

payment_context.make_payment(75)

payment_context.make_payment(75)