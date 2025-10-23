from datetime import date

class Enrollment:
    def __init__(self, student, course):
        self.student = student
        self.course = course
        self.enroll_date = date.today()
        self.payment_status = "Pending"
        self.grade = None

    def mark_paid(self):
        self.payment_status = "Paid"

    def assign_grade(self, grade):
        self.grade = grade
        self.student.update_cgpa(grade)

    def __str__(self):
        return f"{self.student.name} → {self.course.course_name} | {self.payment_status} | Grade: {self.grade}"
