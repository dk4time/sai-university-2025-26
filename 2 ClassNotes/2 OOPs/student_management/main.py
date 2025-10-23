from demo.models.department import Department
from demo.models.faculty import Faculty
from demo.models.student import Student
from demo.models.course import Course
from demo.models.bank_account import BankAccount
from demo.models.upi_payment import UPIPayment

# Create department & faculty
dept = Department("Computer Science")
hod = Faculty("Meena", "meena@uni.edu", "9876543210", "1", "MG Road", "Chennai", "Python", "Professor", 90000)
dept.hod = hod
dept.add_faculty(hod)

# Create student
stu = Student("Dinesh", "dinesh@mail.com", "9876501234", "2", "Anna St", "Chennai", dept, 2)
dept.add_student(stu)

# Create course and enroll
course = Course("Python Programming", 4, 5000.0, hod)
dept.add_course(course)
enroll = stu.enroll(course)

# Payment
upi = UPIPayment()
upi.process_payment(enroll, course.fee)

# Link bank account
acc = BankAccount(stu, 10000)
stu.link_bank_account(acc)

print(stu)
