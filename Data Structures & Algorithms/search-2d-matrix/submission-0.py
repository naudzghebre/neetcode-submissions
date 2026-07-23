class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        mn = (len(matrix) * len(matrix[0]))
        matrixList = mn *[0]
        i = 0
        for r in matrix:
            for c in r:
                matrixList[i] = c
                i += 1

        l, r = 0, mn - 1
        while l <= r:
            m = (l + r) // 2
            if matrixList[m] == target: return True
            elif matrixList[m] < target: l = m + 1
            else: r = m - 1
        return False

        