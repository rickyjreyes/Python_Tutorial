# 05_radix_sort.py
#
# Radix sort sorts non-negative integers one digit place at a time.
# This version uses base 10 buckets.


def radix_sort(values):
    if not values:
        return []

    if any(value < 0 for value in values):
        raise ValueError("This beginner radix sort only supports non-negative integers.")

    numbers = values.copy()
    max_value = max(numbers)
    place = 1

    while max_value // place > 0:
        buckets = [[] for _ in range(10)]

        for number in numbers:
            digit = (number // place) % 10
            buckets[digit].append(number)

        numbers = []
        for bucket in buckets:
            numbers.extend(bucket)

        place *= 10

    return numbers


scores = [170, 45, 75, 90, 802, 24, 2, 66]
print("Original:", scores)
print("Sorted:", radix_sort(scores))
