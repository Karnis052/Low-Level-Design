from typing import Dict, Tuple
from hotel import Hotel
class HotelBooking:
    def __init__(self):
        self.hotels: Dict[str, Hotel] = {}
       
    def addHotel(self, name, location, description,accomodation_price, food_price, service_charge):
        hotel = Hotel(name, location, description, accomodation_price, food_price, service_charge)
        self.hotels[name] = hotel
        
    def allHotels(self):
        for hotel in self.hotels.values():
            print(f"Hotel Name {hotel.name}")
            print(f"Hotel location {hotel.location}")
            # all other information about hotel
    def searchHotel(self, name, description):
        for hotel in self.hotels.values():
            if hotel.name == name:
                return hotel
        
        # search by description
        for hotel in self.hotels.values():
            if hotel.description.lower() == description.lower():
                return hotel
        print("No hotel found for the search")
    def addReview(self,name,rating, review):
        hotel = self.hotels[name]
        hotel.addReview(rating, review)
    
    def showReview(self, name):
        hotel = self.hotels[name]
        hotel.showReview()
    
    def fitelHotelByLocation(self, location):
        filtered_hotel = []
        for hotel in self.hotels.values():
            if hotel.location == location:
                filtered_hotel.append(hotel)
        
        return filtered_hotel
    
    def filterHotelByPrice(self, lower, upper):
        filtered_hotel = []
        for hotel in self.hotels.values():
            if hotel.totalPrice>= lower and hotel.totalPrice <= upper:
                filtered_hotel.append(hotel)
    
    def filterHotelByRating(self, rating):
        filtered_hotel = []
        for hotel in self.hotels.values():
            if hotel.rating == rating:
                filtered_hotel.append(hotel)
        
        return filtered_hotel
            
    # location have to be in value for finding by distance
    def findHotelByDistance(self, location, distance):
        
        locations = [] #location
        lower_location = location
        lb = 0
        rb = len(locations)
        while lb<rb:
            mid = (lb+rb)/2
            if locations[mid] >= location:
                rb = mid
            else:
                lb = mid+1 
            
        
        
        filtered_hotel = []
        for hotel in self.hotels.values():
            if hotel.getDistance(location) <= distance:
                filtered_hotel.append(hotel)
        return filtered_hotel
        
    
        