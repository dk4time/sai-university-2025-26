"""
-------------------------------------------------------------
🎓 PYTHON ANNOTATIONS DEMO — Trainer Version
-------------------------------------------------------------
Covers:
1️⃣ @property and @setter — Encapsulation
2️⃣ @staticmethod — Independent utility methods
3️⃣ @classmethod — Class-level constructors
4️⃣ @abstractmethod — Abstract Base Classes
5️⃣ @dataclass — Auto model generation
-------------------------------------------------------------
Author: Dineshkumar 💻
-------------------------------------------------------------
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass
import math


# ============================================================
# 1️⃣ @property — Encapsulation Example
# ============================================================

class BankAccount:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.__balance = balance  # private attribute

    # Getter method — converts method to property
    @property
    def balance(self):
        return self.__balance

    # Setter method — validates data before setting
    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise ValueError("Balance cannot be negative ❌")
        print(f"✅ Balance updated for {self.owner}")
        self.__balance = amount

    # Deleter method (optional)
    @balance.deleter
    def balance(self):
        print(f"⚠️ Balance for {self.owner} deleted!")
        del self.__balance


print("\n--- 1️⃣ @property Demo ---")
acc = BankAccount("Dinesh", 1000)
print("Current Balance:", acc.balance)
acc.balance = 5000
print("Updated Balance:", acc.balance)
# del acc.balance


# ============================================================
# 2️⃣ @staticmethod — Independent Helper Functions
# ============================================================

class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def circle_area(radius):
        return math.pi * radius ** 2


print("\n--- 2️⃣ @staticmethod Demo ---")
print("Sum:", MathUtils.add(10, 5))
print("Area of circle (r=5):", round(MathUtils.circle_area(5), 2))


# ============================================================
# 3️⃣ @classmethod — Alternative Constructor or Class-Level Method
# ============================================================

class Student:
    def __init__(self, name, dept):
        self.name = name
        self.dept = dept

    @classmethod
    def from_string(cls, info_str):
        """Alternative constructor using class reference."""
        name, dept = info_str.split("-")
        return cls(name, dept)

    @classmethod
    def school_name(cls):
        return "Python Training Institute"

print("\n--- 3️⃣ @classmethod Demo ---")
s1 = Student("Hari", "CSE")
s2 = Student.from_string("Dinesh-IT")
print(s1.name, s1.dept)
print(s2.name, s2.dept)
print("School Name:", Student.school_name())


# ============================================================
# 4️⃣ @abstractmethod — Enforcing Method Implementation
# ============================================================

class PaymentGateway(ABC):
    @abstractmethod
    def process_payment(self, amount):
        """All subclasses must implement this method."""
        pass

class UPIPayment(PaymentGateway):
    def process_payment(self, amount):
        print(f"💰 UPI Payment of ₹{amount} Successful!")

class CardPayment(PaymentGateway):
    def process_payment(self, amount):
        print(f"💳 Card Payment of ₹{amount} Successful!")

print("\n--- 4️⃣ @abstractmethod Demo ---")
upi = UPIPayment()
upi.process_payment(500)
card = CardPayment()
card.process_payment(1000)


# ============================================================
# 5️⃣ @dataclass — Auto-Generated Class
# ============================================================

@dataclass
class Course:
    name: str
    code: str
    credits: int
    fee: float = 0.0

print("\n--- 5️⃣ @dataclass Demo ---")
c1 = Course("Python Programming", "PY101", 4, 5000)
print(c1)
print("Course Fee:", c1.fee)
