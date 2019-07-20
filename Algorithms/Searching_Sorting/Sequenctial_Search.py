# Program: Sequential search
def sequential_search(arr, ele):
    pos = 0
    while pos < len(arr):
        if arr[pos] == ele:
            return True
        else:
            pos += 1
    return False


# If the sequence is ordered. We can stop when we encounter a large item
def sorted_seq_search(arr, ele):
    pos = 0

    while pos < len(arr):
        if arr[pos] == ele:
            return True
        else:
            if arr[pos] > ele:
                return False
            else:
                pos += 1
    return False


arr = [1,2,3,4,6]
print sequential_search(arr, 6)
print sorted_seq_search(arr, 1)
