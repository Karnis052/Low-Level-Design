from typing import Tuple
from user_type import UserType

class User:
    def __init__(self, name:str, contact: str, location: Tuple[float, float], user_type: UserType):
        self.name = name
        self.contact = contact
        self.location = location
        self.user_type = user_type
        
