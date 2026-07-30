class Solution:

    # Maintain a minheap of max values - but always evicting the min val when a
    # larger value comes along
    # O(n log k)
    # def findKthLargest(self, nums: List[int], k: int) -> int:
    #     self.minHeap = []

    #     for n in nums:
    #         heapq.heappush(self.minHeap, n)
    #         if len(self.minHeap) > k:
    #             heapq.heappop(self.minHeap)
        
    #     return self.minHeap[0]

     def findKthLargest(self, nums: List[int], k: int) -> int:
            nums.sort(reverse=True)
            for n in nums:
                if k == 1:
                    return n
                k -= 1