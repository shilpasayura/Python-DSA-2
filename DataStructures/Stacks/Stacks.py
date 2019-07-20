# Stack implementation from Arrays


class Empty(Exception):
    pass


class Stack(object):
    def __init__(self):
        self.data = list()

    def __len__(self):
        return len(self.data)

    def __repr__(self):
        return str([element for element in self.data])

    def push(self, val):
        self.data.append(val)

    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self.data.pop()

    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self.data[-1]

    def is_empty(self):
        return len(self.data) == 0

    def print_elements(self):
        return [element for element in self.data]