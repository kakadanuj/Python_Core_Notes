# Polymorphism: one name, many behaviours

# Same method name, different classes
class UPI:
    def pay(self):
        print("Payment through UPI")

class CreditCard:
    def pay(self):
        print("Payment through Credit Card")

class Cash:
    def pay(self):
        print("Payment through Cash")

for method in (UPI(), CreditCard(), Cash()):
    method.pay()


# Method overloading is not built in; default arguments give a similar result
class Calculator:
    def add(self, a, b, c=0):
        return a + b + c

calc = Calculator()
print(calc.add(10, 20))
print(calc.add(10, 20, 10))


# Operator overloading: define what + means for our own objects
class Student:
    def __init__(self, marks):
        self.marks = marks

    def __add__(self, other):
        return self.marks + other.marks

print(Student(60) + Student(90))


# Method overriding and super()
class Person:
    def work(self):
        print("Streamline is an IT company")

class Intern(Person):
    def work(self):
        super().work()                        # call the parent version
        print("My work is done")

Intern().work()
