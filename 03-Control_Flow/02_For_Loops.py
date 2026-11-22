# for loops and range()

for i in range(5):                # 0 to 4
    print(i, end=" ")
print()

for i in range(1, 11):            # 1 to 10
    print(i, end=" ")
print()

for i in range(1, 10, 2):         # step of 2
    print(i, end=" ")
print()

for i in range(6, 0, -1):         # reverse
    print(i, end=" ")
print()

# Iterating over a list, tuple and string
for n in [10, 20, 30]:
    print(n)
for ch in "Anuj":
    print(ch)

# Factorial: fact starts at 1 because multiplying by 0 would always give 0
num = 5
fact = 1
for i in range(1, num + 1):
    fact = fact * i
print("Factorial of", num, "is", fact)

# Nested loop: star pattern
for i in range(6, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()
