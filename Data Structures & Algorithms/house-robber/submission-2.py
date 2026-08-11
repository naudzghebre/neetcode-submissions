class Solution:

    def rob(self, nums: List[int]) -> int:            
        n = len(nums)
        memo = [-1] * n

        def dfs(i) -> int:
            if i >= n: return 0
            if memo[i] != -1:
                return memo[i]
            else:
                memo[i] = max(nums[i] + dfs(i + 2), dfs(i+1))
                return memo[i]
        return dfs(0)

    # Too inefficient - O(2^n)
    # def rob(self, nums: List[int]) -> int:            
    #     n = len(nums)

    #     def dfs(i) -> int:
    #         if i >= n: return 0

    #         return max(nums[i] + dfs(i + 2), dfs(i+1))
    #     return dfs(0)