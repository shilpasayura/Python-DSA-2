# Program: Quick sort
# Divide and conquer algorithm
# It picks an element as pivot and partitions the given array around the picked pivot

arr = map(int, raw_input().split())


def partition(arr, start, end):
    pivot = arr[end]
    pindex = start

    for i in range(start, end):
        if arr[i] <= pivot:
            arr[i], arr[pindex] = arr[pindex], arr[i]
            pindex += 1

    arr[pindex], arr[end] = arr[end], arr[pindex]
    return pindex


def quick_sort(arr, start, end):
    if start < end:
        pivot = partition(arr, start, end)
        quick_sort(arr, start, pivot-1)
        quick_sort(arr, pivot+1, end)


quick_sort(arr, 0, len(arr)-1)
print arr