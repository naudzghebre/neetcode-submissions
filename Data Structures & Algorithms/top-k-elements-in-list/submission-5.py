class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        topK = []
        counts = {}
        # O(n)
        for n in nums:
            counts[n] = counts.get(n, 0) + 1

            if len(topK) < k and n not in topK:
                topK.append(n)
            elif  n in topK:
                continue
            else:
                # O(3)
                for i in range(len(topK)):                    
                    if counts[topK[i]] < counts[n]:
                        temp = topK[i]
                        topK[i] = n
                        n = temp
        return topK
