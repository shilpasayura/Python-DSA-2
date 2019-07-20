from DoublyLinkedList import DoublyLinkedBase


class Empty(Exception):
    pass


class LinkedDeque(DoublyLinkedBase):

    def first(self):
        if self.is_empty():
            raise Empty("Deque is Empty")
        return self.header.next.data

    def last(self):
        if self.is_empty():
            raise Empty("Deque is Empty")
        return self.trailer.prev.data

    def insert_first(self, value):
        self.insert_between(value, self.header, self.header.next)

    def insert_last(self, value):
        self.insert_between(value, self.trailer.prev, self.trailer)

    def delete_first(self):
        if self.is_empty():
            raise Empty("Deque is Empty")
        self.delete_node(self.header.next)

    def delete_last(self):
        if self.is_empty():
            raise Empty("Deque is Empty")
        self.delete_node(self.trailer.prev)


deque = LinkedDeque()
deque.insert_first(1)
deque.insert_first(2)
deque.insert_last(3)
deque.delete_first()
deque.insert_last(5)
deque.print_list()
deque.delete_last()
deque.print_list()