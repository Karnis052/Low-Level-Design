from vending_machine_state import VendingMachineState

class DispenseState(VendingMachineState):
    def __init__(self, vending_machine):
        self.vending_machine = vending_machine
        
    def selectProduct(self, product):
       print("Product is already selected. Please collect the dispense product")
       
    def insertCoin(self, coin):
        print("Payment already made. Please collect the dispensed product.")
        
    def insertNote(self, note):
        print("Payment already made. Please collect the dispensed product.")
        
    def dispenseProduct(self):   
        product = self.vending_machine.selected_product
        self.vending_machine.inventory.updateProduct(product, self.vending_machine.inventory.getQuantity(product)-1)
        self.vending_machine.setState(self.vending_machine.return_change_state)
    def returnChange(self):
        print("Please collect the dispensed product first.")
    