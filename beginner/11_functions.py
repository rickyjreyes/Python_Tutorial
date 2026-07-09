# 11_functions.py
#
# Functions group reusable code under a name.


def say_hello():
    print("hello world")


say_hello()
say_hello()

# Functions can accept inputs called parameters.
def greet(name):
    print("Hello,", name)


greet("Ricky")
greet("Maya")

# Functions can return values.
def add(first_number, second_number):
    return first_number + second_number


result = add(3, 4)
print("3 + 4 =", result)
