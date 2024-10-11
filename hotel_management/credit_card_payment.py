from payment import Payment 

class CreditCardPayment(Payment):
    def processPayment(self, amount:float) ->bool:
        #process credit card payment 
        return True