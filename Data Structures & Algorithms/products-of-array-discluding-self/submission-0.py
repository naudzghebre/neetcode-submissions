class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_product = 1
        zeroCount = 0
        output = nums
        for n in nums:
            if n == 0:
                zeroCount += 1
            else:
                total_product *= n

        for i in range(len(output)):
            if zeroCount == 0:
                output[i] = total_product // output[i]
            elif zeroCount == 1:
                output[i] = total_product if output[i] == 0 else 0
            else:
                output[i] = 0

        return output
        
    
        