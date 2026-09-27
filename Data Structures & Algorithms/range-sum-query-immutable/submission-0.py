class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = [nums[0]] * len(nums)
        for i in range(1, len(nums)):
            self.prefix[i] = self.prefix[i-1] + nums[i]
        
    def sumRange(self, left: int, right: int) -> int:
        leftSum = self.prefix[left-1] if left > 0 else 0
        rightSum = self.prefix[right]
        return rightSum - leftSum
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)