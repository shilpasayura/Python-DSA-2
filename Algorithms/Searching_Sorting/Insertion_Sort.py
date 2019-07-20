# Program: Insertion sort
# In every iteration, Each new item is inserted back in to the
# previous sublist such that the sorted sublist is one item larger

arr = map(int, raw_input().split())


def insertion_sort(arr):
    for i in range(len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

    return arr


print insertion_sort(arr)