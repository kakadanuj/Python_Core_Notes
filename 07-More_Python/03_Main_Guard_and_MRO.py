# __name__ == "__main__" and method resolution order (MRO)

def greet():
    print("Hello Python")


class A:
    def show(self):
        print("Class A")

class B(A):
    def show(self):
        print("Class B")

class C(A):
    def show(self):
        print("Class C")

class D(B, C):
    pass


if __name__ == "__main__":
    # This block runs only when the file is executed directly,
    # not when it is imported into another file.
    greet()
    D().show()                    # Class B: Python searches D, B, C, A, object
    print([cls.__name__ for cls in D.mro()])
