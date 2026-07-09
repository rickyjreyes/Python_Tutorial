# 06_loops.py
#
# Loops repeat code while a condition is true or for every item in a sequence.

count = 0

if count < 9:
    print("Hello, I am an if statement and count is", count)

while count < 10:
    print("Hello, I am a while loop and count is", count)
    count += 1

loop_condition = True

while loop_condition:
    print("I am a loop")
    loop_condition = False

# For loops are useful when you already have a collection.
for number in range(3):
    print("For loop number:", number)
