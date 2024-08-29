import threading

class CashDispenser:
    def __init__(self, initial_cash):
        self.cash_available = initial_cash
        self.lock = threading.Lock()
        
    def dispenseCash(self, amount):
        with self.lock:
            if amount>self.cash_available:
                raise ValueError("Insufficient cash in ATM")
            self.cash_available -= amount
            print("Cash Dispense", amount)
                