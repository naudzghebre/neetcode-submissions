class Solution:
    def countBits(self, n: int) -> List[int]:
        counts = [0] * (n+1)
        for i in range(1, n+1):
            bits, count = i, 0
            while bits > 0:
                if bits & 1 == 1:
                    count += 1
                bits //= 2
            counts[i] = count
        return counts