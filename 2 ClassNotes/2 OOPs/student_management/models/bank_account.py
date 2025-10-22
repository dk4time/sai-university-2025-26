# models/bank_account.py
class BankAccount:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise ValueError("Balance cannot be negative.")
        self.__balance = amount

    def deposit(self, amount):
        self.balance = self.__balance + amount

    def withdraw(self, amount):
        if amount > self.__balance:
            raise ValueError("Insufficient funds.")
        self.__balance -= amount

    def __str__(self):
        return f"BankAccount[{self.owner}] | Balance: ₹{self.__balance}"
