# 03_math.py
#
# Python can perform common arithmetic operations.

addition = 1 + 2
subtraction = 2 - 1
multiplication = 3 * 3
division = 99 / 11
modulus = 5 % 3
exponent = 2 ** 3

print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)
print("Modulus:", modulus)
print("Exponent:", exponent)

# Updating a number.
a = 5
a += 3
print("Updated a:", a)

# Order of operations.
print(5 + 4 + 3 * 7)
print((5 + 4 + 3) * 7)

# Built-in math helpers.
print("Minimum:", min(12, 34, 2, 15, 56, 45))
print("Maximum:", max(12, 34, 2, 15, 56, 45))
print("Absolute value:", abs(-11))
print("Power:", pow(2, 5))

import random

print("Random number:", random.random())
