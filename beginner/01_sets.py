# 01_sets.py
#
# A set stores unique values. Sets are useful when you care about
# membership, duplicates, or comparing groups of values.

favorite_languages = {"Python", "JavaScript", "C++", "Python"}
print("Set removes duplicates:", favorite_languages)

favorite_languages.add("Go")
print("After add:", favorite_languages)

favorite_languages.discard("C++")
print("After discard:", favorite_languages)

print("Is Python included?", "Python" in favorite_languages)
print("Is Ruby included?", "Ruby" in favorite_languages)

frontend = {"HTML", "CSS", "JavaScript"}
backend = {"Python", "SQL", "JavaScript"}

print("Union:", frontend | backend)
print("Intersection:", frontend & backend)
print("Only frontend:", frontend - backend)
print("Only one side:", frontend ^ backend)

numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = set(numbers)
print("Unique numbers:", unique_numbers)
