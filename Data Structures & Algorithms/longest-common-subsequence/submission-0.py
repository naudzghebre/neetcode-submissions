class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        memo = [[0] * n for _ in range(m)]
        longest = 0

        def dp(l, r) -> int:

            if l >= m or r >= n: return 0
            elif memo[l][r]: return memo[l][r]
            else:
                left, right = text1[l], text2[r]

                if left == right:
                    memo[l][r] = 1 + dp(l + 1, r + 1)
                else:
                    memo[l][r] = max(longest, dp(l+1, r), dp(l, r+1))
                return memo[l][r]
        dp(0, 0)
        return memo[0][0]
