# models/course.py
class Course:
    def __init__(self, course_code, course_name, credits, fee, faculty):
        self.course_code = course_code
        self.course_name = course_name
        self.credits = credits
        self.fee = fee
        self.faculty = faculty

    def __str__(self):
        return f"{self.course_code} | {self.course_name} | Credits: {self.credits} | Fee: ₹{self.fee}"
