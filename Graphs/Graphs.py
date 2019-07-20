class Vertex(object):
    def __init__(self, name):
        self.name = name
        self.adjacencyList = dict()

    def add_neighbour(self, name, weight=0):
        self.adjacencyList[name] = weight

    def get_connections(self):
        return self.adjacencyList.keys()

    def get_name(self):
        return self.name

    def get_weight(self, name):
        return self.adjacencyList[name]

    def __str__(self):
        return self.name + ' connected to ' + str([node.name for node in self.adjacencyList])


class Graph(object):
    def __init__(self):
        self.vertList = dict()
        self.numofVertices = 0

    def add_vertex(self, name):
        self.numofVertices += 1
        new_vertix = Vertex(name)
        self.vertList[name] = new_vertix
        return new_vertix

    def get_vertex(self, name):
        if name in self.vertList:
            return self.vertList[name]
        else:
            return None

    def add_edge(self, fromvert, tovert):
        if fromvert not in self.vertList:
            new_vertex = self.add_vertex(fromvert)
        if tovert not in self.vertList:
            new_vertex = self.add_vertex(fromvert)
        self.vertList[fromvert].add_neighbour(self.vertList[tovert])

    def get_vertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())

    def __contains__(self, item):
        return item in self.vertList


graph = Graph()

for i in 'ABCDEF':
    graph.add_vertex(i)

graph.add_edge('A', 'B')
graph.add_edge('A', 'C')
graph.add_edge('A', 'F')
graph.add_edge('B', 'D')
graph.add_edge('C', 'E')
graph.add_edge('E', 'D')
graph.add_edge('F', 'D')
graph.add_edge('F', 'E')


for vertex in graph:
    print vertex

print graph.get_vertices()