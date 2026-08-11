class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        memo = [[0] * n for _ in range(m)]

        def dp(r, c) -> int:
            if r >= m or c >= n or obstacleGrid[r][c]: return 0
            elif r == m-1 and c == n-1:
                print(r, c)
                memo[r][c] = 1
                return 1
            elif memo[r][c]:
                return memo[r][c]

            memo[r][c] =  dp(r+1, c) + dp(r, c+1)
            return memo[r][c]
        
        dp(0, 0)
        return memo[0][0]