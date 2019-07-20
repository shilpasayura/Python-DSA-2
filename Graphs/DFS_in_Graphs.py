class Node(object):
    def __init__(self, name):
        self.name = name
        self.adjacencyList = list()
        self.visited = None


class DepthFirstSearch(object):
    def dfs(self, starting_node):
        print("%s" % starting_node.name)
        starting_node.visited = True
        for node in starting_node.adjacencyList:
            if not node.visited:
                self.dfs(node)

    def dfs_using_Stack(self, starting_node):
        stack = list()
        stack.append(starting_node)
        while stack:
            node = stack.pop()
            print("%s" % node.name)
            for n in node.adjacencyList:
                if not n.visited:
                    n.visited = True
                    stack.append(n)


node1 = Node('A')
node2 = Node('B')
node3 = Node('C')
node4 = Node('D')
node5 = Node('E')

node1.adjacencyList.append(node2)
node1.adjacencyList.append(node3)
node2.adjacencyList.append(node4)
node4.adjacencyList.append(node5)

dfs = DepthFirstSearch()
dfs.dfs(node1)