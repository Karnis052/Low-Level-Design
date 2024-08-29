class Card:
    def __init__(self, card_number, pin):
        self.card_number = card_number
        self.pin = pin
    def getCardNumber(self):
        return self.card_number
    def getPin(self):
        return self.pin