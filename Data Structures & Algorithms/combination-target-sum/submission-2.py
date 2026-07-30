class Solution:
    # Backtracking optimized
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return

            for j in range(i, len(nums)):
                if total + nums[j] > target:
                    return

                curr.append(nums[j])
                dfs(j, curr, total + nums[j])
                curr.pop()

        dfs(0, [], 0)
        return res
    
    # def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
    #     res = []
    #     subset = []
    #     # nums.sort()

    #     def dfs(i):
    #         print(subset)
    #         if sum(subset) > target or i >= len(nums):
    #             return
    #         elif sum(subset) == target:
    #             res.append(subset.copy())
    #             return

    #         subset.append(nums[i])
    #         dfs(i)
    #         subset.pop()
    #         dfs(i + 1)

    #     dfs(0)
    #     return res