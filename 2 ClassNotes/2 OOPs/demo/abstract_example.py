from abc import ABC, abstractmethod
from typing import override


class Payment(ABC):
    def __init__(self, course_name, course_code, fee):
        self.course_name = course_name
        self.course_code = course_code
        self.fee = fee

    def get_fee(self):
        return self.fee

    @abstractmethod
    def pay(self, amount):
        pass

    def __str__(self):
        return f"{self.course_name} ({self.course_code}) | Fee: {self.fee}"

class CreditCard(Payment):

    def __init__(self, course_name, course_code, fee):
        super().__init__(course_name, course_code, fee)
    @override
    def pay(self, amount):
        print("Credit Card")

class DebitCard(Payment):
    @override
    def pay(self, amount):
        print("Debit Card")

class UPI(Payment):
    @override
    def pay(self, amount):
        print("UPI Card")

class NFC(Payment):
    @override
    def pay(self, amount):
        print("NFC Card")

payment = CreditCard("DSA", "D123", 10000)
print(payment)