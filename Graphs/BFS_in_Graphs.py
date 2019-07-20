class Node(object):
    def __init__(self, name):
        self.name = name
        self.adjacencyList = list()
        self.visited = None


class BreadthFirstSearch(object):
    def bfs(self, starting_node):
        queue = list()
        queue.append(starting_node)
        starting_node.visited = True
        while queue:
            node = queue.pop(0)
            print("%s" % node.name)
            for n in node.adjacencyList:
                if not n.visited:
                    n.visited = True
                    queue.append(n)


node1 = Node('A')
node2 = Node('B')
node3 = Node('C')
node4 = Node('D')
node5 = Node('E')

node1.adjacencyList.append(node2)
node1.adjacencyList.append(node3)
node2.adjacencyList.append(node4)
node4.adjacencyList.append(node5)

bfs = BreadthFirstSearch()
bfs.bfs(node1)