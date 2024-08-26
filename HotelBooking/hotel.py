from typing import Tuple
import heapq

class Hotel:
    def __init__(self, name, location, description, accomodation_price, food_price, service_charge):
        self.name = name
        self.location = location
        self.description = description
        self.accomodation_price = accomodation_price
        self.food_price = food_price
        self.service_charge = service_charge
        self.reviews = []
        self.totalPrice = self.accomodation_price + self.food_price + self.service_charge
        self.rating = 0
        
    def addReview(self, content, rating):
        heapq.heappush(self.reviews, (-rating, content))
        total_rating =0
        for rating, content in self.reviews:
            total_rating += -1*rating
        self.rating = rating/ len(self.reviews)
        
    def showReview(self):
        return self.reviews
    
    def getDistance(self, location):
        distance = ((self.location[0] - location[0])**2 + (self.location[1] -  location[1])**2)**0.5
        return distance
        
        
        