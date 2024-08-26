from typing import List
from parking_spot import ParkingSpot
from vehicle import Vehicle
from vehicle_type import VehicleType

class Level:
    def __init__(self, floor:int, number_spots:int):
        self.floor = floor
        self.parking_spots: List[ParkingSpot] = [ParkingSpot(i, VehicleType.CAR if i%3==0 else VehicleType.MOTORCYCLE if i%3==1 else VehicleType.TRUCK)
                                                 for i in range(number_spots)]
        
    def park_vehicle(self, vehicle:Vehicle)->bool:
        for spot in self.parking_spots:
            if spot.is_available() and spot.get_vehicle_type() == vehicle.get_type():
                spot.park_vehicle(vehicle)
                return True
        return False
    
    def unpark_vehicle(self, vehicle:Vehicle) ->bool:
        for spot in self.parking_spots:
            if not spot.is_available() and spot.get_vehicle() == vehicle:
                spot.unpark_vehicle()
                return True
        return False
    
    def display_availability(self) ->None:
        print(f"Level {self.floor} Availability:")
        for spot in self.parking_spots:
            print(f" Spot {spot.get_spot_number()} is {"Available" if spot.is_available() else "Occupied"}")