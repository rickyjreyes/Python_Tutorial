# 03_merge_sort.py
#
# Merge sort uses divide and conquer:
# 1. Split the list into smaller lists.
# 2. Sort each smaller list.
# 3. Merge the sorted lists back together.


def merge(left, right):
    result = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result.extend(left[left_index:])
    result.extend(right[right_index:])
    return result


def merge_sort(values):
    if len(values) <= 1:
        return values.copy()

    middle = len(values) // 2
    left = merge_sort(values[:middle])
    right = merge_sort(values[middle:])

    return merge(left, right)


scores = [9, 4, 7, 1, 5, 3]
print("Original:", scores)
print("Sorted:", merge_sort(scores))
