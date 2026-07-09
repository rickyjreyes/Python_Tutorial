# 05_conditionals.py
#
# Conditionals let a program make decisions.

print(3 == 4)

if True:
    print("True")
else:
    print("False")

if 100 == (2 * 50):
    print("100 equals 2 * 50")

if 19 <= 19:
    print("19 is less than or equal to 19")

if -50 >= 15:
    print("This will not print")
else:
    print("-50 is not greater than or equal to 15")

if 12 != 12:
    print("This will not print")
else:
    print("12 equals 12")

food = "Burger"

if food == "Burger":
    print("Burgers are sooooo good!")
elif food == "Pizza":
    print("Pizza is good too.")
else:
    print("Try something new.")
