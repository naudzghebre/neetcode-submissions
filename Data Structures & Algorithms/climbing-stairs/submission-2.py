class Solution:

    def climbStairs(self, n: int) -> int:
        dp = [1, 2]

        if n == 1: return 1
        elif n == 2: return 2
        else:
            while n > 2:
                dp[0], dp[1] = dp[1], dp[0] + dp[1]
                n -= 1
            return dp[1]

    # O(2^n) - too inefficient
    # def climbStairs(self, n: int) -> int:
    #     if n == 1: return 1
    #     elif n == 2: return 2
    #     else: return self.climbStairs(n-1) + self.climbStairs(n-2)