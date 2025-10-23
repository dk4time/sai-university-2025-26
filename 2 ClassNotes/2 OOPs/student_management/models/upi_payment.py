import uuid
from demo.models.payment_gateway import PaymentGateway

class UPIPayment(PaymentGateway):
    def __init__(self):
        self.transaction_id = None

    def process_payment(self, enrollment, amount):
        self.transaction_id = str(uuid.uuid4())[:8]
        enrollment.mark_paid()
        print(f"UPI Transaction Successful | ID: {self.transaction_id} | Amount: ₹{amount}")
