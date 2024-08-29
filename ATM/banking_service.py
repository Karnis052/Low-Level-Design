from transaction import Transaction
from account import Account

class BankingService:
    def __init__(self):
        self.accounts = {}
    
    def createAccount(self, account_number, initial_balance):
        self.accounts[account_number] = Account(account_number, initial_balance)
    
    def getAccount(self, account_number):
        return self.accounts[account_number]

    def processTransaction(self, transaction):
        transaction.execute()
        