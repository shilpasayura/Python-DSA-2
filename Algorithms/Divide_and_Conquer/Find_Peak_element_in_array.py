# Finding a peak element in an array


def find_peak(arr, low, high, n):
    mid = int((low + high) / 2)
    if (mid == 0 or arr[mid-1] <= arr[mid]) and\
        (mid == n-1 or arr[mid+1] <= arr[mid]):
        return mid

    elif mid > 0 and arr[mid-1] > arr[mid]:
        return find_peak(arr, low, mid-1, n)
    elif mid > 0 and arr[mid+1] > arr[mid]:
        return find_peak(arr, mid+1, high, n)


arr = map(int, raw_input().split())

print "Index of the peak position is %s" % find_peak(arr, 0, len(arr)-1, len(arr))