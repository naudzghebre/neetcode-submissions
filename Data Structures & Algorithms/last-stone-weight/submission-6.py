class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        print(stones)

        while len(stones) > 1:
            x, y = heapq.heappop_max(stones), heapq.heappop_max(stones)

            if x == y: heapq.heappush_max(stones, 0)
            elif x > y: heapq.heappush_max(stones, x - y)
            else: heapq.heappush_max(stones, y - x)

            print(stones)

        return stones[0]