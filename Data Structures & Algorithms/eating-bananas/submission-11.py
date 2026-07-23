class Solution:

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, kMax = 1, max(piles)

        while l <= kMax:
            km = (l + kMax) // 2
            hours = sum(math.ceil(p / km) for p in piles)
            print(l, km, kMax, hours)

            # print("k: " + str(maxK))
            # print("hours: " + str(hours))
            if hours <= h:
                kMax = km - 1
            else:
                l = km + 1

        return l


    # def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
    #     hours = 0
    #     minK = kMax = max(piles)

    #     l, r = 1, kMax
    #     while l <= r:
    #         m = (l + r) // 2
    #         hours = 0
    #         for p in piles:
    #             if p <= m: hours += 1
    #             else:
    #                 hours += (p // m + 1)

    #         if hours <= h:
    #             minK = min(minK, m)
    #             l = m + 1
    #         else:
    #             r = m - 1
    #     return minK

    # Too inefficient
    # O(n + n * s) - where s is the sum of the input array
    # def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
    #     hours = 0
    #     minK = kMax = sum(piles)

    #     while kMax > 0:
    #         hours = 0
    #         for p in piles:
    #             if p <= kMax: hours += 1
    #             else:
    #                 hours += (p // kMax + 1)

    #         if hours <= h:
    #             minK = min(minK, kMax)
    #         kMax -= 1
    #     return minK
            