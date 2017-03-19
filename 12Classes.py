class Customer(object):
    """A class that makes customers."""
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def print_info(self):
        print("Customer Name: %s Age: %i Address: %d" % (self.name, self.age, self.address))

Jimmy = Customer("Jimmy", 17, True)
Liz = Customer("Liz", 25, False)

Jimmy.print_info()
Liz.print_info()