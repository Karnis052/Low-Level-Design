from typing import Tuple

class RideRequest:
    def __init__(self, passenger, pickup: Tuple[float, float], destination: Tuple[float, float]):
        self.passenger = passenger
        self.pickup = pickup
        self.destination = destination
        self.driver = None
        self.price = self.calculatePrice()
    def calculatePrice(self):
        distance = ((self.pickup[0] - self.destination[0])**2  + (self.pickup[1] - self.destination[1])**2)**0.5
        return round(5 + (distance*2), 2)
    def assignDriver(self, driver):
        self.driver = driver
        