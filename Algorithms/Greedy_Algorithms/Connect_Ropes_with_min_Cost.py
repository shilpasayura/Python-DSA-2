# Given n ropes of different length, program to connect these ropes
# into one rope with min cost. cost is sum of two ropes lengths
import heapq


def min_cost(ropes):
    # Set the total cost to 0
    total_cost = 0

    # Build a min heap to get the minimum element
    heapq.heapify(ropes)

    # Loop till heap is reduced to 1 item.
    # Calculate the cost and push that to heap
    while len(ropes) > 1:
        current_cost = heapq.heappop(ropes)+ heapq.heappop(ropes)
        total_cost += current_cost
        heapq.heappush(ropes, current_cost)

    return total_cost


ropes = map(int, raw_input().split())

print min_cost(ropes)