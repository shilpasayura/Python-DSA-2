# Program to minimize the cashflow among all friends who have to take
# or give some amount of money from another


def get_max(arr):
    # Return the index of maximum element
    max_index = 0
    for i in range(len(arr)):
        if arr[i] > arr[max_index]:
            max_index = i
    return max_index


def get_min(arr):
    # Returns the indes of minimum element
    min_index = 0
    for i in range(len(arr)):
        if arr[i] < arr[min_index]:
            min_index = i
    return min_index


def settle_amount(net_amounts):
    max_taken = get_min(net_amounts)
    max_given = get_max(net_amounts)

    if net_amounts[max_taken] == 0 and net_amounts[max_given] == 0:
        return 0

    # Calculate the amount to be transferred as the min amount of max taken and max given
    amount_to_be_given = min(-net_amounts[max_taken], net_amounts[max_given])

    print "Person %s pays %s person %s" % (max_taken, amount_to_be_given, max_given)

    # Update the amounts after transfer
    net_amounts[max_taken] += amount_to_be_given
    net_amounts[max_given] -= amount_to_be_given

    # Call recursively untill the values becomes zero
    settle_amount(net_amounts)


def min_cash_flow(amounts):
    # Create a list of net amount to be paid for each person
    no_of_persons = len(amounts)
    net_amounts = [0 for i in range(no_of_persons)]

    for i in range(no_of_persons):
        for j in range(no_of_persons):
            net_amounts[i] += amounts[j][i] - amounts[i][j]

    print net_amounts

    settle_amount(net_amounts)


# Input is taken in 2D matrix where each row corresponds to the amount
# indicating that person needs to pay to the other person
amounts = [[0, 100, 0, 200],
           [0, 0, 0, 100],
           [300, 0, 0, 0],
           [0, 0, 150, 0]]

# The above matrix indicates that, person 0 has to give 100rs to person 2, 200rs to person 3.
# person 2 has to give 500rs to person 3 and person 3 is no need to give to anyone

min_cash_flow(amounts)
