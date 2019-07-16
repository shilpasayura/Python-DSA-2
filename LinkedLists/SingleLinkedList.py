# LinkedList implementation


class LinkedList(object):
    class _Node(object):
        def __init__(self, next=None, data=None):
            self.next = next
            self.data = data

    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def add_node(self, data, pos):
        """ Adds the node at given position to the linked list"""
        new_node = self._Node(None, data)
        # Check if the list is empty
        if self.head is None:
            print("List is empty.")
            self.head = new_node
        # Check for the beginning of list
        elif pos == 0:
            print("Adding %s in the beginning" % data)
            new_node.next = self.head
            self.head = new_node
        # Check for the ending
        elif pos == self.size:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            print("Adding %s in the last" % data)
            temp.next = new_node
        else:
            i = 0
            current = self.head
            while i != pos-1:
                if current.next is None:
                    print("Not enough elements. Please insert between 1 and %s" %  self.size)
                    return
                current = current.next
                i += 1
            print("Adding %s in the middle" % data)
            temp = current.next
            current.next = new_node
            new_node.next = temp

        self.size += 1

    def delete_node(self, data):
        """ Deletes the node after searching the data"""
        current = self.head
        if data == current.data:
            print("Deleting %s from the beginning" % data)
            self.head = current.next
            current.next = None
            self.size -= 1
        else:
            pos = 1
            while current.next is not None:
                if data == current.next.data:
                    print("Deleting %s from the position %s" % (data, pos))
                    temp = current.next
                    current.next = temp.next
                    self.size -= 1
                    break
                current = current.next
                pos += 1
            else:
                print("Not found in the list")

    def print_list(self):
        """ Prints the linked list"""
        current = self.head
        while current is not None:
            print "%s -> " % current.data,
            current = current.next

    def search(self, data):
        """ Searches the element with the given data """
        current = self.head
        pos = 1
        while current is not None:
            if current.data == data:
                print "Found at %s" % pos
                break
            current = current.next
            pos += 1
        else:
            print "%s is not found in the list" % pos

    def reverse_list(self):
        """ Reverses the list in iterative manner """
        current = self.head
        prev = None
        after = None
        while current is not None:
            after = current.next
            current.next = prev
            prev = current
            current = after
        self.head = prev

    def recursion_reverse(self, node):
        """ Reverses the list in recursive manner """
        if node.next is None:
            self.head = node
            return
        self.recursion_reverse(node.next)
        node.next.next = node
        node.next = None


list = LinkedList()
list.add_node(2, 0)
list.add_node(3, 1)
list.add_node(4, 2)
list.add_node(5, 1)
list.add_node(10, 0)
list.add_node(24, 3)
list.delete_node(5)
list.add_node(60, 13)

print "List is"
list.print_list()
print "list size is"
print list.size
list.delete_node(4)
list.print_list()
print list.size
list.delete_node(26)
list.search(24)
list.print_list()
list.reverse_list()
list.print_list()
list.recursion_reverse(list.head)
list.print_list()