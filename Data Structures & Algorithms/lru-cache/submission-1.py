# Brute Force
# get/put both in O(n)
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = []
        

    def get(self, key: int) -> int:
        for i in range(len(self.cache)):
            (k, v) = self.cache[i]
            if k == key:
                self.cache.pop(i)
                self.cache.append((k, v))
                return v
        return -1

    def put(self, key: int, value: int) -> None:
        for i in range(len(self.cache)):
            k, v = self.cache[i]
            if k == key:
                self.cache.pop(i)
                self.cache.append((k, value))
                return

        self.cache.append((key, value))
        if len(self.cache) > self.capacity:
            self.cache.pop(0)
