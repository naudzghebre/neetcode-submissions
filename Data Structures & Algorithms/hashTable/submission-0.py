class HashTable:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.map = [None for _ in range(capacity)]

    def _hash(self, key: int):
        return key % self.capacity

    def insert(self, key: int, value: int) -> None:
        ind = self._hash(key)
        while self.map[ind]:
            if self.map[ind][0] == key:
                self.map[ind] = (key, value)
                return
            ind = (ind + 1) % self.capacity
        self.map[ind] = (key, value)
        self.size += 1

        if self.size >= self.capacity // 2:
            self.resize()


    def get(self, key: int) -> int:
        ind = self._hash(key)
        while self.map[ind]:
            if self.map[ind][0] == key:
                return self.map[ind][1]
            ind = (ind + 1) % self.capacity
        return -1

    def remove(self, key: int) -> bool:
        ind = self._hash(key)
        while self.map[ind]:
            if self.map[ind][0] == key:
                self.map[ind] = None
                self.size -= 1
                return True
            ind = (ind + 1) % self.capacity
        return False

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        self.capacity *= 2
        self.size = 0
        oldMap = self.map
        self.map = [None for _ in range(self.capacity)]

        for item in oldMap:
            if item:
                self.insert(item[0], item[1])

