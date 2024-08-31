from paymentProcessor import PaymentProcessor
class CreditCardPaymentProcessor(PaymentProcessor):
    def processPayment(self, amount):
        #Logic for payment
        return True