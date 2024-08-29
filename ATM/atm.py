from withdrawal_transaction import WithdrawalTransaction
from deposit_transaction import DepositTransaction
import threading
from datetime import datetime

class ATM:
    def __init__(self, banking_service, cash_dispenser):
        self.banking_service = banking_service
        self.cash_dispenser = cash_dispenser
        self.transaction_counter = 0
        self.transaction_lock = threading.Lock()
        
    def authenticateUser(self, card):
        pass

    def checkBalance(self, account_number):
        account = self.banking_service.getAccount(account_number)
        return account.getBalance()
        
        
    def withdrawCash(self, account_number, amount):
        account = self.banking_service.getAccount(account_number)
        transaction = WithdrawalTransaction(self.generateTransactionId(), account, amount)
        self.banking_service.processTransaction(transaction)
        self.cash_dispenser.dispenseCash(amount)
        
    def depositCash(self, account_number, amount):
        account = self.banking_service.getAccount(account_number)
        transaction = DepositTransaction(self.generateTransactionId(), account, amount)
        self.banking_service.processTransaction(transaction)
       
        
        
        
    def generateTransactionId(self):
        with self.transaction_lock:
            self.transaction_counter +=1
            timestamp = datetime.now()
            return f"{timestamp}{self.transaction_counter}"
        