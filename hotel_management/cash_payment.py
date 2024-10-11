from payment import Payment

class CashPayment(Payment):
    def processPayment(self, amount:float) ->bool:
        #logic for cash  payment
        return True
        