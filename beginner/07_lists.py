# 07_lists.py
#
# Lists store ordered values that can be changed.

subjects = ["physics", "chemistry", 1997, 2000]
numbers = [1, 2, 3, 4, 5]
letters = ["a", "b", "c", "d"]

print("subjects[0]:", subjects[0])
print("numbers[1:5]:", numbers[1:5])
print("letters:", letters)

print("Value at index 2:")
print(subjects[2])

subjects[2] = 2001
print("New value at index 2:")
print(subjects[2])

subjects.append("biology")
print("After append:", subjects)

subjects.remove("chemistry")
print("After remove:", subjects)
