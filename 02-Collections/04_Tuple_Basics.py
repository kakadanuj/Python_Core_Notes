# Tuples: ordered, immutable, allow duplicates

t = (10, 20, 30, 40, 50)
print(t[0], t[-1], t[1:4], t[::-1])

# A single-element tuple needs a comma
single = (10,)
not_a_tuple = (10)
print(type(single))
print(type(not_a_tuple))

# Only two methods: count() and index()
t2 = (10, 20, 10, 30, 10)
print(t2.count(10))
print(t2.index(30))

# Packing and unpacking
packed = 10, 20, 30
a, b, c = packed
print(a, b, c)
