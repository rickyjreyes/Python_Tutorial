# 02_variables.py
#
# Variables store values so you can use them later.

# Basic data types.
dogs = 5                 # int
book_price = 49.99       # float
today = "Sunday"         # string
is_on = True             # bool

print(dogs)
print(book_price)
print(today)
print(is_on)

# Multiple assignment.
puppy, monkey, baby = "puppy", "monkey", "baby"
print(puppy)
print(monkey)
print(baby)

same_value_one = same_value_two = "same value"
print(same_value_one)
print(same_value_two)

# Convert values when combining different types.
age = 42
print("I am " + str(age) + " years old.")

# Local variables exist inside a function.
# Global variables exist outside a function.
global_message = "I am global"


def show_scope():
    local_message = "I am local"
    print(global_message)
    print(local_message)


show_scope()
print(global_message)
