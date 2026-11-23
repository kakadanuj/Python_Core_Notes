# Comprehensions

squares = [x * x for x in range(1, 6)]
print(squares)

even = [x for x in range(1, 11) if x % 2 == 0]
print(even)

unique_squares = {x * x for x in range(1, 6)}
print(unique_squares)

square_map = {x: x * x for x in range(1, 6)}
print(square_map)

# Generator expression: produces values lazily
gen = (x * x for x in range(1, 6))
print(next(gen))
print(next(gen))
