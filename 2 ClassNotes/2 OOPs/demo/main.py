class Counter:
    count = 0
    def __init__(self):
        # self.count = 0
        self.increment()

    @classmethod
    def increment(cls):
        Counter.count += 1

    @staticmethod
    def show():
        print(Counter.count)

c1 = Counter() #count = 0 (1)
c2 = Counter() #count = 2
c3 = Counter() #count = 3

print(Counter.count)

#instance(self) class(cls) static(util neither cls nor self)

