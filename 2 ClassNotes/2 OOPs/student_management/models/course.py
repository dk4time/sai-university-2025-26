class Course:
    code = 501

    def __init__(self, course_name=None, credits=3, fee=0.0, faculty=None, max_seats=30):
        self.course_code = course_name[:3].upper() + str(Course.code)
        Course.code += 1
        self.course_name = course_name
        self.credits = credits
        self.fee = fee
        self.faculty = faculty
        self.max_seats = max_seats
        self.enrolled_students = []

    def seat_available(self):
        return len(self.enrolled_students) < self.max_seats

    def register_student(self, student):
        if self.seat_available():
            self.enrolled_students.append(student)
            return True
        return False

    def __str__(self):
        return f"{self.course_name} ({self.course_code}) | Fee: ₹{self.fee}"
