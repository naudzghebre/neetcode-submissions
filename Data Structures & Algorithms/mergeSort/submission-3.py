# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        n = len(pairs)
        buf = [None] * n

        def sort(lo, hi):  # half-open [lo, hi)
            if hi - lo <= 1:
                return
            mid = (lo + hi) // 2
            sort(lo, mid)
            sort(mid, hi)
            i, j, k = lo, mid, lo
            while i < mid and j < hi:
                if pairs[i].key <= pairs[j].key:
                    buf[k] = pairs[i]; i += 1
                else:
                    buf[k] = pairs[j]; j += 1
                k += 1
            while i < mid:
                buf[k] = pairs[i]; i += 1; k += 1
            while j < hi:
                buf[k] = pairs[j]; j += 1; k += 1
            for t in range(lo, hi):
                pairs[t] = buf[t]

        sort(0, n)
        return pairs


