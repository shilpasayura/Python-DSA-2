# Problem Statement
# House robber problem


houses = map(int, raw_input().split())


def rob_house(houses, index):
    if index >= len(houses):
        return 0
    else:
        return max(houses[index] + rob_house(houses, index+2), rob_house(houses, index+1))


print rob_house(houses, 0)


def dp_rob(houses, n):
    if n == 0:
        return 0
    if n == 1:
        return houses[0]
    if n == 2:
        return max(houses[0], houses[1])

    dp = [0] * n
    dp[0] = houses[0]
    dp[1] = max(houses[0], houses[1])

    for i in range(2, n):
        dp[i] = max(houses[i] + dp[i-2], dp[i-1])

    return dp[n-1]


print dp_rob(houses, len(houses))