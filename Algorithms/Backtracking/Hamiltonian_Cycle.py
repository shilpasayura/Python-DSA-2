def is_safe(graph, vertex, pos, paths):

    # Check if the current vertex and last vertex int the path are adjacent
    # Check if the current vertex already not in the paths
    if graph[paths[pos-1]][vertex] == 1 and vertex not in paths:
        return True
    return False


def hamitonian(graph, pos, paths):
    if pos == len(graph):
        if graph[paths[pos-1]][paths[0]] == 1:
            return True
        return False
    for vertex in range(1, len(graph)):
        if is_safe(graph, vertex, pos, paths):
            paths[pos] = vertex
            if hamitonian(graph, pos+1, paths):
                return True

            paths[pos] = -1

    return False


graph = [[0, 1, 0, 1, 0],
         [1, 0, 1, 1, 1],
         [0, 1, 0, 0, 1],
         [1, 1, 0, 0, 1],
         [0, 1, 1, 1, 0]]

paths = [-1, -1, -1, -1, -1]
paths[0] = 0
print hamitonian(graph, 1, paths)
print paths

graph1 = [ [0, 1, 0, 1, 0], [1, 0, 1, 1, 1],
           [0, 1, 0, 0, 1,], [1, 1, 0, 0, 0],
           [0, 1, 1, 0, 0] ]

paths = [-1, -1, -1, -1, -1]
paths[0] = 0
print hamitonian(graph1, 1, paths)
print paths
