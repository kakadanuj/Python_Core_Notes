# Exception handling: try, except, else, finally, raise

def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: division by zero is not allowed.")
    else:
        print("The output is:", result)       # runs only if no exception
    finally:
        print("Division attempt finished")    # always runs


divide(10, 2)
divide(10, 0)


# Handle specific exceptions
def to_int(text):
    try:
        return int(text)
    except ValueError:
        print("Please enter a valid integer")


to_int("42")
to_int("abc")


# raise: manually trigger an exception
def check_age(age):
    if age < 18:
        raise ValueError("Age less than 18 is not allowed")
    print("You are eligible to vote")


check_age(20)
try:
    check_age(16)
except ValueError as error:
    print("Caught:", error)
