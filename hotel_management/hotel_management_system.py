from threading import Lock
from reservation import Reservation
from reservation_status import ReservationStatus
from payment import Payment 
from guest import Guest 
from typing import Dict, Optional
from room import Room
from datetime import date
from room_status import RoomStatus
import uuid

class HotelManagementSystem:
    _instace = None 
    
    def __new__(cls):
        if cls._instace is None:
            cls._instace = super().__new__(cls)
            cls._instace.guests: Dict[str, Guest] = {} 
            cls._instace.rooms: Dict[str, Room] = {}
            cls._instace.reservations: Dict[str, Reservation] = {}
            cls._instace.lock = Lock()
        return cls._instace
    
    def addGuest(self, guest:Guest):
        self.guests[guest.id] = guest 
    def getGuest(self, guest_id:str)->Optional[Guest]: 
        return self.guests.get(guest_id)
    
    def addRoom(self, room:Room):
        self.rooms[room.id] = room
    def getRoom(self, room_id:str)->Optional[Room]:
        return self.rooms.get(room_id)
   
         
    def bookRoom(self, guest: Guest, room:Room, check_in_date: date, check_out_date: date)->Optional[Reservation]:
        with self.lock:
            if room.status == RoomStatus.AVAILABLE:
                room.book()
                reservation_id = self.generate_reservation_id()
                reservation = Reservation(reservation_id, guest, room, check_in_date, check_out_date)
                self.reservations[reservation_id] = reservation 
                return reservation
            return None 
    
    def cancelReservation(self, reservation_id:str):
        with self.lock:
            reservation = self.reservations.get(reservation_id)
            if reservation:
                reservation.cancel()
                del self.reservations[reservation_id]
    
    def checkIn(self, reservation_id:str):
        with self.lock:
            reservation = self.reservations.get(reservation_id)
            if reservation and reservation.status == ReservationStatus.CONFIRMED:
                reservation.room.checkIn()
            else:
                raise ValueError("Invalid reservation")
    def checkOut(self, reservation_id:str, payment:Payment):
        with self.lock:
            reservation = self.reservations.get(reservation_id)
            if reservation and  reservation.status == ReservationStatus.CONFIRMED:
                room = reservation.room 
                amount = room.price*(reservation.check_out_date - reservation.check_in_date).days
                if payment.processPayment(amount):
                    room.checkOut()
                    del self.reservations[reservation_id]
                else:
                    raise ValueError("Payment failed") 
            else:
                raise ValueError("Invalid reservation") 
    
    def generate_reservation_id(self)->str:
        return f"RES{uuid.uuid4().hex[:8].upper()}"        
            
        
            