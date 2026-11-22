# Functions and argument types

def greet(name):                          # name is a parameter
    print("Hello", name)

greet("Pallavi")                          # "Pallavi" is an argument


def add(a, b):
    return a + b                          # return sends a value back

print(add(10, 20))


# print() shows a value, return sends it back
def add_print(a, b):
    print(a + b)

result = add_print(10, 20)
print(result)                             # None


# Positional arguments depend on order
def students(name, age, city):
    print(name, age, city)

students("Gayatri", 22, "Nashik")


# Default argument
def welcome(name="Sakshi"):
    print("Hello", name)

welcome()
welcome("Pallavi")


# Keyword arguments: order does not matter
def stud(name, city):
    print(name, city)

stud(city="Pune", name="Sayali")


# *args collects positional arguments into a tuple
def num(*args):
    print(args)

num(10, 20, 30, 40)


# **kwargs collects keyword arguments into a dictionary
def details(**kwargs):
    return kwargs

print(details(name="Om", age=21, city="Nagar", roll="01"))


# Returning multiple values gives a tuple
def numbers():
    return 10, 20, 30

print(numbers())
