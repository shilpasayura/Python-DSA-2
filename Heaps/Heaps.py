# Program: Max Heap


class MaxHeap(object):

    def __init__(self):
        self.heap = []

    def insert(self, item):
        self.heap.append(item)
        self.bubble_up(len(self.heap)-1)

    def pop(self):
        if len(self.heap) > 1:
            # Swap the max value with last value and bubble down
            self.heap[0], self.heap[len(self.heap)-1] = self.heap[len(self.heap)-1], self.heap[0]
            max = self.heap.pop()
            self.bubble_down(len(self.heap), 0)
        else:
            max = self.heap.pop()

        return max

    def bubble_up(self, index):
        parent = index//2
        if index < 1:
            return
        elif self.heap[parent] < self.heap[index]:
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            self.bubble_up(parent)

    def bubble_down(self, n, index):
        left = 2*index+1
        right = 2*index+2
        largest = index
        if n > left and self.heap[left] > self.heap[largest]:
            largest = left
        if n > right and self.heap[right] > self.heap[largest]:
            largest = right
        if largest != index:
            self.heap[largest], self.heap[index] = self.heap[index], self.heap[largest]
            self.bubble_down(n, largest)

    def heap_sort(self):
        n = len(self.heap)
        for i in range(n-1, 0, -1):
            self.heap[i], self.heap[0] = self.heap[0], self.heap[i]
            self.bubble_down(i, 0)
        print self

    def __repr__(self):
        return ' '.join(map(str, self.heap))


h = MaxHeap()
h.insert(56)
h.insert(72)
h.insert(46)
h.insert(32)
h.insert(86)
h.insert(92)
h.insert(101)
h.insert(11)
h.insert(51)
h.insert(121)
print h
print h.pop()

print h.heap_sort()


