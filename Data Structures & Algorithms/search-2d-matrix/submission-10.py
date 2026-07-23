class Solution:

    # 7. Binary search over entire matrix, treating it as one big list
    # by flattening mappings (row,col)
    # O(log mn) 
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        numRows, numCols = len(matrix), len(matrix[0])
        l, r = 0, numRows * numCols - 1

        while l <= r:
            mid = (l + r) // 2
            row, col = mid // numCols, mid % numCols

            if target == matrix[row][col]: return True
            elif target > matrix[row][col]: l = mid + 1
            else: r = mid - 1
        return False

    # 6. Binary search over end values of the array, then over the row that gets selected
    # O(log m + log n) = O(log mn) 
    # def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    #     m, n = len(matrix), len(matrix[0])

    #     # O(log m)
    #     top, bottom, row = 0, m - 1, 0
    #     while top <= bottom:
    #         row = (top + bottom) // 2
    #         if target > matrix[row][-1]: top = row + 1
    #         elif target < matrix[row][0]: bottom = row - 1
    #         else: break
        
    #     if top > bottom: return False

    #     # O(log n)
    #     l, r = 0, n - 1
    #     while l <= r:
    #         col = (l + r) // 2
    #         if target == matrix[row][col]: return True
    #         elif target > matrix[row][col]: l = col + 1
    #         else:
    #             r = col - 1
    #     return False


    # 5. Staircase smart search going down the rows and checking last value till
    # you're sure about which row it's in - linear search
    # O(m + n) 
    # def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    #     for r in matrix:
    #         if r[-1] < target: continue # Go down

    #         for c in r:
    #             if c == target: return True
    #         return False
    #     return False

    # 4. Staircase smart search going down the rows and checking last value till
    # you're sure about which row it's in - run binary search
    # O(m + log n) 
    # def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    #     for r in matrix:
    #         if r[-1] < target: continue # Go down
    #         else:
    #             return self.binarySearch(r, target)
    #     return False


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


        