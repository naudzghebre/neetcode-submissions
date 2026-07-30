class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums, self.k  = nums, k
        heapq.heapify(self.nums)

        while len(self.nums) > k:
            heapq.heappop(self.nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)
        return self.nums[0]


    # def __init__(self, k: int, nums: List[int]):
    #     self.k = k
    #     self.kList = []
    #     self.nums = nums
    #     for n in nums:
    #         if len(self.kList) < k:
    #             self.kList.append(n)
    #             self.kList = sorted(self.kList)
    #         else:
    #             for i, kVal in enumerate(self.kList):
    #                 if kVal < n:
    #                     self.kList[i] = n
    #                     self.kList = sorted(self.kList)
    #                     break

    # O(k log k)
    # def add(self, val: int) -> int:
        # self.nums.append(val)

        # if len(self.kList) < self.k:
        #     self.kList.append(val)
        #     return min(self.kList)

        # for i, k in enumerate(self.kList):
        #     if k < val:
        #         self.kList[i] = val
        #         self.kList = sorted(self.kList)
        #         break
        # return min(self.kList)

    # O(k + n log n)
    # def add(self, val: int) -> int:
    #     self.nums.append(val)
    #     self.nums.sort()
    #     return self.nums[-self.k]

