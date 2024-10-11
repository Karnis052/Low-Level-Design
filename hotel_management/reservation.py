from guest import Guest
from room import Room
from datetime import date
from reservation_status import ReservationStatus
from threading import Lock
class Reservation:
    def __init__(self, id:str, guest:Guest, room:Room, check_in_date:date, check_out_date:date):
        self.id = id 
        self.guest = guest 
        self.room = room 
        self.check_in_date = check_in_date 
        self.check_out_date = check_out_date 
        self.status = ReservationStatus.CONFIRMED
        self.lock = Lock() 
    
    def cancel(self):
        with self.lock:
            if self.status == ReservationStatus.CONFIRMED:
                self.status = ReservationStatus.CANCELED
            else:
                raise ValueError("Reservation is not confirmed")