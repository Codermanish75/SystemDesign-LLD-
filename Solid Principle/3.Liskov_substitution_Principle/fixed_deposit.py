from account import Account

class fixedDeposit(Account):
    def __init__(self, balance):
        super().__init__(balance)
    def deposit(self, amount):
        self.balance+=amount
        print(f"amount deposited,current balance={self.balance}")