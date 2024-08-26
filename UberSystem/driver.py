from typing import Tuple, List
from user import User
from user_type import UserType
from ride_request import RideRequest

class Driver(User):
    def __init__(self, name: str, contact: str, location: Tuple[float, float]):
        super().__init__(name, contact, location, UserType.DRIVER)
        self.available = True
        self.ride_count = 0
        
    def searchRequest(self, ride_requests:List[RideRequest]) ->List[RideRequest]:
        possible_ride= []
        for ride_request in ride_requests:
            if self.calculateDistance(ride_request.pickup)<=5:
                possible_ride.append(ride_request)
        return possible_ride
    
    
    def calculateDistance(self, pickup:Tuple[float, float]):
        return ((self.location[0] - pickup[0]) ** 2 + (self.location[1] - pickup[1]) ** 2) ** 0.5
    
    def acceptRequest(self, request: RideRequest):
        self.available = False
        request.assignDriver(self)