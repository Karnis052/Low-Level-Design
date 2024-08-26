from parking_lot import ParkingLot
from vehicle import Vehicle
from vehicle_type import VehicleType
from level import Level
from car import Car
from motocycle import Motorcycle
from truck import Truck

class ParkingLotDemo:
    def run():
        parking_lot = ParkingLot.get_instance()
        parking_lot.add_level(Level(1, 2))
        parking_lot.add_level(Level(2, 3))
        
        car = Car("Car123")
        motorcycle = Motorcycle("motorcycle123")
        truck = Truck("Truck1234")
        
        #Park Vehicle
        parking_lot.park_vehicle(car)
        parking_lot.park_vehicle(motorcycle)
        parking_lot.park_vehicle(truck)
        
        # Display availability
        parking_lot.display_availability()
        
        
        # Unpark vehicle
        parking_lot.unpark_vehicle(car)
        
        # Display availability
        parking_lot.display_availability()

if __name__ == "__main__":
    ParkingLotDemo.run()
    
    