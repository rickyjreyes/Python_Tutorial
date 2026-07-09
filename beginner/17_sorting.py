# 17_sorting.py
#
# Python has built-in sorting tools. Learn these before writing sorting
# algorithms by hand.

scores = [91, 72, 88, 100, 65]

print("Original scores:", scores)
print("Sorted copy:", sorted(scores))
print("Original after sorted():", scores)

scores.sort()
print("Original after .sort():", scores)

names = ["Zoey", "anna", "Chris", "ben"]
print("Default name sort:", sorted(names))
print("Case-insensitive sort:", sorted(names, key=str.lower))

students = [
    {"name": "Alice", "score": 92},
    {"name": "Marco", "score": 81},
    {"name": "Jules", "score": 98},
]

by_score = sorted(students, key=lambda student: student["score"])
highest_first = sorted(students, key=lambda student: student["score"], reverse=True)

print("Students by score:", by_score)
print("Highest first:", highest_first)
