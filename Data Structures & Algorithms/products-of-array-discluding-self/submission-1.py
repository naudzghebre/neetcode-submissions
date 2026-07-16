class Solution:

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = len(nums) * [1]

        pre = 1
        for i in range(len(nums)):
            output[i] = pre
            pre *= nums[i]

        post = 1
        for j in range(len(nums) - 1, -1, -1):
            output[j] *= post
            post *= nums[j]

        return output
        

    
    # This solution works but uses the // operator
    # def productExceptSelf(self, nums: List[int]) -> List[int]:
    #     total_product, zeroCount, output = 1, 0, nums
    #     for n in nums:
    #         if n == 0:
    #             zeroCount += 1
    #         else:
    #             total_product *= n

    #     for i in range(len(output)):
    #         if zeroCount == 0:
    #             output[i] = total_product // output[i]
    #         elif zeroCount == 1:
    #             output[i] = total_product if output[i] == 0 else 0
    #         else:
    #             output[i] = 0

    #     return output
        
    
        