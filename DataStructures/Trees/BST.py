import sys


class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST(object):
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(self.root, data)

    # O(logN) - If the tree is balanced
    def _insert(self, node, data):
        if data < node.data:
            if node.left is not None:
                self._insert(node.left, data)
            else:
                node.left = Node(data)
        else:
            if node.right is not None:
                self._insert(node.right, data)
            else:
                node.right = Node(data)

    def get_min(self):
        if self.root:
            return self._get_min(self.root)
        else:
            print("Tree is Empty")

    def _get_min(self, node):
        if node.left:
            return self._get_min(node.left)
        return node.data

    def get_max(self):
        if self.root:
            return self._get_max(self.root)

    def _get_max(self, node):
        if node.right:
            return self._get_max(node.right)
        return node.data

    def remove(self, data):
        if self.root:
            self.root = self._remove(data, self.root)

    def _remove(self, data, node):
        if not node:
            return node
        if data < node.data:
            node.left = self._remove(data, node.left)
        elif data > node.data:
            node.right = self._remove(data, node.right)
        else:
            if not node.left and node.right:
                print("Removing %s Leaf node" % data)
                del node
                return None
            if not node.left:
                print("Removing node %s which has single right child" % data)
                temp = node.right
                del node
                return temp
            elif not node.right:
                print("Removing node %s which has single left child" % data)
                temp = node.left
                del node
                return temp
            print("Removing node %s which has both left and right children" % data)
            temp = self.get_predecessor(node.left)
            node.data = temp.data
            node.left = self._remove(temp.data, node.left)

        return node

    def get_predecessor(self, node):
        if node.right:
            return self.get_predecessor(node.right)
        return node

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print "%s -> " % node.data,
            self.inorder(node.right)

    def preorder(self, node):
        if node:
            print "%s -> " % node.data,
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):
        if node:
            self.preorder(node.left)
            self.preorder(node.right)
            print "%s -> " % node.data,

    def is_BST(self):
        return self._is_BST(self.root, -sys.maxint-1, sys.maxint)

    def _is_BST(self, node, min, max):
        if not node:
            return True
        if min < node.data < max and \
                self._is_BST(node.left, min, node.data) and \
                self._is_BST(node.right, node.data, max):
            return True
        else:
            return False

    def level_order(self):
        queue = list()
        queue.append(self.root)
        while queue:
            current = queue[0]
            print "%s ->" % current.data,
            if current.left is not None:
                queue.append(current.left)
            if current.right is not None:
                queue.append(current.right)
            queue.pop(0)

    def trim_BST(self, node, min_value, max_value):
        """This method is to trim the BST such that values are in range of
        min and max values and the resulting tree is still BST"""
        if not node:
            return
        node.left = self.trim_BST(node.left, min_value, max_value)
        node.right = self.trim_BST(node.right, min_value, max_value)
        if min_value <= node.data <= max_value:
            return node
        elif node.data > max_value:
            return node.left
        elif node.data < min_value:
            return node.right


bst = BST()
bst.insert(10)
bst.insert(5)
bst.insert(8)
bst.insert(20)
bst.insert(30)
bst.insert(7)
bst.insert(1)
bst.insert(40)
bst.insert(90)
bst.inorder(bst.root)
bst.remove(10)
bst.inorder(bst.root)
print bst.is_BST()
print bst.level_order()
bst.trim_BST(bst.root, 8, 40)
bst.inorder(bst.root)