# Comprehensions.py
#
# Comprehensions create lists or dictionaries from existing data in a compact way.

numbers = [1, 2, 3, 4, 5]

squares = [number ** 2 for number in numbers]
print("Squares:", squares)

# Add an if condition to keep only some values.
even_numbers = [number for number in numbers if number % 2 == 0]
print("Even numbers:", even_numbers)

names = ["ricky", "maya", "jordan"]
capitalized_names = [name.title() for name in names]
print("Capitalized names:", capitalized_names)

# Dictionary comprehensions create key/value pairs.
score_by_name = {name.title(): len(name) for name in names}
print("Score by name:", score_by_name)
