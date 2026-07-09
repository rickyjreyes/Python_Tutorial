# 15_exceptions.py
#
# Exceptions are errors that happen while a program is running.
# try/except lets your program handle expected problems gracefully.


def divide_numbers(first_number, second_number):
    try:
        result = first_number / second_number
        print(first_number, "divided by", second_number, "=", result)
    except ZeroDivisionError:
        print("You cannot divide by zero.")


divide_numbers(10, 2)
divide_numbers(10, 0)

text_number = "42"

try:
    converted_number = int(text_number)
    print("Converted number:", converted_number)
except ValueError:
    print("That text cannot be converted to an integer.")

bad_number = "forty-two"

try:
    converted_number = int(bad_number)
    print("Converted number:", converted_number)
except ValueError:
    print("'forty-two' cannot be converted to an integer.")
