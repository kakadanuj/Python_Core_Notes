# Dictionaries: key-value pairs, mutable, keys must be unique

student = {"id": 123, "name": "anuj", "age": 23}

print(student["name"])
print(student.get("mobile"))              # None, no error
print(student.get("mobile", "not found")) # default value

print(student.keys())
print(student.values())
print(student.items())

student.update({"age": 24})               # modify an existing key
student.update({"city": "Pune"})          # add a new key
print(student)

print(student.pop("id"))                  # remove a key, returns its value
print(student.popitem())                  # removes the last inserted pair
print(student)

copy_of_student = student.copy()
student.clear()
print(student, copy_of_student)

# A repeated key keeps the latest value
duplicate = {"id": 123, "name": "anuj", "id": 456}
print(duplicate)

# Nested dictionary
students = {
    "student1": {"id": 123, "name": "anuj", "age": 23},
    "student2": {"id": 124, "name": "rahul", "age": 24},
}
print(students["student2"]["name"])
