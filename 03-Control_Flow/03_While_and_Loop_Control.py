# while loop and loop control statements

i = 1
while i <= 5:
    print(i)
    i = i + 1                     # update the variable, or the loop never ends

# Multiplication table
n = 2
i = 1
while i <= 10:
    print(n, "x", i, "=", n * i)
    i = i + 1

# break stops the loop completely
for i in range(10):
    if i == 5:
        break
    print(i, end=" ")
print()

# continue skips only the current iteration
for i in range(10):
    if i == 5:
        continue
    print(i, end=" ")
print()

# pass does nothing; it is a placeholder
for i in range(3):
    pass
