from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = 0
        max_sum = 0
        
        for ele in nums:
            if ele + max_sum > 0:
                max_sum = max_sum + ele
            else:
                max_sum = 0
            
            ans = max(ans, max_sum)    
        
        if ans > 0:
            return ans
        return max(nums)         
        
sol = Solution()
nums = [-2,1,-3,4,-1,2,1,-5,4]
nums = [1]
nums = [5,-4,-1,7,8]
# nums = [-5,-4,-3,-7,-8]
nums = [-1,1,2,1]

print(sol.maxSubArray(nums))
