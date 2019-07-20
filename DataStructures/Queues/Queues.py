# Queue implementation from Arrays


class Empty(Exception):
    pass


class Queue(object):
    def __init__(self):
        self.size = 0
        self.queue = list()
        self.front = None
        self.rear = None

    def __len__(self):
        return len(self.queue)

    def __repr__(self):
        if self.is_empty():
            print("Queue is Empty")
        return ' '.join(map(str, self.queue))

    def enqueue(self, item):
        if self.size == 0:
            self.front = 0
            self.rear = 0
        else:
            self.rear += 1
        self.queue.append(item)
        self.size += 1
        print "Queue appended with %s" % item

    def dequeue(self):
        item = self.queue.pop(0)
        self.front -= 1
        print "Dequeued %s from queue" % item

    def is_empty(self):
        return self.size == 0

    def size(self):
        return self.size

    def queue_front(self):
        if self.is_empty():
            print("Queue is Empty")
            return
        return self.queue[self.front]

    def queue_rear(self):
        if self.is_empty():
            print("Queue is Empty")
            return
        return self.queue[self.rear]


queue = Queue()
print queue
queue.enqueue(7)
print("Queue front is", queue.queue_front())
print("Queue front is", queue.queue_rear())
queue.enqueue(9)
print queue
queue.dequeue()
queue.dequeue()
print queue