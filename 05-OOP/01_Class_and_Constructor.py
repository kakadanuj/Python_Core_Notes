# Class, object, constructor and self

class Laptop:
    def __init__(self, name):                 # constructor
        self.name = name                      # instance attribute

    def programming(self):
        return f"My name is {self.name}"


l1 = Laptop("Raj")                            # l1 is a reference to the object
l2 = Laptop("Anuj")
print(l1.programming())
print(l2.name)


# Constructor with default parameters
class Intern:
    def __init__(self, name="Anuj", age=21):
        self.name = name
        self.age = age


i1 = Intern("Anuj", 23)
i2 = Intern()
print(i1.name, i1.age)
print(i2.name, i2.age)
