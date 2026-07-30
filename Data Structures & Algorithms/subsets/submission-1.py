class Solution:

    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]

        for num in nums:
            new_subsets = []

            for i in range(len(result)):
                existing_subset = result[i]
                copy = existing_subset.copy()
                copy.append(num)
                new_subsets.append(copy)

            for i in range(len(new_subsets)):
                result.append(new_subsets[i])

        return result

    # Recursive Backtracking
    # O(n 2^n)
    # def subsets(self, nums: List[int]) -> List[List[int]]:
    #     res = []
    #     subset = []

    #     def dfs(i):
    #         if i >= len(nums):
    #             res.append(subset.copy())

    #             return
    #         subset.append(nums[i])
    #         dfs(i + 1)
    #         subset.pop()
    #         dfs(i + 1)

    #     dfs(0)
    #     return res

    # Iterative
    # O(n 2^n)
    # def subsets(self, nums: List[int]) -> List[List[int]]:
    #     subsets = [[]]
    #     for num in nums:
    #         subsets += [sets + [num] for sets in subsets]
    #     return subsets


