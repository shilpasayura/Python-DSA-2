# Program: Binary Search
def binary_search_iterative(arr, element):
    first = 0
    last = len(arr)-1
    while first <= last:
        mid = (first + last)/2
        if arr[mid] == element:
            return True
        else:
            if arr[mid] < element:
                first = mid + 1
            else:
                last = mid - 1
    return False


def binary_search_recursive(arr, element):
    if len(arr) == 0:
        return False
    else:
        mid = len(arr)/2
        if arr[mid] == element:
            return True
        else:
            if arr[mid] < element:
                return binary_search_recursive(arr[mid+1:], element)
            else:
                return binary_search_recursive(arr[:mid], element)


arr = [1,2,3,4,6,7]
print binary_search_iterative(arr, 6)
print binary_search_recursive(arr, 10)