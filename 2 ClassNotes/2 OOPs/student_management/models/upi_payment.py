# models/upi_payment.py
from .payment_gateway import PaymentGateway

class UPIPayment(PaymentGateway):
    def process_payment(self, enrollment, amount):
        print(f"🔹 [UPI] Processing ₹{amount} for {enrollment.student.name}...")
        enrollment.mark_paid()
        print("✅ UPI Payment Successful!")
