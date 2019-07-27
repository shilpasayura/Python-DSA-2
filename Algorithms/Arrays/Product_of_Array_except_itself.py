# Given an array of integers, construct a product array such that
# prod[i] is equal to the product of all elements except itself
# Solving this without division operator


arr = map(int, raw_input().split())


def product_array(arr):

    # Create an empty output list
    output = [None] * len(arr)

    product = 1
    i = 0

    # Forward pass
    while i < len(arr):
        output[i] = product
        product = product * arr[i]
        i = i+1

    product = 1
    i = len(arr) - 1

    # Backward pass
    while i >= 0:
        output[i] = output[i] * product
        product = product * arr[i]
        i = i-1

    return output


print product_array(arr)