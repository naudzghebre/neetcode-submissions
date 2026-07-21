# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        if len(pairs) <= 1:
            return pairs

        m = len(pairs) // 2
        left = self.mergeSort(pairs[0:m])
        right = self.mergeSort(pairs[m:])

        merged = []

        ll, lr = 0, 0
        while ll < len(left) or lr < len(right):
            if ll < len(left) and lr < len(right):
                if left[ll].key <= right[lr].key:
                    merged.append(left[ll])
                    ll += 1
                else:
                    merged.append(right[lr])
                    lr += 1
            elif ll < len(left):
                while ll < len(left):
                    merged.append(left[ll])
                    ll += 1
            else:
                while lr < len(right):
                    merged.append(right[lr])
                    lr += 1
        return merged


