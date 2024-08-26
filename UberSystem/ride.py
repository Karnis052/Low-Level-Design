from ride_request import RideRequest
from transaction import Transaction

class Ride:
    def __init__(self, request:RideRequest):
        self.request = request
        self.status = "In Progress"
    def endRide(self):
        self.status = "Completed"
        return Transaction(self.request.passenger, self.request.driver, self.request.price)
        