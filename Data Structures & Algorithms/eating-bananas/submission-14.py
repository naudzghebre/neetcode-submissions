class Solution:

    # O(m*n)
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, kMax = 1, max(piles)
        k = kMax
        # O(m)
        while l <= kMax:
            km = (l + kMax) // 2
            # O(n)
            hours = sum(math.ceil(p / km) for p in piles)

            if hours <= h:
                k = km
                kMax = km - 1
            else:
                l = km + 1

        return l

    # Too inefficient
    # O(m * n) - m is max number in piles, and n is length of list
    # def minEatingSpeed(self, piles: List[int], h: int) -> int:
    #     speed = 1
    #     while True:
    #         totalTime = 0
    #         for pile in piles:
    #             totalTime += math.ceil(pile / speed)

    #         if totalTime <= h:
    #             return speed
    #         speed += 1
    #     return speed