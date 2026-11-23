# Iterators and generators

# Iterator: gives one value at a time
numbers = [10, 20, 30]
it = iter(numbers)
print(next(it))
print(next(it))
print(next(it))
# next(it) now would raise StopIteration


# Generator function: yield pauses the function and keeps its state
def count():
    yield 1
    yield 2
    yield 3


for value in count():
    print(value)


# Generators are memory efficient: values are produced only when needed
def even_numbers(limit):
    for n in range(0, limit + 1, 2):
        yield n


print(list(even_numbers(10)))
