class Solution:
    def reverseBits(self, n: int) -> int:
        reverse = 0
        for i in range(32):
            reverse *= 2
            if n & 1 == 1: reverse +=  1

            n //= 2
            print(reverse)
        return reverse