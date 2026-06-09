# Dictionaries.py
#
# Dictionaries store information as key/value pairs.
# Use a key to look up its matching value.

student = {
    "name": "Ricky",
    "age": 17,
    "favorite_subject": "Computer Science",
    "is_enrolled": True,
}

print("Student name:", student["name"])
print("Favorite subject:", student["favorite_subject"])

# Add a new key/value pair.
student["grade"] = "A"
print("Grade:", student["grade"])

# Update an existing value.
student["age"] = 18
print("Updated age:", student["age"])

# Safely get a value that might not exist.
print("Locker number:", student.get("locker_number", "No locker assigned"))

# Loop through every key and value in the dictionary.
print("\nStudent profile:")
for key, value in student.items():
    print(key, "=", value)

# Dictionaries can also be nested inside lists.
students = [
    {"name": "Ricky", "grade": 95},
    {"name": "Maya", "grade": 88},
    {"name": "Jordan", "grade": 91},
]

print("\nClass grades:")
for person in students:
    print(person["name"], "earned", person["grade"])
