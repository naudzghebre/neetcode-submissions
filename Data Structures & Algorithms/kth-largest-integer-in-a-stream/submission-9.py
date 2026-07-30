class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.kList = []
        self.nums = nums
        for n in nums:
            if len(self.kList) < k:
                self.kList.append(n)
                self.kList = sorted(self.kList)
            else:
                for i, kVal in enumerate(self.kList):
                    if kVal < n:
                        self.kList[i] = n
                        self.kList = sorted(self.kList)
                        break
        print(self.kList)


    def add(self, val: int) -> int:
        self.nums.append(val)

        if len(self.kList) < self.k:
            self.kList.append(val)
            return min(self.kList)

        for i, k in enumerate(self.kList):
            if k < val:
                self.kList[i] = val
                self.kList = sorted(self.kList)
                break
        print(self.kList)
        return min(self.kList)

    # O(k + n log n)
    # def add(self, val: int) -> int:
    #     self.nums.append(val)
    #     self.nums.sort()
    #     return self.nums[-self.k]

