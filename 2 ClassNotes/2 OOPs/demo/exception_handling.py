"""
-------------------------------------------------------------
🎓 REAL-TIME EXCEPTION HANDLING DEMO — Trainer Edition
-------------------------------------------------------------
Concepts Covered:
✅ try / except / else / finally
✅ Multiple exception types
✅ raise keyword
✅ Custom exception class
✅ Nested exception handling
✅ Resource (file) handling
-------------------------------------------------------------
Scenario:
A student fee payment system that validates:
- Student ID
- Fee amount
- Payment status
-------------------------------------------------------------
Author: Dineshkumar 💻
-------------------------------------------------------------
"""

from datetime import datetime


# -------------------------------------------------------------
# 1️⃣ Custom Exception Class
# -------------------------------------------------------------
class InvalidStudentError(Exception):
    """Raised when the student ID is not found"""
    pass


class InsufficientBalanceError(Exception):
    """Raised when account balance is too low"""
    pass


class PaymentError(Exception):
    """Raised for generic payment issues"""
    pass


# -------------------------------------------------------------
# 2️⃣ Supporting Classes
# -------------------------------------------------------------
class Student:
    def __init__(self, student_id, name, balance):
        self.student_id = student_id
        self.name = name
        self.balance = balance


class FeePaymentSystem:
    def __init__(self):
        # simulate a student database
        self.students = {
            "ST101": Student("ST101", "Dinesh", 15000),
            "ST102": Student("ST102", "Hari", 5000),
            "ST103": Student("ST103", "Meena", 0)
        }

    def process_payment(self, student_id, fee_amount):
        """
        Handles fee payment with full exception handling demo
        """
        try:
            # --------------- Validation Layer -------------------
            if student_id not in self.students:
                raise InvalidStudentError(f"❌ Student ID '{student_id}' not found!")

            student = self.students[student_id]

            if fee_amount <= 0:
                raise ValueError("❌ Fee amount must be positive!")

            # --------------- Payment Process -------------------
            try:
                if student.balance < fee_amount:
                    raise InsufficientBalanceError("🚫 Insufficient balance for payment!")

                student.balance -= fee_amount
                self.generate_receipt(student, fee_amount)

            except InsufficientBalanceError as e:
                print("⚠️", e)
                raise PaymentError("Payment failed due to insufficient funds!") from e

            else:
                print(f"✅ Payment of ₹{fee_amount} successful for {student.name}")

            # --------------- Post Payment (no exception) --------
        except (InvalidStudentError, ValueError) as e:
            print("⚠️ Validation Error:", e)

        except PaymentError as e:
            print("💥 Transaction Error:", e)

        except Exception as e:
            print("❗ Unexpected Error:", e)

        else:
            print("🎉 Transaction completed successfully!")

        finally:
            print("🧾 Transaction process ended.\n")

    def generate_receipt(self, student, amount):
        """
        File handling inside try/finally — ensures file closure
        """
        try:
            file = open("fee_receipt.txt", "a")
            file.write(f"{datetime.now()} | {student.student_id} | {student.name} | ₹{amount}\n")
        except Exception as e:
            print("⚠️ Error writing to file:", e)
        finally:
            file.close()
            print("📁 Receipt file updated (finally block executed).")


# -------------------------------------------------------------
# 3️⃣ TESTING / TRAINER DEMO FLOW
# -------------------------------------------------------------
if __name__ == "__main__":
    fps = FeePaymentSystem()

    print("\n--- 🧍 Valid Payment ---")
    fps.process_payment("ST101", 5000)

    print("\n--- 🚫 Invalid Student ID ---")
    fps.process_payment("ST999", 3000)

    print("\n--- 🚫 Negative Amount ---")
    fps.process_payment("ST102", -2000)

    print("\n--- 💸 Insufficient Balance ---")
    fps.process_payment("ST103", 4000)

    print("\n--- ✅ Final Student Balances ---")
    for sid, s in fps.students.items():
        print(f"{s.name} ({s.student_id}) → Balance: ₹{s.balance}")
