class BankAccount:
    def __init__(self, owner=None, balance=0.0):
        self.owner = owner
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise ValueError("Balance cannot be negative")
        self.__balance = amount

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Invalid deposit amount")
        self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            raise ValueError("Insufficient funds")
        self.__balance -= amount

    def transfer_to(self, other_account, amount):
        self.withdraw(amount)
        other_account.deposit(amount)

    def __str__(self):
        return f"Account({self.owner.name}): ₹{self.__balance:.2f}"
