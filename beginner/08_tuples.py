# 08_tuples.py
#
# Tuples are ordered collections like lists, but they cannot be changed
# after they are created. This is called immutability.

subjects = ("physics", "chemistry", 1997, 2000)
numbers = (1, 2, 3, 4, 5)
letters = "a", "b", "c", "d"

print("Subjects tuple:", subjects)
print("First subject:", subjects[0])
print("Numbers from index 1 to 3:", numbers[1:4])
print("Letters tuple:", letters)

# Tuples are useful when values belong together.
point = (10, 25)
x, y = point
print("Point x:", x)
print("Point y:", y)

# This would cause an error because tuples cannot be changed:
# subjects[0] = "biology"
