# Program: Bubble sort
# Compare item with its adjacent item.
# In every iteration, the larger item will move to the end

arr = map(int, raw_input().split())


def bubble_sort(arr):
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

    return arr


print bubble_sort(arr)