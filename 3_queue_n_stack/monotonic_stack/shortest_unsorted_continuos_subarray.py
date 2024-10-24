from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        # 17,34,52,43,23,26,32
        # 
        # 17,23,26,32,34,43,52
        # 
        sorted_num = sorted(nums)
        i, j = 0, len(nums) - 1
        while i < len(nums):
            if sorted_num[i] == nums[i]:
                i += 1
            else:
                break
        while j > -1:
            if sorted_num[j] == nums[j]:
                j -= 1
            else:
                break
        return j-i+1 if j>i else 0
    
sol = Solution()
nums = [2,6,4,8,10,9,15]
nums = [1,2,3,4]
nums = [1]
nums = [2,4,7,6,15]
print(sol.findUnsortedSubarray(nums))

            