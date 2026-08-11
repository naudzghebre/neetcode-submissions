class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        memo = [[-1] * n for _ in range(m)]

        def dp(l, r) -> int:

            if l >= m or r >= n: return 0
            elif memo[l][r] >= 0: return memo[l][r]
            else:
                # If letters match, move both indices forward to look for more
                # subsequent matchings
                if text1[l] == text2[r]:
                    memo[l][r] = 1 + dp(l + 1, r + 1)
                else:
                    # Check subsequent paths, one without each of the two letters
                    memo[l][r] = max(dp(l+1, r), dp(l, r+1))
                return memo[l][r]
        dp(0, 0)
        return memo[0][0]
