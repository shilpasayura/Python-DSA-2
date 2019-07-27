# Program for getting the Maximum profit possible from
# the purchase and sale of single share on the same day


price_ranges = map(int, raw_input().split())


def profit(price_ranges):

    # Check the length
    if len(price_ranges) < 2:
        print("At least 2 stock prices should be present")
        return

    # Start the minimum marker ar first price
    min_price = price_ranges[0]

    # Start off with a value 0
    max_profit = 0

    for i in range(0, len(price_ranges)):
        # Check the current price against min price
        current_profit = price_ranges[i] - min_price

        # compare max price against current profit
        max_profit = max(max_profit, current_profit)

        # Check to set the lowest stock price so far
        min_price = min(price_ranges[i], min_price)

    return max_profit


print profit(price_ranges)
