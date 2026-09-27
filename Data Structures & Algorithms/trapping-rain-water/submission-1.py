class Solution:

    def trap(self, height: List[int]) -> int:
        n, l, r = len(height), 0, len(height) - 1

        if n == 0: return 0

        leftMax, rightMax = [0] * n, [0] * n

        leftMax[0] = height[0]
        for i in range(1, n):
            leftMax[i] = max(leftMax[i - 1], height[i])

        rightMax[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            rightMax[i] = max(rightMax[i + 1], height[i])

        area = 0
        for i in range(n):
            area += min(leftMax[i], rightMax[i]) - height[i]
        return area


    # O(n^2) solution - too long
    # def trap(self, height: List[int]) -> int:
    #     n, area = len(height), 0
    #     for i in range(len(height)):
    #         a = min(self.findMax(height, i, 'left'), self.findMax(height, i, 'right')) - height[i]
    #         print(a)
    #         area += a

    #     return area
        
    # def findMax(self, height: List[int], ind: int, direction: str) -> int:
    #     n, iter_direction = len(height), None
    #     if direction == 'left': iter_direction = range(ind)
    #     else: iter_direction = range(ind + 1, n)

    #     maxHeight = height[ind]
    #     for i in iter_direction:
    #         maxHeight = max(maxHeight, height[i])
    #     return maxHeight

