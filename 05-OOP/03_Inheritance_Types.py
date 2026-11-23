# Types of inheritance

# Single: one parent, one child
class Parent:
    def parent_method(self):
        print("Parent method")

class Child(Parent):
    def child_method(self):
        print("Child method")

c = Child()
c.parent_method()
c.child_method()


# Multiple: more than one parent
class Father:
    def father_method(self):
        print("Father method")

class Mother:
    def mother_method(self):
        print("Mother method")

class Kid(Father, Mother):
    pass

k = Kid()
k.father_method()
k.mother_method()


# Multilevel: a chain of inheritance
class Grandfather:
    def grandfather_method(self):
        print("Grandfather")

class Dad(Grandfather):
    pass

class Son(Dad):
    pass

Son().grandfather_method()


# Hierarchical: one parent, many children
class Base:
    def hello(self):
        print("Hello from Base")

class Child1(Base):
    pass

class Child2(Base):
    pass

Child1().hello()
Child2().hello()


# Hybrid: a combination of types
class A:
    def show_a(self):
        print("A")

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

D().show_a()
