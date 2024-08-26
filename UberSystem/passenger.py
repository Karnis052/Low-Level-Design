from typing import Tuple
from user_type import UserType
from ride_request import RideRequest
from user import User
class Passenger(User):
    def __init__(self, name: str, contact: str, location: Tuple[float, float]):
        super().__init__(name, contact, location, UserType.PASSENGER)
    
    def requestRide(self, destination: Tuple[float, float]):
        return RideRequest(self, self.location, destination)