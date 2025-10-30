class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    def show_instance(self):
        print("Instance method — count =", Counter.count)

    @classmethod
    def show_class(cls):
        print("Class method — count =", cls.count)

    @staticmethod
    def show_static():
        print("Static method — no access to self or cls")

c1 = Counter()
c2 = Counter()

c1.show_instance()
Counter.show_class()
Counter.show_static()
