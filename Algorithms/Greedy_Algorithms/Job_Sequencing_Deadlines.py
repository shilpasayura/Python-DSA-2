# Given an array of jobs with deadlines and profits
# Maximize the total profit by doing that job in single unit of time


def max_profit(jobs):

    # Sort the array using the profits in decreasing order
    jobs = sorted(jobs, key=lambda x: x[2], reverse=True)

    # Get the maximum deadline
    max_deadline = max(jobs, key=lambda x:x[1])[1]

    # Create an array of lenght max deadline to keep track of the slots
    result = [None] * max_deadline

    total_profit = 0

    # Iterate through all jobs.
    for job in jobs:
        # iterate through the slots from the last possible. if not check the previous one
        for j in range(job[1]-1, -1, -1):
            if result[j] is None:
                result[j] = job[0]
                total_profit += job[2]
                break

    print ' '.join(result)
    print total_profit


jobs = [['a', 3, 35],
       ['b', 4, 30],
       ['c', 4, 25],
       ['d', 2, 20],
       ['e', 3, 15],
       ['f', 1, 12],
       ['g', 2, 5]]

max_profit(jobs)