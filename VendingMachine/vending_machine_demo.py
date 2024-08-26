from vending_machine import VendingMachine
from product import Product
from inventory import Inventory
from coin import Coin
from note import Note

class VendingMachineDemo:
    @staticmethod
    def run():
        vending_machine = VendingMachine.getInstance()
        
        cookie = Product("Cookie", 1.5)
        water = Product("Water", 1.25)
        pepsi = Product("Pepsi", 1.5)
        vending_machine.inventory.addProduct(cookie, 10)
        vending_machine.inventory.addProduct(water, 5)
        vending_machine.inventory.addProduct(pepsi, 5)

        vending_machine.selectProduct(cookie)
        
        vending_machine.insertCoin(Coin.QUARTER)
        vending_machine.insertCoin(Coin.QUARTER)
        vending_machine.insertCoin(Coin.QUARTER)
        vending_machine.insertCoin(Coin.QUARTER)
        
        vending_machine.insertNote(Note.FIVE)
        
        vending_machine.dispenseProduct()
        
        vending_machine.returnChange()
        
        #Select Pepsi
        vending_machine.selectProduct(pepsi)
        vending_machine.insertCoin(Coin.QUARTER)
        vending_machine.dispenseProduct()
        
        vending_machine.insertCoin(Coin.QUARTER)
        vending_machine.insertCoin(Coin.QUARTER)
        vending_machine.insertCoin(Coin.QUARTER)
        vending_machine.insertCoin(Coin.QUARTER)
        
        vending_machine.dispenseProduct()
        
        vending_machine.returnChange()
        
if __name__ == "__main__":
    VendingMachineDemo.run()