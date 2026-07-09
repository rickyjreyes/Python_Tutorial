# 04_quick_sort.py
#
# Quick sort also uses divide and conquer.
# It chooses a pivot, places smaller values before it, and larger values after it.


def quick_sort(values):
    if len(values) <= 1:
        return values.copy()

    pivot = values[len(values) // 2]
    smaller = []
    equal = []
    larger = []

    for value in values:
        if value < pivot:
            smaller.append(value)
        elif value > pivot:
            larger.append(value)
        else:
            equal.append(value)

    return quick_sort(smaller) + equal + quick_sort(larger)


scores = [9, 4, 7, 1, 5, 3]
print("Original:", scores)
print("Sorted:", quick_sort(scores))
