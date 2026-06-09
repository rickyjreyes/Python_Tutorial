# Modules.py
#
# Modules are files of reusable Python code. Python includes many modules
# that you can import into your own programs.

import math
import random
from datetime import date

print("Square root of 81:", math.sqrt(81))
print("Pi rounded to 2 decimals:", round(math.pi, 2))

# randint includes both the first and last number.
dice_roll = random.randint(1, 6)
print("Dice roll:", dice_roll)

# The date module can work with calendar dates.
today = date.today()
print("Today is:", today)

# You can also write your own helper functions and reuse them.
def circle_area(radius):
    return math.pi * radius ** 2


print("Area of a circle with radius 3:", round(circle_area(3), 2))
