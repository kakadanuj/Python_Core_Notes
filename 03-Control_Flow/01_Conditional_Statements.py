# Conditional statements

age = 20

# if
if age > 18:
    print("Eligible to buy a ticket")

# if-else
if age > 18:
    print("Adult")
else:
    print("Child")

# if-elif-else: only the first True block runs
marks = 80
if marks > 70:
    print("Grade A")
elif marks > 50:
    print("Grade B")
elif marks > 35:
    print("Grade C")
else:
    print("Failed")

# Ternary
result = "Adult" if age >= 18 else "Child"
print(result)

# Nested if
if age > 18:
    print("You are an adult")
    if age >= 60:
        print("You are a senior citizen")

# Logical operators with conditions
if age >= 18 and age <= 60:
    print("Eligible")
