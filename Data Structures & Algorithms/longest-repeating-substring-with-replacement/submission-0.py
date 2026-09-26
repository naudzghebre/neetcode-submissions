class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L, longest, counts = 0, 0, {}

        for R in range(len(s)):
            counts[s[R]] = counts.get(s[R], 0) + 1

            while (R - L + 1) - max(counts.values()) > k:
                counts[s[L]] -= 1
                L += 1

            longest = max(longest, R - L + 1)
        return longest
