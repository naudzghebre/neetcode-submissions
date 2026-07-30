class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        # nums.sort()

        def dfs(i):
            if sum(subset) > target or i >= len(nums):
                return
            elif sum(subset) == target:
                res.append(subset.copy())
                return

            subset.append(nums[i])
            dfs(i)
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res