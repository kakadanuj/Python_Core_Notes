# Recursion: a function that calls itself
# Every recursive function needs a base condition that stops it.

def countdown(n):
    if n == 0:                    # base condition
        return
    print(n)
    countdown(n - 1)              # recursive call


def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


countdown(5)
print("5! =", factorial(5))
for i in range(7):
    print(fibonacci(i), end=" ")
print()
