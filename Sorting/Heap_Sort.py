def heapify(arr, n, index):
    largest = index
    left = 2*index+1
    right = 2*index+2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != index:
        arr[index], arr[largest] = arr[largest], arr[index]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    # Building max heap from the elements
    for i in range(n, -1, -1):
        heapify(arr, n, i)

    # Sorting
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


arr = [12, 11, 13, 5, 6, 7]
heap_sort(arr)
print "After Sorting"
print arr
