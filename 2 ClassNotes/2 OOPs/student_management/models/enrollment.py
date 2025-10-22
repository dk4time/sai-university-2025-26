# models/enrollment.py
import datetime

class Enrollment:
    def __init__(self, student, course):
        self.student = student
        self.course = course
        self.enroll_date = datetime.date.today()
        self.payment_status = False
        self.grade = None

    def mark_paid(self):
        self.payment_status = True

    def assign_grade(self, grade):
        self.grade = grade
        self.student.update_cgpa(grade)

    def __str__(self):
        return f"{self.student.name} -> {self.course.course_name} | Grade: {self.grade if self.grade else 'N/A'}"
