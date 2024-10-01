from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ma = max(nums)
        i = 0
        max_count = 0
        while i < len(nums):
            count = 0
            if nums[i] == ma:
                while i < len(nums) and  nums[i] == ma :
                    count += 1
                    i += 1
            max_count = max(max_count, count)
            i += 1
        return max_count

s = Solution()
nums = [1,3,5,5,5, 3,5,0]
nums = [0]*1000
print(s.longestSubarray(nums))