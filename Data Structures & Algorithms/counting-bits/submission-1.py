class Solution:

    # Nice shorthand for the below solution
    def countBits(self, n: int) -> List[int]:
        counts = [0] * (n + 1)
        for i in range(1, n + 1):
            counts[i] = counts[i >> 1] + (i & 1)
        return counts    

    # If it's even, has the same num of 1s as num // 2 (floor)
    # else, has same num as num // 2 plus the odd bit
    # def countBits(self, n: int) -> List[int]:
    #     counts = [0] * (n+1)
    #     for i in range(1, n+1):
    #         if i % 2 == 0: counts[i] = counts[i // 2]
    #         else: counts[i] = counts[i // 2] + 1
    #     return counts

    # O(n log n) - we can do better
    # def countBits(self, n: int) -> List[int]:
    #     counts = [0] * (n+1)
    #     for i in range(1, n+1):
    #         bits, count = i, 0
    #         while bits > 0:
    #             if bits & 1 == 1:
    #                 count += 1
    #             bits //= 2
    #         counts[i] = count
    #     return counts