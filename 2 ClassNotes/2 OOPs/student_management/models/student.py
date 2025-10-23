from demo.models.person import Person
from demo.models.enrollment import Enrollment

class Student(Person):
    code = 1001

    def __init__(self, name=None, email=None, phone=None, door_no=None, street=None, city=None, department=None, year_of_study=None):
        super().__init__(name, email, phone, door_no, street, city)
        self.student_id = name[:2].upper() + str(Student.code)
        Student.code += 1
        self.department = department
        self.year_of_study = year_of_study
        self.enrollments = []
        self.cgpa = 0.0
        self.attendance = {}
        self.account = None

    def enroll(self, course):
        enrollment = Enrollment(self, course)
        self.enrollments.append(enrollment)
        course.register_student(self)
        return enrollment

    def mark_attendance(self, course_code, present=True):
        self.attendance[course_code] = self.attendance.get(course_code, 0) + (1 if present else 0)

    def update_cgpa(self, new_grade_point):
        self.cgpa = round((self.cgpa + new_grade_point) / 2, 2)

    def calculate_total_fee(self):
        return sum(e.course.fee for e in self.enrollments)

    def link_bank_account(self, account):
        self.account = account

    def __str__(self):
        return f"{super().__str__()} | ID: {self.student_id} | Dept: {self.department.name if self.department else 'None'} | CGPA: {self.cgpa}"
