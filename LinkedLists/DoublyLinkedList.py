class DoublyLinkedBase(object):
    """ This is another type of implementation of Doulbly Linked Lists.
    We create sentinels to avoid methods od insert_after, insert_at_beginning, insert_at_end
    insert_between() works for all type of insert operations as we are creating dummy sentinals
    which makes creation always happens between the two nodes"""
    class _Node(object):
        def __init__(self, data, prev, next):
            self.data = data
            self.prev = prev
            self.next = next

    def __init__(self):
        self.header = self._Node(None, None, None)
        self.trailer = self._Node(None, None, None)
        self.header.next = self.trailer
        self.trailer.prev = self.header
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def insert_between(self, data, predecessor, successor):
        new_node = self._Node(data, predecessor, successor)
        predecessor.next = new_node
        successor.prev = new_node
        self.size += 1
        return new_node

    def delete_node(self, node):
        successor = node.next
        predecessor = node.prev
        predecessor.next = successor
        successor.prev = predecessor
        self.size -= 1
        element = node.data
        node.data = node.prev = node.next = None
        return element

    def print_list(self):
        current = self.header.next
        while current != self.trailer:
            print "%s -> " % current.data,
            current = current.next


class DoublyLinkedList(object):
    class _Node(object):
        def __init__(self, data, prev, next):
            self.data = data
            self.prev = prev
            self.next = next

    def __init__(self):
        self.size = 0
        self.head = None

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def get_node(self, data):
        if self.head is None:
            print("List is empty")
            return
        current = self.head
        item = None
        while current is not None:
            if current.data == data:
                item = current
                break
            current = current.next
        return item

    def insert_at_beginning(self, data):
        new_node = self._Node(data, None, None)
        print("Adding %s at the beginning" % data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.size += 1

    def insert_at_end(self, data):
        new_node = self._Node(data, None, None)
        print("Adding %s at the end" % data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            new_node.prev = temp
            temp.next = new_node

        self.size += 1

    def insert_after(self, data, value):
        predecessor = self.get_node(value)
        if predecessor is None:
            print("No insertion happened")
            return
        new_node = self._Node(data, None, None)
        new_node.next = predecessor.next
        predecessor.next = new_node
        new_node.prev = predecessor
        if new_node.next is not None:
            new_node.next.prev = new_node
        self.size += 1

    def insert_before(self, data, value):
        successor = self.get_node(value)
        if successor is None:
            print("No insertion happened")
            return
        new_node = self._Node(data, None, None)
        new_node.next = successor
        new_node.prev = successor.prev
        if new_node.prev is not None:
            new_node.prev.next = new_node
        new_node.prev = new_node
        self.size += 1

    def delete_node(self, data):
        node = self.get_node(data)
        if node is None or self.head is None:
            print("node returned none")
            return
        if self.head == node:
            print("Deleting %s from the beginning" % data)
            self.head = node.next
        elif node.next is None and node.prev:
            print("Deleting %s from the end" % data)
            node.prev.next = None
            print "node.data", node.prev.data
        elif node.next is not None and node.prev is not None:
            print("Deleting %s from the middle" % data)
            node.prev.next = node.next
        self.size -= 1

    def print_list(self):
        current = self.head
        while current is not None:
            print "%s -> " % current.data,
            current = current.next

    def reverse_print(self):
        pass


d = DoublyLinkedList()

d.insert_at_end(10)
d.insert_at_end(20)
d.insert_at_end(30)
d.insert_at_end(120)
d.insert_at_end(150)
d.insert_at_end(160)
d.insert_after(40, 30)
print d.size
d.print_list()
d.insert_before(99, 30)
d.print_list()
d.delete_node(40)
print d.size
print d.get_node(99).data
d.print_list()
d.delete_node(30)
# print d.get_node(99).data
print d.size
d.print_list()
# print d.get_node(99).data
d.delete_node(99)
d.print_list()
