from tokenize import Double


class Product:
    def __init__(self, name:str, price):
        self.name = name
        self.price = price
    def getProductName(self):
        return self.name
    def getProductPrice(self):
        return self.price