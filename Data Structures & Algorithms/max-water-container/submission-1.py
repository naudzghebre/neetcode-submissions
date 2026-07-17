class Solution:

    def maxArea(self, heights: List[int]) -> int:
        maxVolume = -10**4
        l, r = 0, len(heights) - 1

        while l < r:
            newVolume = min(heights[l], heights[r]) * (r-l)
            maxVolume = max(maxVolume, newVolume)

            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return maxVolume

    # brute force
    # def maxArea(self, heights: List[int]) -> int:
    #     maxVolume = -10**4
    #     for i in range(len(heights) - 1):
    #         for j in range(i+1, len(heights)):
    #             maxVolume = max(maxVolume, min(heights[i], heights[j])*(j-i))
    #     return maxVolume
        