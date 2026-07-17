class Solution:

    # brute force
    def maxArea(self, heights: List[int]) -> int:
        maxVolume = -10**4
        for i in range(len(heights) - 1):
            for j in range(i+1, len(heights)):
                maxVolume = max(maxVolume, min(heights[i], heights[j])*(j-i))
        return maxVolume
        