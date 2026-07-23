class Solution:

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        for r in matrix:
            if r[-1] < target: continue # Go down
            else:
                return self.binarySearch(r, target)
        return False


    # 3. Binary search over every row
    # O(m log n)
    # def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    #     for r in matrix:
    #         if self.binarySearch(r, target): return True
    #     return False

    # 2. Construct list and then run binary search
    # O(m*n + log m*n) = O(m*n)
    # def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    #     # O(m*n)
    #     mn = (len(matrix) * len(matrix[0]))
    #     matrixList = mn *[0]
    #     i = 0
    #     for r in matrix:
    #         for c in r:
    #             matrixList[i] = c
    #             i += 1
    #     return self.binarySearch(matrixList, target) # Passing in combined list so - O(log m*n)

    # 1. Linear pass brute force
    # O(m*n)
    # def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    #     for r in matrix:
    #         for c in r:
    #             if c == target: return True
    #     return False

    # Helper binary search method
    # O(log len(nums))
    def binarySearch(self, nums: list, target: int) -> bool:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target: return True
            elif nums[m] < target: l = m + 1
            else: r = m - 1
        return False


        