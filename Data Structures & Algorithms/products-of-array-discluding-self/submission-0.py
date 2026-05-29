class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_sum, suffix_sum = [1] * (n + 1), [1] * (n + 1)
        result = []

        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] * nums[i]
            suffix_sum[n - i - 1] = suffix_sum[n - i] * nums[n - 1 - i]
         
        for i in range(n):
            result.append(prefix_sum[i] * suffix_sum[i + 1])
        
        return result




        


        