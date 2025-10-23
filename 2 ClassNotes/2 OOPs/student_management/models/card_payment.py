import uuid
from demo.models.payment_gateway import PaymentGateway

class CardPayment(PaymentGateway):
    def __init__(self, card_last4):
        self.card_last4 = card_last4
        self.transaction_id = None

    def process_payment(self, enrollment, amount):
        self.transaction_id = str(uuid.uuid4())[:8]
        enrollment.mark_paid()
        print(f"Card Payment Successful | ID: {self.transaction_id} | Card ****{self.card_last4} | Amount: ₹{amount}")
