class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            counts[n] = counts.get(n, 0) + 1
        for n, c in counts.items():
            freq[c].append(n)
        
        include = []
        for i in range(len(freq) - 1, 0, -1):
            for e in freq[i]:
                include.append(e)
                if len(include) == k:
                    return include

        return include

    # O(k * n)
    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #     topK = []
    #     counts = {}
    #     # O(n)
    #     for n in nums:
    #         counts[n] = counts.get(n, 0) + 1

    #         if len(topK) < k and n not in topK:
    #             topK.append(n)
    #         elif  n in topK:
    #             continue
    #         else:
    #             # O(k)
    #             for i in range(len(topK)):                    
    #                 if counts[topK[i]] < counts[n]:
    #                     temp = topK[i]
    #                     topK[i] = n
    #                     n = temp
    #     return topK
