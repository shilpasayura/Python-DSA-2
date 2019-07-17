# Program: Merge sort
# Divide and conquer algorithm

arr = map(int, raw_input().split())


def merge_sort(arr):

    if len(arr) == 1:
        return

    mid = len(arr)/2

    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left)
    merge_sort(right)

    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[j] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


print("Before Sorting")
print(arr)
merge_sort(arr)
print("After Sorting")
print(arr)
