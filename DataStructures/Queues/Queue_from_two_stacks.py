class Empty(Exception):
    pass


class Queue(object):
    def __init__(self):
        self.S1 = self.create_stack()
        self.S2 = self.create_stack()

    def create_stack(self):
        stack  = list()
        return stack

    def push(self, stack, element):
        stack.append(element)

    def pop(self, stack):
        if not self.is_empty(stack):
            return stack.pop()

    def is_empty(self, stack):
        return len(stack) == 0

    def enque(self, element):
        self.push(self.S1, element)

    def deque(self):
        if self.is_empty(self.S1) and self.is_empty(self.S2):
            raise Empty("Queue is empty")
        if self.is_empty(self.S2):
            while not self.is_empty(self.S1):
                self.push(self.S2, self.pop(self.S1))
        return self.pop(self.S2)

    def print_queue(self):
        pass

Q = Queue()
Q.enque(2)
Q.enque(3)
Q.enque(4)
print Q.deque()
print Q.deque()
Q.enque(6)
print Q.deque()