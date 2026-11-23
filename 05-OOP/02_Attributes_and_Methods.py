# Types of attributes and methods

class Car:
    total_cars = 0                                # class attribute (shared)

    def __init__(self, model):
        self.model = model                        # instance attribute
        Car.total_cars += 1

    def show(self):                               # instance method
        return f"Model: {self.model}"

    @classmethod
    def car_count(cls):                           # class method
        return f"Total cars = {cls.total_cars}"

    @staticmethod
    def add(a, b):                                # static method: no self or cls
        return a + b


c1 = Car("Nexon")
c2 = Car("Harrier")
print(c1.show())
print(Car.car_count())
print(Car.add(2, 4))
