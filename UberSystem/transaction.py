from passenger import Passenger
from driver import Driver
class Transaction:
    def __init__(self, passenger:Passenger, driver:Driver, amount:float):
        self.passenger = passenger
        self.driver = driver
        self.amount = amount
    def process(self):
        print(f"Processing payment of ${self.amount} from {self.passenger.name} to {self.driver.name}")