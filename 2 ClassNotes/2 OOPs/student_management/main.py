# main.py
from models.faculty import Faculty
from models.student import Student
from models.department import Department
from models.course import Course
from models.upi_payment import UPIPayment
from utils.logger import Logger

def main():
    Logger.log("System booting up...")

    # Faculty
    hod = Faculty("Dr. Meena", "meena@college.com", "9876543210", "F101", "Python", "HOD", 90000)

    # Department
    cse = Department("CSE", "Computer Science", hod)

    # Courses
    c1 = Course("PY101", "Python Programming", 3, 4000, hod)
    c2 = Course("DB102", "Database Systems", 4, 5000, hod)
    cse.add_course(c1)
    cse.add_course(c2)

    # Student
    s1 = Student("Dinesh", "dinesh@college.com", "9988776655", "S101", "CSE", 3)
    cse.add_student(s1)

    # Enrollment
    e1 = s1.enroll(c1)
    e2 = s1.enroll(c2)
    Logger.log(f"{s1.name} enrolled in 2 courses.")

    # Payment
    payment = UPIPayment()
    payment.process_payment(e1, c1.fee)
    payment.process_payment(e2, c2.fee)

    Logger.log("All payments successful.")
    s1.display_enrollments()

    Logger.log("Generating report...")
    cse.display_info()
    print(f"{s1.name}'s CGPA: {s1.cgpa}")

if __name__ == "__main__":
    main()
