import uuid
from creditCardPaymentProcessor import CreditCardPaymentProcessor
from reservation import Reservation

class RentalSystem:
    _instance = None
    
    def __init__(self):
        if RentalSystem._instance is not None:
            raise Exception("This class is a singleton!")
        else:
            RentalSystem._instance = self
            self.cars = {}
            self.reservations = {}
            self.paymentProcessor = CreditCardPaymentProcessor()
    @staticmethod
    def getInstance():
        if RentalSystem._instance is None:
            RentalSystem()
        return RentalSystem._instance
    
    def addCar(self, car):
        self.cars[car.getLicense()] = car
    def removeCar(self, car):
        self.cars.pop(car.getLicense())
    def searchCars(self, make, model, startDate, endDate):
        avilableCars = []
        # print(len(self.cars))
        for car in self.cars.values():
            if car.make.lower()== make.lower() and car.model.lower() == model.lower() and car.isAvailable():
                if self.isCarAvailable(car, startDate, endDate):
                    avilableCars.append(car)
        
        return avilableCars
    def isCarAvailable(self, car, startDate, endDate):
        for reservation in self.reservations.values():
            if reservation.getCar()== car:
                if reservation.getEndDate()< endDate and reservation.getStartDate() > startDate:
                    return False
        return True
    
    def makeReservation(self, customer, car, startDate, endDate):
     
        if self.isCarAvailable(car, startDate, endDate):
            reservationId = self.generateReservationId()
            reservation = Reservation(reservationId,customer, car, startDate, endDate)
            self.reservations[reservationId] = reservation
            car.setAvailable(False)
            return reservation
        return None
    def cancelReservation(self,reservation_id):
        reservation = self.reservations.pop(reservation_id,None)
        if reservation is not None:
            reservation.getCar().setAvailable(True)
    def processPayment(self, reservation):
        return self.paymentProcessor.processPayment(reservation.getTotalPrice())
    
    def generateReservationId(self):
        return "RES" + str(uuid.uuid4()).upper()