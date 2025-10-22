# models/card_payment.py
from .payment_gateway import PaymentGateway

class CardPayment(PaymentGateway):
    def process_payment(self, enrollment, amount):
        print(f"💳 [Card] Charging ₹{amount} for {enrollment.student.name}...")
        enrollment.mark_paid()
        print("✅ Card Payment Successful!")
