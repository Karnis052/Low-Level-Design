from product import Product
class Inventory:
    def __init__(self):
        self.products = {}
        
    def addProduct(self, product:Product, quantity:int):
        self.products[product] = quantity
        
    def removeProduct(self, product:Product):
        del self.products[product]
        
    def updateProduct(self, product, quantity):
        self.products[product] = quantity
        
    def getQuantity(self, product):
        return self.products.get(product, 0)
    
    def isAvailable(self, product):
        return product in self.products and self.products[product]>0
    