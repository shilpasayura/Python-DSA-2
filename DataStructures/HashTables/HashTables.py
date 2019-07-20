# Program: HasTables Implementation in Python


class HashTable(object):
    def __init__(self):
        self.size = 10
        self.keys = [None] * self.size
        self.values = [None] * self.size

    def hashing(self, key):
        return key % self.size

    def rehashing(self, oldhash):
        return (oldhash+1) % self.size

    def get(self, key):
        index = self.hashing(key)

        while self.keys[index] is None:
            index = self.rehashing(index)

        if self.keys[index] == key:
            return self.values[index]

        return None

    def put(self, key, value):
        index = self.hashing(key)

        while self.keys[index] is not None:
            index = self.rehashing(index)

        self.keys[index] = key
        self.values[index] = value

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.put(key, value)


table = HashTable()

table[1] = 'One'
table[2] = 'Two'
table[3] = 'Three'


print(table[1])
print(table[2])
print(table[3])