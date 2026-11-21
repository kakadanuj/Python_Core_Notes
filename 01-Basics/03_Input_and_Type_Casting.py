# input() always returns a string, so convert it when you need a number

name = input("Enter your name: ")
age = int(input("Enter your age: "))
price = float(input("Enter total price: "))

print("Hello, " + name + "!")
print("Next year you will be", age + 1)
print("Price with 10 added:", price + 10)
