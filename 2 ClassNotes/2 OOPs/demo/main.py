import datetime

class AgeNotFound(Exception):
    pass

try:
    nums = [1, 2]
    quo = 5/3
    print(nums[1])
    print("quo:", quo)
    age = 4
    if age < 18:
        raise AgeNotFound("not eligible error")
except ArithmeticError as e:
    print("Arithmeric:", e)

except Exception as e:
    print(e)

else:
    print("No exception raised")
finally:
    print(datetime.datetime.now())