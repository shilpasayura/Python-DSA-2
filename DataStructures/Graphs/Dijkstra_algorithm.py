import sys
import heapq


class Edge(object):
    def __init__(self, weight, from_vertex, to_vertex):
        self.weight = weight
        self.from_vertex = from_vertex
        self.to_vertex = to_vertex


class Node(object):
    def __init__(self, name):
        self.name = name
        self.visited = False
        self.predecessor = None
        self.adjacency_list = list()
        self.min_distance = sys.maxsize

    def __cmp__(self, other_vertex):
        return cmp(self.min_distance, other_vertex.min_distance)

    def __lt__(self, other_vertex):
        return self.min_distance < other_vertex.min_distance


class DijkstraAlgorithm(object):

    def calculate_shortest_path(self, starting_node):
        heap = list()
        starting_node.min_distance = 0
        heapq.heappush(heap, starting_node)

        while heap:
            current_vertex = heapq.heappop(heap)
            for edge in current_vertex.adjacency_list:
                u = edge.from_vertex
                v = edge.to_vertex
                new_distance = u.min_distance + edge.weight

                if new_distance < v.min_distance:
                    v.predecessor = u
                    v.min_distance = new_distance
                    heapq.heappush(heap, v)

    def get_shortest_path(self, target_vertex):
        print("Shortest path to vertex is: %s" % target_vertex.min_distance)

        node = target_vertex

        while node is not None:
            print("%s " % node.name)
            node = node.predecessor


node1 = Node('A')
node2 = Node('B')
node3 = Node('C')
node4 = Node('D')
node5 = Node('E')
node6 = Node('F')
node7 = Node('G')
node8 = Node('H')

edge1 = Edge(5, node1, node2)
edge2 = Edge(8, node1, node8)
edge3 = Edge(9, node1, node5)
edge4 = Edge(15, node2, node4)
edge5 = Edge(12, node2, node3)
edge6 = Edge(4, node2, node8)
edge7 = Edge(7, node8, node3)
edge8 = Edge(6, node8, node6)
edge9 = Edge(5, node5, node8)
edge10 = Edge(4, node5, node6)
edge11 = Edge(20, node5, node7)
edge12 = Edge(1, node6, node3)
edge13 = Edge(13, node6, node7)
edge14 = Edge(3, node3, node4)
edge15 = Edge(11, node3, node7)
edge16 = Edge(9, node4, node7)

node1.adjacency_list.extend([edge1, edge2, edge3])
node2.adjacency_list.extend([edge4, edge5, edge6])
node3.adjacency_list.extend([edge14, edge15])
node4.adjacency_list.extend([edge16])
node5.adjacency_list.extend([edge9, edge10, edge11])
node6.adjacency_list.extend([edge12, edge13])
node8.adjacency_list.extend([edge7, edge8])

shortest_path = DijkstraAlgorithm()
shortest_path.calculate_shortest_path(node1)
shortest_path.get_shortest_path(node7)




