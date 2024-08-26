class User:
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email
    
    def getId(self):
        return self.user_id
    def getName(self):
        return self.name
    def getEmail(self):
        return self.email
    
        