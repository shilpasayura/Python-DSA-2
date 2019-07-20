class Deque(object):
    def __init__(self):
        self.size = 0
        self.deque = list()

    def __len__(self):
        return len(self.deque)

    def __repr__(self):
        if self.is_empty():
            print("Deque is empty")
        return ' '.join(map(str, self.deque))

    def add_front(self, item):
        self.deque.insert(0, item)

    def add_rear(self, item):
        self.deque.append(item)

    def remove_front(self):
        return self.deque.pop(0)

    def remove_rear(self):
        return self.deque.pop()

    def is_empty(self):
        return self.size == 0

deque = Deque()
print deque
deque.add_front(3)
deque.add_front(4)
deque.add_rear(7)
deque.add_rear(8)
print deque
deque.remove_front()
print deque
deque.remove_rear()
print deque