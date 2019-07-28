# Problem Statement
# You can climb 1 or 2 stairs with 1 step. How many different ways can you climb n stairs?

n = int(raw_input())


def climb(n):
    steps = [0] * (n+1)
    steps[1] = 1
    steps[2] = 2
    for i in range(3, n+1):
        steps[i] = steps[i-1] + steps[i-2]

    return steps[n]


print climb(n)