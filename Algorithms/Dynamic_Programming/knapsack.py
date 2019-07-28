# Problem Statement
# Knapsack Problem

W = int(raw_input())
val = map(int, raw_input().split())
weights = map(int, raw_input().split())
n = len(weights)


def knapsack(W, i):
    if W == 0 or i >= len(val):
        return 0
    elif weights[i] > W:
        return knapsack(W, i+1)
    else:
        return max(val[i] + knapsack(W-weights[i], i+1), knapsack(W, i+1))


def dp_knapsack(W, n):
    K = [[0 for x in range(W+1)] for x in range(n+1)]
    for i in range(n+1):
        for j in range(W+1):
            if j == 0 or i == 0:
                K[i][j] = 0
            elif weights[i-1] > W:
                K[i][j] = K[i-1][j]
            else:
                K[i][j] = max(val[i-1] + K[i-1][j-weights[i-1]], K[i-1][j])

    return K[n][W]



print knapsack(W, 0)
print dp_knapsack(W, n)