from demo.models.address import Address

class Person:
    def __init__(self, name=None, email=None, phone=None, door_no=None, street=None, city=None):
        print("Person constructor")
        self.name = name
        self.email = email
        self.phone = phone
        self.address = Address(door_no, street, city)

    def is_valid_phone(self):
        return self.phone.isdigit() and len(self.phone) == 10

    def is_valid_email(self):
        return self.email and "@" in self.email and "." in self.email

    def update_contact(self, phone=None, email=None, address=None):
        if phone:
            self.phone = phone
        if email:
            self.email = email
        if address:
            self.address = address

    def __str__(self):
        return f"{self.name} | {self.email} | {self.phone} | {self.address}"
