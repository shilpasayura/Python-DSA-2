# Program: Fractional Knapsack problem

class Item(object):
    def __init__(self, weight, value, index):
        self.weight = weight
        self.value = value
        self.index = index
        self.cost = self.value // self.weight

    def __lt__(self, other):
        return self.cost < other.cost


def fractional_knapsack(weights, values, capacity):
    # Sort the array using
    fractions = list()
    for i in range(len(weights)):
        fractions.append(Item(weights[i], values[i], i))

    # Sorting items by fraction
    fractions.sort(reverse=True)

    print [fraction.cost for fraction in fractions]

    # Set the initial value of total value to 0
    total_value = 0

    # Add item into bag untill we can't add the next item
    # as the capacity is less than the weight of the bag
    for fraction in fractions:
        current_weight = fraction.weight
        current_value = fraction.value
        if capacity - current_weight >= 0:
            total_value = total_value + current_value
            capacity = capacity - current_weight
        else:
            # Adding the fractions to the total value
            total_value += current_value * capacity / current_weight
            break
    return total_value


weights = map(int, raw_input().split())
values = map(int, raw_input().split())
capacity = int(raw_input())

print fractional_knapsack(weights, values, capacity)
