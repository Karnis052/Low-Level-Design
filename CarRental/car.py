class Car:
    def __init__(self, make, model, year, license, rentalPricePerDay):
        self.make = make
        self.model = model
        self.year = year
        self.license = license
        self.rentalPricePerDay = rentalPricePerDay
        self.available = True

    
    def getMake(self):
        return self.make
    def getModel(self):
        return self.model

    def getLicense(self):
        return self.license
    def getRentalPricePerDay(self):
        return self.rentalPricePerDay
    def isAvailable(self):
        return self.available
    def setAvailable(self, available):
        self.available = available
  