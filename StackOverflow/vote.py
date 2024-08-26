class Vote:
    def __init__(self, user, value):
        self.id = id(self)
        self.user = user
        self.value = value