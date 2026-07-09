# 02_insertion_sort.py
#
# Insertion sort builds a sorted section one value at a time.
# It is simple and works well for small or nearly sorted lists.


def insertion_sort(values):
    numbers = values.copy()

    for index in range(1, len(numbers)):
        current_value = numbers[index]
        position = index - 1

        while position >= 0 and numbers[position] > current_value:
            numbers[position + 1] = numbers[position]
            position -= 1

        numbers[position + 1] = current_value

    return numbers


scores = [9, 4, 7, 1, 5, 3]
print("Original:", scores)
print("Sorted:", insertion_sort(scores))
print("Original unchanged:", scores)
