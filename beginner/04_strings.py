# 04_strings.py
#
# Strings store text. You can index, slice, format, and transform them.

message = "I am a string"
print(message)

apostrophe = "don't won't I'm"
print(apostrophe)

word = "MINECRAFT"
print("First letter:", word[0])

access = "Access!"
print(access)
print(access[0])
print(access[2:5])
print(access[2:])
print(access * 4)
print(access + " TEST")

animal = "lion"
print("Length:", len(animal))
print("Lowercase:", "CAT".lower())
print("Uppercase:", "raccoon".upper())

print("%s are number %d" % ("games", 21))
print(f"{animal.title()} has {len(animal)} letters.")
