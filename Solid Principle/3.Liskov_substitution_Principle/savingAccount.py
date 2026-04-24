from withdrableAccount import withdrableAccount

class SavingAccount(withdrableAccount):
    def __init__(self, balance):
        super().__init__(balance)
    
    def deposit(self,amount):
        self.balance+=amount
        print(f"amount deposited,current balance={self.balance}")
    
    def withdraw(self, amount):
        if self.balance<amount:
            print("Can not withdraw,not a sufficient balance ")
        else:
            self.balance-=amount
            print(f"amount withdran, current balance ={self.balance}")