class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        topK = []
        counts = {}
        # O(n)
        for n in nums:
            counts[n] = counts.get(n, 0) + 1

            if n in topK:
                continue
            elif len(topK) < k:
                topK.append(n)
            else:
                # O(3)
                for i in range(len(topK)):
                    if topK[i] == n:
                        break
                    
                    if counts[topK[i]] < counts[n]:
                        temp = topK[i]
                        topK[i] = n
                        n = temp
                print
        return topK
