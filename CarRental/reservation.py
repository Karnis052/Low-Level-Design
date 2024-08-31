from datetime import date, timedelta
class Reservation:
    def __init__(self, reservationId,  customer,car, startDate, endDate):
        self.reservationId = reservationId
        self.customer = customer
        self.car = car
        self.startDate = startDate
        self.endDate = endDate
        self.totalPrice = self.calculatePrice()
    
    def calculatePrice(self):
        daysRented =  (self.endDate - self.startDate).days +1 
        return daysRented*self.car.getRentalPricePerDay()

    def getStartDate(self):
        return self.startDate
    def getEndDate(self):
        return self.endDate
    def getTotalPrice(self):
        return self.totalPrice
    def getReservationId(self):
        return self.reservationId
    def getCar(self):
        return self.car
        
        
        