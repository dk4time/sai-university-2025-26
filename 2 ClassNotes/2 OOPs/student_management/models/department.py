# models/department.py
class Department:
    def __init__(self, dept_code, name, hod=None):
        self.dept_code = dept_code
        self.name = name
        self.hod = hod
        self.courses = []
        self.students = []

    def add_course(self, course):
        self.courses.append(course)

    def add_student(self, student):
        self.students.append(student)

    def display_info(self):
        print(f"Department: {self.name} | HOD: {self.hod.name if self.hod else 'Not Assigned'}")
        print(f"Total Courses: {len(self.courses)}, Total Students: {len(self.students)}")
