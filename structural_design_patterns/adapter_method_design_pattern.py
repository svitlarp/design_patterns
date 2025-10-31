from abc import ABC, abstractmethod

# Target Interface
class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self):
        pass

# Adaptee1 (external api)
class PayPal_API:
    def make_payment(self, amount):
        print(f'[PayPal] Payment of {amount} processed successfully.')

# Adaptee2 (external api)  
class Stripe_API:
    def send_money(self, amount):
        print(f'[Stripe] Sent {amount} successfully.')        

# Adapter1
class PayPal_Adapter(PaymentProcessor):
    def __init__(self, paypal_api):
        self.paypal = paypal_api

    def process_payment(self, amount):
        self.paypal.make_payment(amount)

# Adapter2
class Stripe_Adapter(PaymentProcessor):
    def __init__(self, stripe_api):
        self.stripe = stripe_api

    def process_payment(self, amount):
        self.stripe.send_money(amount)   
        
# Our bank system BankingApp
class BankingApp():
    def __init__(self, payment_processor: PaymentProcessor):
        self.payment_processor = payment_processor

    def transfer_money(self, amount):
        print(f'[BankingApp] Payment init...')
        self.payment_processor.process_payment(amount)
        print(f'[BankingApp] Payment complete.\n')

# Client Code
paypal_adapter = PayPal_Adapter(PayPal_API())
stripe_adapter = Stripe_Adapter(Stripe_API())

app1 = BankingApp(paypal_adapter)
app1.transfer_money(200)

app2 = BankingApp(stripe_adapter)
app2.transfer_money(400)





# # ____________________________________
# # Example with Printers
# # Target inteface
# class Printer(ABC):
#     @abstractmethod
#     def print(self):
#         pass


# # Adaptee
# class LegacyPrinter():
#     def print_document(self):
#         print('Legacy printer is printing a document')

# # Adapter
# class PrinterAdapter(Printer):
#     def __init__(self):
#         self.legacy_printer = LegacyPrinter()  

#     def print(self):
#         self.legacy_printer.print_document()

# # client code:
# def client_code(printer):
#     printer.print()

# if __name__ == "__main__":
#     adapter = PrinterAdapter()
#     client_code(adapter)



