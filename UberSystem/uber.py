from ride_request import RideRequest
from ride import Ride
from transaction import Transaction
from driver import Driver
from passenger import Passenger

class Uber:
    def __init__(self):
        self.drivers = []
        self.passengers = []
        self.ride_requests = []
        self.active_rides = []
        
    def addDriver(self, driver:Driver):
        self.drivers.append(driver)
        
    def addPassenger(self, passenger:Passenger):
        self.passengers.append(passenger)
        
    def requestRide(self, passenger, destination):
        request = passenger.requestRide(destination)
        self.ride_requests.append(request)
        print(f"Ride requested by {passenger.name} to {destination}. Price: ${request.price}")
        return request
    
    def findDriver(self, request:RideRequest):
        available_drivers = [driver for driver in self.drivers if driver.available]
        
        for driver in available_drivers:
            if request in driver.searchRequest(self.ride_requests):
                driver.acceptRequest(request)
                self.ride_requests.remove(request)
                ride = Ride(request)
                self.active_rides.append(ride)
                print(f"Driver {driver.name} accepted the ride for {request.passenger.name}")
                return ride
                
        print("No driver available")
        return None
    
    
    def endRide(self, ride):
        transaction = ride.endRide()
        self.active_rides.remove(ride)
        ride.request.driver.available = True
        ride.request.driver.ride_count +=1
        transaction.process()
        
        print(f"Ride completed. {ride.request.passenger.name} reached their destination.")
        
        