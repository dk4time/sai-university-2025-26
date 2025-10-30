"""
-------------------------------------------------------------
🎓 DECORATORS DEMO FILE — Trainer Version
-------------------------------------------------------------
Covers 5 Key Features:
1️⃣ Basic Decorator
2️⃣ Decorator Handling Arguments
3️⃣ Decorator With Its Own Arguments
4️⃣ Class-Based Decorator
5️⃣ Real-World Decorator Use Cases (Logging, Auth, Timing)
-------------------------------------------------------------
Author: Dineshkumar 💻
-------------------------------------------------------------
"""

import time
import uuid

# ============================================================
# 1️⃣ BASIC DECORATOR — Wraps a Function
# ============================================================

def greet_decorator(func):
    def wrapper():
        print("[Before] Getting ready to greet...")
        func()
        print("[After] Greeting completed!")
    return wrapper

@greet_decorator
def say_hello():
    print("Hello, Python Students!")

print("\n--- 1️⃣ Basic Decorator Demo ---")
say_hello()


# ============================================================
# 2️⃣ DECORATOR WITH FUNCTION ARGUMENTS — *args, **kwargs
# ============================================================

def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"[LOG] Calling {func.__name__} with {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"[LOG] {func.__name__} returned {result}")
        return result
    return wrapper

@log_decorator
def add(a, b):
    return a + b

print("\n--- 2️⃣ Decorator with Args Demo ---")
add(10, 5)


# ============================================================
# 3️⃣ DECORATOR WITH ITS OWN ARGUMENTS — @repeat(3)
# ============================================================

def repeat(times):
    """Decorator factory that repeats a function 'times' number of times."""
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(times):
                print(f"➡️  Run {i+1} of {times}")
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def motivate():
    print("Keep Learning, Keep Growing! 💪")

print("\n--- 3️⃣ Decorator with Its Own Arguments Demo ---")
motivate()


# ============================================================
# 4️⃣ CLASS-BASED DECORATOR — Uses __call__()
# ============================================================

class Logger:
    """Decorator implemented as a class to log function calls."""
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print(f"[CLASS-LOGGER] Running {self.func.__name__} with {args} {kwargs}")
        result = self.func(*args, **kwargs)
        print(f"[CLASS-LOGGER] {self.func.__name__} finished execution.")
        return result

@Logger
def welcome_user(name):
    print(f"Welcome, {name}! 🎉")

print("\n--- 4️⃣ Class-Based Decorator Demo ---")
welcome_user("Dinesh")


# ============================================================
# 5️⃣ REAL-WORLD DECORATORS — Logging, Auth, Timing
# ============================================================

# 🕒 Timing Decorator
def timer(func):
    """Measures function execution time."""
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"[TIMER] {func.__name__} executed in {end - start:.5f}s")
        return result
    return wrapper

# 🔐 Authorization Decorator
def require_login(func):
    """Checks if user is logged in before accessing function."""
    def wrapper(user, *args, **kwargs):
        if not user.get("is_logged_in"):
            print("🚫 Access Denied! Please log in.")
            return
        print(f"✅ Access Granted for {user['name']}")
        return func(user, *args, **kwargs)
    return wrapper

# 💰 Payment Logging Decorator
def payment_logger(func):
    """Logs simulated payment transactions."""
    def wrapper(*args, **kwargs):
        transaction_id = str(uuid.uuid4())[:8]
        print(f"[PAYMENT] Transaction ID: {transaction_id}")
        return func(*args, **kwargs)
    return wrapper

@timer
@require_login
@payment_logger
def make_payment(user, amount):
    print(f"💵 Processing payment of ₹{amount} for {user['name']}")
    time.sleep(1)
    print("✅ Payment Successful!")

print("\n--- 5️⃣ Real-World Decorators Demo ---")

user1 = {"name": "Dinesh", "is_logged_in": True}
user2 = {"name": "Hari", "is_logged_in": False}

make_payment(user1, 2500)
make_payment(user2, 2500)


"""
-------------------------------------------------------------
🎯 Summary of Covered Features
-------------------------------------------------------------
| Feature             | Concept               | Example                        |
| ------------------- | --------------------- | ------------------------------ |
| Basic Decorator     | Wraps a function      | @greet_decorator               |
| With Args           | Handle parameters     | def wrapper(*args, **kwargs)   |
| With Decorator Args | Add outer function    | @repeat(3)                     |
| Class Decorator     | Use __call__          | @Logger                        |
| Real Usage          | Logging/Auth/Timing   | @require_login, @timer         |
-------------------------------------------------------------
"""
