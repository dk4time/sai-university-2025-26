# models/faculty.py
from .person import Person

class Faculty(Person):
    def __init__(self, name, email, phone, emp_id, subject, designation, salary):
        super().__init__(name, email, phone)
        self.emp_id = emp_id
        self.subject = subject
        self.designation = designation
        self.salary = salary
        self.courses_taught = []

    def assign_course(self, course):
        self.courses_taught.append(course)

    def calculate_bonus(self, percentage):
        return (self.salary * percentage) / 100

    def __str__(self):
        return f"Faculty[{self.emp_id}] {self.name} - {self.designation} | {self.subject}"
