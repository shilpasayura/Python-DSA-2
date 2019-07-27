# Program: Give an array of integers (both positive and negative)
# find the largest continuous sum


def large_cont_sum(arr):
    # Handle edge case
    if len(arr) == 0:
        return 0

    if len(arr) == 1:
        return len(arr[0])

    largest_sum = 0
    current_sum = 0
    start_index = 0
    end_index = 0
    for i in range(1, len(arr)):
        if current_sum + arr[i] < 0:
            current_sum = 0
            start_index = i+1
        else:
            current_sum = current_sum + arr[i]
            largest_sum = max(current_sum, largest_sum)
            end_index = i

    print start_index
    print end_index
    return largest_sum


arr = map(int, raw_input().split())
print large_cont_sum(arr)