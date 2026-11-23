# File handling: modes r, w, a, x and the with statement
from pathlib import Path

# Write the demo file next to this script
path = Path(__file__).parent / "demo_output.txt"

# "w" creates the file and overwrites any existing content
with open(path, "w") as file:
    file.write("Hello World!\n")

# "a" appends at the end
with open(path, "a") as file:
    file.write("Good Morning!\n")
    file.write("Streamline Tech\n")

# read(), readline() and readlines()
with open(path, "r") as file:
    print(file.read())

with open(path, "r") as file:
    print(file.readline())

with open(path, "r") as file:
    print(file.readlines())

# tell() and seek() work with the file cursor
with open(path, "r") as file:
    print(file.tell())
    file.seek(0)
    print(file.read(5))

# Reading a missing file raises FileNotFoundError
try:
    with open(path.parent / "missing.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found")
