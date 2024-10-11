from reservation import Reservation
from room import Room
from guest import Guest
from hotel_management_system import HotelManagementSystem

class HotelManagementSystemDemo:
    @staticmethod
    def run():
        hotel_management_system = HotelManagementSystem()
        
        guest1 = Guest("G001", "John Doe", "john@example.com", "1234567890")
        guest2 = Guest("G002", "Jane Smith", "jane@example.com", "9876543210")
        
        
if __name__ == "__main__":
    HotelManagementSystemDemo.run()