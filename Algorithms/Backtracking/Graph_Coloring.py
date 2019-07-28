# Graph coloring problem


def is_safe(graph, vertex, color, c):

    # Checking if the color is same in the adjacent nodes
    for i in range(len(graph)):
        if graph[vertex][i] == 1 and color[i] == c:
            return False

    return True


def color_graph(graph, m, vertex, color):
    # Return True if all the vertices are done
    if vertex >= len(graph):
        return True

    # Loop over all the colors to see which color we can apply
    for c in m:

        # Check if we can apply the color, if not outer for loop applies another color
        if is_safe(graph, vertex, color, c):
            color[vertex] = c

            # If the before one is safe to apply, then check for the next vertex
            if color_graph(graph, m, vertex+1, color):
                return True

            # If the above one is not safe, set that color to zero and apply another color
            # using outer for loop
            color[vertex] = 0
    return False


# Graph is taken in 2D matrix. 1 represents an edge between two nodes.
# first item represents first node adjacency list
graph = [[0,1,1,1], [1,0,1,0], [1,1,0,1], [1,0,1,0]]

# Initialize the color list to all zeros so that we will update in the main function
color = [0,0,0,0]
m = ['R', 'B', 'G']
print color_graph(graph, m, 0, color)
print color