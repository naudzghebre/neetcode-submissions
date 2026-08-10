class Graph:
    
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, src: int, dst: int) -> None:
        self.graph[src].append(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        neighbors = self.graph[src]
        for n in neighbors:
            if n == dst:
                neighbors.remove(dst)
                return True
        return False


    def hasPath(self, src: int, dst: int) -> bool:

        visited, queue = set([src]), deque([src])
        print(visited)
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()

                if node == dst: return True

                for n in self.graph[node]:
                    print(n)
                    if n not in visited:
                        queue.append(n)
                        visited.add(n)
        return False

