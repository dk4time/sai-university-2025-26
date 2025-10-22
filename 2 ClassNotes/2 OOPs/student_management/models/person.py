# models/person.py
import re

class Person:
    def __init__(self, name, email, phone, address=""):
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address

    # ---- Validation Methods ----
    def is_valid_email(self):
        return bool(re.match(r"[^@]+@[^@]+\.[^@]+", self.email))

    def is_valid_phone(self):
        return len(self.phone) == 10 and self.phone.isdigit()

    # ---- Utility Methods ----
    def update_contact(self, email=None, phone=None):
        if email:
            self.email = email
        if phone:
            self.phone = phone

    def __str__(self):
        return f"{self.name} ({self.email}, {self.phone})"
