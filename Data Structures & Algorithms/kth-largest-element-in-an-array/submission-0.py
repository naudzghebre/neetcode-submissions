class Solution:

    # O(n log k)
    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.minHeap = []

        for n in nums:
            heapq.heappush(self.minHeap, n)
            if len(self.minHeap) > k:
                heapq.heappop(self.minHeap)
        
        return self.minHeap[0]
            