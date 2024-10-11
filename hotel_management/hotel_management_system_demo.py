from reservation import Reservation
from room import Room
from guest import Guest
from hotel_management_system import HotelManagementSystem
from room_type import RoomType
from datetime import date 
from credit_card_payment import CreditCardPayment
class HotelManagementSystemDemo:
    @staticmethod
    def run():
        hotel_management_system = HotelManagementSystem()
        
        guest1 = Guest("G001", "John Doe", "john@example.com", "1234567890")
        guest2 = Guest("G002", "Jane Smith", "jane@example.com", "9876543210")
        hotel_management_system.addGuest(guest1)
        hotel_management_system.addGuest(guest2)
        
        
        room1 = Room("R001", RoomType.SINGLE, 100.0)
        room2 = Room("R002", RoomType.DOUBLE, 200.0)
        hotel_management_system.addRoom(room1)
        hotel_management_system.addRoom(room2)
        
        check_in_date = date.today()
        check_out_date = check_in_date.replace(day=check_in_date.day + 3)
        reservation1 = hotel_management_system.bookRoom(guest1, room1,check_in_date, check_out_date)
        if reservation1:
            print(f"Reservation created: {reservation1.id}")
        else:
            print("Room not available for booking.")
        
        hotel_management_system.checkIn(reservation1.id)
        print(f"Checked in: {reservation1.id}")
        
        credit_card_payment = CreditCardPayment()
        hotel_management_system.checkOut(reservation1.id, credit_card_payment)
        print(f"Checked out: {reservation1.id}")
        
        hotel_management_system.cancelReservation(reservation1.id)
        print(f"Reservation cancelled: {reservation1.id}")

        
if __name__ == "__main__":
    HotelManagementSystemDemo.run()