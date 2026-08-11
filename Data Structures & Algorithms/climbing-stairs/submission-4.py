class Solution:

    def climbStairs(self, n: int) -> int:
        one, two = 1, 2

        if n == 1: return one
        elif n == 2: return two
        else:
            while n > 2:
                one, two = two, one + two
                n -= 1
            return two

    # O(2^n) - too inefficient
    # def climbStairs(self, n: int) -> int:
    #     if n == 1: return 1
    #     elif n == 2: return 2
    #     else: return self.climbStairs(n-1) + self.climbStairs(n-2)