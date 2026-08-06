class Node:
    def __init__(self, key, val) -> None:
        self.key, self.val = key, val
        self.prev = self.next = None

# Optimized with inspiration from Python's lru_cache impl
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity, self.cache = capacity, {}
        self.lru, self.mru = Node(0, 0),  Node(0, 0)
        self.lru.next, self.mru.prev = self.mru, self.lru

    def insert(self, node):
        prev, next = self.mru.prev, self.mru
        prev.next = next.prev = node
        node.next, node.prev = next, prev

    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev


    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key)
        if node is not None:
            node.val = value
            self.remove(node)
            self.insert(node)
            return
        
        node = self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.lru.next
            self.remove(lru)
            del self.cache[lru.key]

# O(1) get/puts
# class LRUCache:
#     def __init__(self, capacity: int):
#         self.capacity, self.cache = capacity, {}
#         self.lru, self.mru = Node(0, 0),  Node(0, 0)
#         self.lru.next, self.mru.prev = self.mru, self.lru

#     def insert(self, node):
#         prev, next = self.mru.prev, self.mru
#         prev.next = next.prev = node
#         node.next, node.prev = next, prev

#     def remove(self, node):
#         prev, next = node.prev, node.next
#         prev.next, next.prev = next, prev


#     def get(self, key: int) -> int:
#         if key in self.cache:
#             self.remove(self.cache[key])
#             self.insert(self.cache[key])
#             return self.cache[key].val
#         return -1

#     def put(self, key: int, value: int) -> None:
#         if key in self.cache:
#             self.remove(self.cache[key])
#         self.cache[key] = Node(key, value)
#         self.insert(self.cache[key])

#         if len(self.cache) > self.capacity:
#             lru = self.lru.next
#             self.remove(self.cache[lru.key])
#             del self.cache[lru.key]


# Brute Force
# get/put both in O(n)
# class LRUCache:
#     def __init__(self, capacity: int):
#         self.capacity, self.cache = capacity, []

#     def get(self, key: int) -> int:
#         for i in range(len(self.cache)):
#             (k, v) = self.cache[i]
#             if k == key:
#                 # remove from position and move to the end.
#                 self.cache.pop(i)
#                 self.cache.append((k, v))
#                 return v
#         return -1

#     def put(self, key: int, value: int) -> None:
#         for i in range(len(self.cache)):
#             k, v = self.cache[i]
#             if k == key:
#                 self.cache.pop(i)
#                 self.cache.append((key, value))
#                 return
#         # If not in the cache, add the new entry.
#         self.cache.append((key, value))
#         if len(self.cache) > self.capacity:
#             self.cache.pop(0)
