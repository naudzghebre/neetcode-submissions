class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefix = [[r[0]] * len(r) for r in matrix]
        for r in range(len(matrix)):
            for c in range(1, len(matrix[r])):
                self.prefix[r][c] = self.prefix[r][c-1] + matrix[r][c]        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        s = 0
        for r in range(row1, row2 + 1):
            leftSum = self.prefix[r][col1 -1] if col1 > 0 else 0
            rightSum = self.prefix[r][col2]
            s += (rightSum - leftSum)
        return s
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)