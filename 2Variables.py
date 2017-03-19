# variables.py
#
# What are Variables?

# Variables
i_am_a_variable = 7

# Basic DATA TYPES
dogs = 5           #int
today = "Sunday"   #string
money = 49.343     #float
is_On = True       #bool

# Variable a = 5 is and int
a = 5
print(a)

# Variable b = 1.59 is a float
b = 1.59
print(b)

# Variable c is a String
c = "apples"
print(c)

# Multiple Assignment
puppy, monkey, baby = "puppy", "monkey", "baby"
print(puppy)
print(monkey)
print(baby)

puppy = monkey = baby = "puppy monkey baby"
print(puppy)
print(monkey)
print(baby)


# Error Can't mismatch Data Types
#print ("I am a string" + 42)

# Convert Data Type int 42 to string 42
print("I am a string " + str(42))

# Global vs. Local variables
local = 0
glob = 0

def local_function():
    global glob
    glob = "    I am Global"
    local = "I am Local"
    print(glob)
    print(local)

local_function()

# Global changes while local does not
print(local)
print(glob)

#Delete glob variable
del glob
#print(glob)