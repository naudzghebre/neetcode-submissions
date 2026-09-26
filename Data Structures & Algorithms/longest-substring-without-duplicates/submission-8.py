class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # if len(s) in [0, 1]: return len(s)

        L, longest, seen = 0, 0, set()

        for R in range(len(s)):
            while s[R] in seen:
                seen.remove(s[L])
                L += 1

            longest = max(longest, R - L + 1)
            seen.add(s[R])

        return longest