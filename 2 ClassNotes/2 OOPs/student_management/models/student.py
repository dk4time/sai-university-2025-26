# models/student.py
from .person import Person
from datetime import date

class Student(Person):
    def __init__(self, name, email, phone, student_id, department, year_of_study):
        super().__init__(name, email, phone)
        self.student_id = student_id
        self.department = department
        self.year_of_study = year_of_study
        self.enrollments = []
        self.cgpa = 0.0
        self.attendance = {}
        self.date_joined = date.today()

    # ---- Academic Behavior ----
    def enroll(self, course):
        from .enrollment import Enrollment
        enrollment = Enrollment(self, course)
        self.enrollments.append(enrollment)
        return enrollment

    def mark_attendance(self, course_code, present=True):
        self.attendance[course_code] = self.attendance.get(course_code, 0) + (1 if present else 0)

    def update_cgpa(self, new_grade_point):
        self.cgpa = round((self.cgpa + new_grade_point) / 2, 2)

    def calculate_total_fee(self):
        return sum(e.course.fee for e in self.enrollments)

    def display_enrollments(self):
        for e in self.enrollments:
            print(f"{e.course.course_code} - {e.course.course_name} ({'Paid' if e.payment_status else 'Pending'})")

    def __str__(self):
        return f"Student[{self.student_id}] {self.name} | Dept: {self.department} | CGPA: {self.cgpa}"
