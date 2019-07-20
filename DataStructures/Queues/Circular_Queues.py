class CircularQueue(object):

    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    def __len__(self):
        return self.size

    def __repr__(self):
        '''To print the circular queue'''
        if self.front == self.rear == -1:
            print("Queue is Empty")
        elif self.rear >= self.front:
            return ' '.join(map(str, [self.queue[element] for element in range(self.front, self.rear+1)]))
        else:
            return ' '.join(map(str, [self.queue[element%self.size] for element in range(self.rear, self.front + self.rear + 1)]))

    def is_empty(self):
        return self.size == 0

    def enqueue(self, item):
        # Check if Queue is full
        if (self.rear + 1) % self.size == self.front:
            print("Queue is full")
        # Check for empty queue
        elif self.front == -1:
            self.front = self.rear = 0
            self.queue[self.rear] = item
        else:
            self.rear = (self.rear + 1)% self.size
            self.queue[self.rear] = item

    def dequeue(self):
        # Check if queue is empty
        if self.front == -1:
            print("Queue is Empty")
            return
        # Check for only 1 element
        elif self.front == self.rear:
            temp = self.queue[self.front]
            self.front = self.rear = -1
            return temp
        else:
            temp = self.queue[self.front]
            self.front = (self.front + 1) % self.size
            return temp


deque = CircularQueue(5)
deque.enqueue(14)
deque.enqueue(22)
deque.enqueue(13)
deque.enqueue(-6)
print deque
print ("Deleted value = ", deque.dequeue())
print ("Deleted value = ", deque.dequeue())
print deque
deque.enqueue(9)
deque.enqueue(20)
deque.enqueue(5)
print deque






