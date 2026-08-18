class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        windowSum = 0
        criteria = 0
        L = 0

        for R in range(len(arr)):
            # Add new element to window
            windowSum += arr[R]
            
            # Check if window is full (size k)
            if R >= k - 1:
                # Check if window meets criteria
                if windowSum / k >= threshold:
                    criteria += 1
                # Remove leftmost element for next iteration
                windowSum -= arr[L]
                L += 1

        return criteria