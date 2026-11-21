# Primary data types in Python

x = 10               # int
pi = 3.14            # float
msg = "Hello"        # str
a, b = 10, 20
result = a < b       # bool (True or False)
z = 2 + 3j           # complex (real + imaginary part)

for value in (x, pi, msg, result, z):
    print(value, "->", type(value))
