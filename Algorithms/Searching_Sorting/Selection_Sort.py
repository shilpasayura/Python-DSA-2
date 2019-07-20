# Program: Selection sort
# In every iteration, the minimum element from the unsorted subarray
# is picked and moved to the sorted subarray

arr = map(int, raw_input().split())


def selection_sort(arr):
    for i in range(len(arr)-1):
        min_i = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_i]:
                min_i = j

        if min_i != i:
            arr[i], arr[min_i] = arr[min_i], arr[i]

    return arr


print selection_sort(arr)
