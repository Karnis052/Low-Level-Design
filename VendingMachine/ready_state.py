from vending_machine_state import VendingMachineState
from product import Product
from inventory import Inventory
from coin import Coin
from note import Note

class ReadyState(VendingMachineState):
    def __init__(self, vending_machine):
       self.vending_machine = vending_machine
       
    def selectProduct(self, product):
        print("Product already selected. Please make payment.")
        
    def insertCoin(self, coin):
        self.vending_machine.addCoin(coin)
        print(f"Coin inserted: {coin.name}")
        self.checkPaymentStatus()
        
    def insertNote(self, note):
        self.vending_machine.addNote(note)
        print(f"Note inserted: {note.name}")
        self.checkPaymentStatus()
    
    def dispenseProduct(self):
        print("Please make payment first.")
        
    def returnChange(self):
        change = self.vending_machine.total_payment - self.vending_machine.selected_product.getProductPrice()
        if change>0:
            print(f"Change returned: ${change:.2f}")
            self.vending_machine.resetPayment()
        else:
            print("No change to return.")
        self.vending_machine.setState(self.vending_machine.idle_state)
        
    def checkPaymentStatus(self):
        if self.vending_machine.total_payment >= self.vending_machine.selected_product.getProductPrice():
            self.vending_machine.setState(self.vending_machine.dispense_state)
    