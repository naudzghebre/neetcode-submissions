class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[0] * n for _ in range(m)]

        def dp(r, c) -> int:
            if r >= m or c >= n: return 0

            if r == m-1 and c == n-1:
                print(r, c)
                memo[r][c] = 1
                return 1
            elif memo[r][c]:
                return memo[r][c]

                
            memo[r][c] =  dp(r+1, c) + dp(r, c+1)
            return memo[r][c]
        dp(0, 0)
        print(memo)
        return memo[0][0]