class Solution:
    # Bottom Up Approach
    def uniquePaths(self, m: int, n: int) -> int:
        currRow = [0] * n
        currRow[-1] = 1

        for i in range(m-1, -1, -1):
            prevRow =  currRow
            currRow = [0] * n
            currRow[-1] = 1
            for j in range(n-2, -1, -1):
                currRow[j] = prevRow[j] + currRow[j + 1]

        
        return currRow[0]

    # Top Down Approach
    # def uniquePaths(self, m: int, n: int) -> int:
    #     memo = [[0] * n for _ in range(m)]

    #     def dp(r, c) -> int:
    #         if r >= m or c >= n: return 0

    #         if r == m-1 and c == n-1:
    #             print(r, c)
    #             memo[r][c] = 1
    #             return 1
    #         elif memo[r][c]:
    #             return memo[r][c]

    #         memo[r][c] =  dp(r+1, c) + dp(r, c+1)
    #         return memo[r][c]
        
    #     dp(0, 0)
    #     return memo[0][0]