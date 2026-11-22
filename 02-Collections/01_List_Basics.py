# Lists: ordered, mutable, allow duplicates

fruits = ["apple", "banana", "cherry"]

fruits[1] = "blueberry"          # lists are mutable
fruits.append("orange")
fruits.insert(1, "mango")
fruits.remove("cherry")
print(fruits)

numbers = [1, 2, 10, 4, 5]
print(numbers[2], numbers[-3])   # positive and negative indexing
print(numbers[1:4])              # slicing: stop index is excluded
print(len(numbers), max(numbers), min(numbers), sum(numbers))

numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
print(numbers.pop())             # removes and returns the last item

# append() adds one item, extend() adds many
a = [1, 2]
a.append([3, 4])
b = [1, 2]
b.extend([3, 4])
print(a)
print(b)
