from vehicle import Vehicle
from level import Level
from typing import List


class ParkingLot:
    _instance = None
    
    def __init__(self):
        if ParkingLot._instance is not None:
            raise Exception("This is a singleton")
        else:
            ParkingLot._instance = self
            self.levels: List[Level] = []
    
    @staticmethod
    def get_instance():
        if ParkingLot._instance is None:
            ParkingLot()
        return ParkingLot._instance
    def add_level(self, level:Level):
        self.levels.append(level)
    
    def park_vehicle(self, vehicle:Vehicle)->bool:
        for level in self.levels:
            if level.park_vehicle(vehicle):
                return True
        return False
    def unpark_vehicle(self, vehicle:Vehicle)->bool:
        for level in self.levels:
            if level.unpark_vehicle(vehicle):
                return True
        return False
    def display_availability(self)->None:
        for level in self.levels:
            level.display_availability()
            
    
