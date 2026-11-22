# lambda, map(), filter() and reduce()
from functools import reduce

# lambda: a small anonymous function
square = lambda x: x * x
add = lambda a, b: a + b
even_or_odd = lambda n: "Even" if n % 2 == 0 else "Odd"
print(square(5), add(2, 3), even_or_odd(7))

numbers = [1, 2, 3, 4, 5, 6, 7]

# map(): transform every element
print(list(map(lambda x: x * x, numbers)))

# filter(): keep elements that satisfy a condition
print(list(filter(lambda n: n % 2 == 0, numbers)))

# reduce(): combine all elements into a single value
print(reduce(lambda a, b: a + b, numbers))
print(reduce(lambda a, b: a * b, [1, 2, 3, 4]))
