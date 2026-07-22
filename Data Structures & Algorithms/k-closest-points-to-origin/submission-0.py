import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = [(points[i][0]**2 + points[i][1] ** 2, i) for i in range(k)]
        heapq.heapify_max(heap)
        for i in range(k, len(points)):
            dist = points[i][0] ** 2 + points[i][1] ** 2
            if dist < heap[0][0]:
                heapq.heappushpop_max(heap, (dist, i))
        return [points[i] for (_, i) in heap] 
        