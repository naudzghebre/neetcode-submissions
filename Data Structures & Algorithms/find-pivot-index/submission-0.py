class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        postfixSum = [0] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            postfixSum[i] = postfixSum[i+1] + nums[i+1]
        
        prefixSum = [0] * len(nums)
        for i in range(len(nums)):
            if i == 0: prefixSum[i] = 0
            else: prefixSum[i] = prefixSum[i-1] + nums[i-1]

            if prefixSum[i] == postfixSum[i]: return i

        return -1
