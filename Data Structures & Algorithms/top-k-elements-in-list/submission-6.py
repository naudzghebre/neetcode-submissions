class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            counts[n] = counts.get(n, 0) + 1
        for n, c in counts.items():
            freq[c].append(n)
        
        include = []
        ind = len(freq) - 1
        while k > 0:
            for e in freq[ind]:
                include.append(e)
                k -= 1

                # if k == 0:
                #     break
            ind -= 1

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
