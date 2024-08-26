from uber import Uber
from driver import Driver
from passenger import Passenger
from ride import Ride

class UberDemo:
    @staticmethod
    def run():
       
        uber = Uber()
        uber.addDriver(Driver("Jane", "098-765-4321", (10, 10)))
        uber.addDriver(Driver("John", "123-456-7890", (0, 0)))
        
        uber.addPassenger(Passenger("Alice", "111-222-3333", (2, 2)))
        uber.addPassenger(Passenger("Bob", "444-555-6666", (20, 20)))
        
        request1 = uber.requestRide(uber.passengers[0], (5,5))
        request2 = uber.requestRide(uber.passengers[1], (35, 35))
        
     
        ride1 = uber.findDriver(request1)
        ride2 = uber.findDriver(request2)
        
        if ride1:
            uber.endRide(ride1)
        if ride2:
            uber.endRide(ride2)
            
if __name__ == "__main__":
    UberDemo.run()