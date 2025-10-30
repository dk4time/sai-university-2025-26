"""
-------------------------------------------------------------
🎓 CLASSMETHOD vs STATICMETHOD vs INSTANCE METHOD — Trainer Demo
-------------------------------------------------------------
Topic: Real-world example using BankAccount system
-------------------------------------------------------------
Author: Dineshkumar 💻
-------------------------------------------------------------
"""

import datetime


class BankAccount:
    # Class variable (shared across all accounts)
    bank_name = "Python National Bank"
    total_accounts = 0
    interest_rate = 0.05   # 5% interest for all accounts

    # -----------------------------
    # Instance Method Section
    # -----------------------------
    def __init__(self, holder_name, balance=0.0):
        self.holder_name = holder_name
        self.balance = balance
        BankAccount.total_accounts += 1

    def deposit(self, amount):
        """Instance method - modifies object data"""
        self.balance += amount
        print(f"💰 {self.holder_name} deposited ₹{amount}. New Balance = ₹{self.balance}")

    def withdraw(self, amount):
        """Instance method - modifies object data"""
        if amount > self.balance:
            print(f"🚫 Insufficient funds for {self.holder_name}")
        else:
            self.balance -= amount
            print(f"💸 {self.holder_name} withdrew ₹{amount}. Balance = ₹{self.balance}")

    def show_balance(self):
        """Instance method - reads object data"""
        print(f"👤 Account Holder: {self.holder_name} | Balance: ₹{self.balance}")

    # -----------------------------
    # Class Method Section
    # -----------------------------
    @classmethod
    def update_interest_rate(cls, new_rate):
        """Class method - modifies class-level data"""
        cls.interest_rate = new_rate
        print(f"🏦 Interest rate updated to {cls.interest_rate * 100}% for all accounts.")

    @classmethod
    def show_bank_info(cls):
        """Class method - reads class-level data"""
        print(f"🏛️ Welcome to {cls.bank_name} | Total Accounts: {cls.total_accounts}")

    @classmethod
    def from_string(cls, info):
        """Alternate constructor - creates instance from string"""
        name, bal = info.split("-")
        return cls(name, float(bal))

    # -----------------------------
    # Static Method Section
    # -----------------------------
    @staticmethod
    def calculate_interest(amount, years):
        """Static method - independent utility (no self/cls)"""
        return amount * (1 + BankAccount.interest_rate) ** years

    @staticmethod
    def get_timestamp():
        """Static method - helper for logs"""
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

if __name__ == "__main__":

    print("\n--- 🏛️ Class Method Demo ---")
    BankAccount.show_bank_info()     # Class method
    BankAccount.update_interest_rate(0.07)

    print("\n--- 🧍‍♂️ Instance Method Demo ---")
    acc1 = BankAccount("Dinesh", 5000)
    acc2 = BankAccount.from_string("Hari-10000")  # Class method used as alternate constructor

    acc1.deposit(2000)
    acc2.withdraw(2500)
    acc1.show_balance()
    acc2.show_balance()

    print("\n--- ⚙️ Static Method Demo ---")
    print("Projected Balance (5 years): ₹", round(BankAccount.calculate_interest(acc1.balance, 5), 2))
    print("Log Timestamp:", BankAccount.get_timestamp())

    print("\n--- 🧾 Summary ---")
    BankAccount.show_bank_info()
