from hotel import Hotel
from hotel_booking import HotelBooking

class HotelBookingDemo:
    @staticmethod
    def run():
        system =  HotelBooking()
        system.addHotel("ABC", (2,3), "A Safe hotel", 20, 10, 5)
        system.addHotel("BCD", (5,5), "A Safe hotel", 50, 50, 40)
     

    
    
if __name__ == "__main__":
    HotelBookingDemo.run()
    