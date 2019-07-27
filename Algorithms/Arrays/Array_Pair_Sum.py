# Program: Given an integer array, output all the unique pairs
# that sum up to a specific value k


def array_pair_sum(arr, k):

    # Handle edge case
    if len(arr) < 2:
        return

    seen = set()
    output = set()

    # Loop over each item, get the target and see if it is present in seen,
    # if yes, add that to output set else add that to seen set
    for num in arr:
        target = k-num
        if target not in seen:
            seen.add(num)
        else:
            # To get unique sets, we need to maintain the order
            output.add(( min(num, target), max(num, target)))

    print ','.join(map(str, list(output)))


arr = map(int, raw_input().split())
k = int(raw_input())
array_pair_sum(arr, k)