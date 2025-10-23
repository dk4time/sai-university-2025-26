from demo.models.person import Person

class Faculty(Person):
    __code = 201

    def __init__(self, name=None, email=None, phone=None, door_no=None, street=None, city=None, subject=None, designation=None, salary=0.0):
        super().__init__(name, email, phone, door_no, street, city)
        self.emp_id = name[:2].upper() + str(Faculty.__code)
        Faculty.__code += 1
        self.subject = subject
        self.designation = designation
        self.salary = salary
        self.courses_taught = []

    def assign_course(self, course):
        self.courses_taught.append(course)

    def calculate_bonus(self, percentage):
        return (percentage / 100) * self.salary

    def __str__(self):
        return f"{super().__str__()} | EmpID: {self.emp_id} | {self.designation} | {self.subject}"
