from vending_machine_state import VendingMachineState
from product import Product
from coin import Coin
from note import Note
from inventory import Inventory

class IdleState(VendingMachineState):
    def __init__(self, vending_machine):
        self.vending_machine = vending_machine
        
    def selectProduct(self, product):
        if  self.vending_machine.inventory.isAvailable(product):
            self.vending_machine.selected_product = product
            self.vending_machine.setState(self.vending_machine.ready_state)
            print(f"Product selected: {self.vending_machine.selected_product.getProductName()}")
        else:
            product(f"Product is not available: {product.getProductName()}")
              
    def insertCoin(self, coin):
        print("Please select a product first.")
    def insertNote(self, note):
        print("Please select a product first.")
        
    def dispenseProduct(self):
         print("Please select a product and make payment.")
    def returnChange(self):
        print("No change to return.")