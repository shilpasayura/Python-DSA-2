# Program: Activity Selection
# Given start and end times, Select the maximum number of activites
# that can be performed by a single person


def get_max_activies(start, finish):
    # We need to sort the activities according to their finish times
    # For that, we will get the indexed sorted
    sorted_indices = sorted(dict(enumerate(finish)).items(), key=lambda x: x[1])
    sorted_indices = [index[0] for index in sorted_indices]

    # Selecting the first activity
    i = sorted_indices[0]
    print i,

    # Looping over the activities and checking if the start time is greater
    # than or eqaul to the finish time of previous activity
    for j in sorted_indices:
        if start[j] >= finish[i]:
            print j,
            i = j


start = map(int, raw_input().split())
finish = map(int, raw_input().split())
get_max_activies(start, finish)
