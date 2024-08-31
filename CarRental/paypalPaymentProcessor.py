from paymentProcessor import PaymentProcessor
class PaypalPaymentProcessor(PaymentProcessor):
    def processPayment(self, amount):
        #Logic for payment
        return True