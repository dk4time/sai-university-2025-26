class Address:
    def __init__(self, door_no=None, street=None, city=None):
        self.door_no = door_no
        self.street = street
        self.city = city

    def __str__(self):
        return f"{self.door_no}, {self.street}, {self.city}"
