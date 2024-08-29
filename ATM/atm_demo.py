from atm import ATM
from banking_service import BankingService
from cash_dispenser import CashDispenser
from card import Card

class ATMDemo:
    @staticmethod
    def run():
        banking_service = BankingService()
        cash_dispenser = CashDispenser(10000)
        atm = ATM(banking_service, cash_dispenser)
        
        banking_service.createAccount("123", 1000)
        banking_service.createAccount("456", 500)
        
        card = Card("123456", "pin")
        atm.authenticateUser(card)
        
        balance = atm.checkBalance('123')
        print("Account balance:", balance)
        atm.withdrawCash('123', 200)
        atm.depositCash('123', 500)
         
        balance = atm.checkBalance('123')
        print("Account balance:", balance)
         
if __name__ == "__main__":
    ATMDemo.run()