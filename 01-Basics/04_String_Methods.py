# String methods, indexing and slicing

text = "india is my country"

print(text.capitalize())
print("INDIA IS MY COUNTRY".casefold())
print(text.index("my"))          # raises ValueError if not found
print(text.find("My"))           # returns -1 if not found (case-sensitive)
print("Anuj".isalpha(), "Anuj123".isalpha())
print("abc123".isalnum(), "abc@".isalnum())
print("StreamlineTech".center(22, "*"))
print("StreamlineTech".zfill(20))
print("StreamlineTech".count("e"))
print(text.startswith("india"), "StreamlineTech".endswith("tech"))

# Indexing and slicing
print(text[1:8])
print(text[2:15:2])
print(text[::-1])                # reverse
print(text[-1])
print(text[:-1])
