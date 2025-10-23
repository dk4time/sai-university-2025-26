class Department:
    code = 101

    def __init__(self, name=None, hod=None):
        self.dept_code = name[:2].upper() + str(Department.code)
        Department.code += 1
        self.name = name
        self.hod = hod
        self.__courses = []
        self.__students = []
        self.__faculties = []

    def add_course(self, course):
        self.courses.append(course)

    def add_student(self, student):
        self.students.append(student)

    def add_faculty(self, faculty):
        self.__faculties.append(faculty)

    def get_courses(self):
        return self.__courses

    def get_students(self):
        return self.__students

    def get_faculties(self):
        return self.__faculties

    def remove_student(self, student_id):
        self.students = [s for s in self.students if s.student_id != student_id]

    def display_info(self):
        print(f"Department: {self.name} ({self.dept_code})")
        print(f"HOD: {self.hod.name if self.hod else 'None'}")
        print(f"Courses: {[c.course_name for c in self.courses]}")
        print(f"Students: {[s.name for s in self.students]}")

    def __str__(self):
        return f"{self.name} ({self.dept_code})"
