# Problem Statement
# Cutting Rod DP problem

prices = map(int, raw_input().split())


def cutting(prices):
    n = len(prices)
    result = [0] * (n+1)
    result[0] = 0
    for i in range(1, n+1):
        max_value = -1
        for j in range(1, i+1):
            temp = prices[j-1] + result[i-j]
            if temp > max_value:
                max_value = temp

        result[i] = max_value
    return result[n]


print cutting(prices)
