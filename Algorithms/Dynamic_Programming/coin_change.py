# Coin change problem


def count(coins, num_of_coins, change):
    if change == 0:
        return 1

    if num_of_coins <= 0 and change >= 1:
        return 0

    if change < 0:
        return 0

    return count(coins, num_of_coins-1, change) + count(coins, num_of_coins, change-coins[num_of_coins-1])

def dp_coin_change(coins, num_of_coins, change):
    table = [[0 for _ in range(change+1)] for _ in range(num_of_coins+1)]

    for i in range(num_of_coins+1):
        for j in range(change+1):
            if i == 0 and j == 0:
                table[i][j] = 1
            elif i > j:
                table[i][j] = table[i-1][j]
            else:
                table[i][j] = table[i-1][j] + table[i][j-i]

    print table

    return table[num_of_coins][change]


coins = [1,2,3,4]
change = 7
print count(coins, len(coins), change)
print dp_coin_change(coins, len(coins), change)