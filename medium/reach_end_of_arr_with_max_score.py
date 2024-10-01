from typing import List


class Solution:
    def findMaximumScore(self, nums: List[int]) -> int:
        ma = nums[0]
        idx = 0
        su = 0
        for i in range(1, len(nums)-1):
            if ma < nums[i]:
                su += (i-idx)*ma
                ma = nums[i]
                idx = i
        su += ma*(len(nums)-1-idx)
        return su
    
s = Solution()
nums = [1,3,1,5]
nums = [4,3,1,3,2]
nums = [4,8]
print(s.findMaximumScore(nums))
            