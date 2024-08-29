class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
        
    def getAccountNumber(self):
        return self.account_number
    def getBalance(self):
        return self.balance
    def debit(self, amount):
        self.balance -= amount
    def credit(self, amount):
        self.balance += amount
        