# Operators in Python

a, b = 10, 3

# Arithmetic
print("Arithmetic Operators:-")
print("a =", a, ", b =", b)
print("a + b  =", a + b)
print("a - b  =", a - b)
print("a * b  =", a * b)
print("a / b  =", a / b)      # always a float
print("a // b =", a // b)     # floor division
print("a % b  =", a % b)      # remainder
print("a ** b =", a ** b)     # power

print()
# Assignment
print("Assignment Operators:-")
x = 20
x += 10
print("x = 20, then x += 10")
print("x after += 10:", x)

print()
# Comparison
print("Comparison Operators:-")
print("a =", a, ", b =", b)
print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)

print()
# Logical
print("Logical Operators:-")
print("5 > 2 and 10 > 5:", 5 > 2 and 10 > 5)
print("15 >= 18 or 10 > 5:", 15 >= 18 or 10 > 5)
print("not (10 > 20):", not (10 > 20))

print()
# Bitwise
print("Bitwise Operators:-")
print("5 & 3 =", 5 & 3)
print("5 | 3 =", 5 | 3)
print("5 ^ 3 =", 5 ^ 3)
print("~5    =", ~5)         # -(5 + 1)
print("5 << 1 =", 5 << 1)
print("5 >> 1 =", 5 >> 1)

print()
# Membership
print("Membership Operators:-")
print("'a' in 'apple':", 'a' in 'apple')
print("10 not in [1, 2, 3]:", 10 not in [1, 2, 3])

print()
# Identity vs equality
print("Identity vs Equality:-")
p = [1, 2]
q = [1, 2]
r = p
print("p = [1, 2], q = [1, 2], r = p")
print("p == q:", p == q)      # same values
print("p is q:", p is q)      # different objects
print("p is r:", p is r)      # same object
