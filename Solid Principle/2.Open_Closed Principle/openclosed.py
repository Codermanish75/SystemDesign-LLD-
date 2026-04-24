from abc import ABC,abstractmethod

class  paymentMethod(ABC):
    @abstractmethod
    def pay(self,amount:int):
        pass

class UPIpayment(paymentMethod):
    def pay(self,amount:int):
        print(f"Paying through UPI of Rs.{amount}")

class DebitCardpayment(paymentMethod):
    def pay(self,amount:int):
        print(f"Paying through debitCard of Rs.{amount}")

class CreditCardpayment(paymentMethod):
    def pay(self,amount:int):
        print(f"Paying through creaditCard of Rs.{amount}")

class PaymentProcessor:
    def process_payment(self,paymentMethod:paymentMethod,amount:int):
        paymentMethod.pay(amount)

debit=DebitCardpayment()
creadit=CreditCardpayment()
pymt_process=PaymentProcessor()
pymt_process.process_payment(debit,500)


