from vehicle import Vehicle
from vehicle_type import VehicleType
 

class ParkingSpot():
    def __init__(self, spot_number:int, vehicle_type:VehicleType):
        self.spot_number = spot_number
        self.vehicle_type = vehicle_type
        self.parked_vehicle = None
        
    def is_available(self) ->bool:
        return self.parked_vehicle is None
    
    def park_vehicle(self, vehicle: Vehicle)->None:
        if self.is_available() and vehicle.get_type() == self.vehicle_type:
            self.parked_vehicle = vehicle
            print(f"{vehicle.license_plate} is parked in spot {self.spot_number}")
        else:
            raise ValueError("Invalid vehicle type or spot already occupied")
        
    def unpark_vehicle(self)->None:
        self.parked_vehicle = None
        
    def get_vehicle(self) ->Vehicle:
        return self.parked_vehicle
    def get_vehicle_type(self) ->VehicleType:
        return self.vehicle_type
    def get_spot_number(self) ->int:
        return self.spot_number


