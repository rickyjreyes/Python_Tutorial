# Classes.py
#
# Classes let us create our own data types with attributes and methods.

class Customer(object):
    """A simple class that stores customer information."""

    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def print_info(self):
        print("Customer Name: %s Age: %i Address: %s" % (self.name, self.age, self.address))

    def birthday(self):
        self.age += 1
        print(self.name, "is now", self.age)


jimmy = Customer("Jimmy", 17, "123 Python Lane")
liz = Customer("Liz", 25, "456 Tutorial Street")

jimmy.print_info()
liz.print_info()
jimmy.birthday()
