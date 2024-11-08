from typing import List


class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        left_less_count = [0]
        for idx in range(1, len(nums)):
            max_left = 0
            for i in range(idx):
                if nums[idx] > nums[i]:
                    max_left = max(max_left, left_less_count[i]+1)
            left_less_count.append(max_left)
        
        print(f"left less count: {left_less_count}")
        
        right_less_count = [0]*len(nums)
        for idx in range(len(nums)-2, -1 , -1):
            max_right = 0
            for i in range(idx+1, len(nums)):
                if nums[idx] > nums[i]:
                    max_right = max(max_right, right_less_count[i]+1)
            right_less_count[idx] = max_right
        print(f"right less count: {right_less_count}")
        
        max_length = 0
        for i in range(1,len(nums)-1):
            if left_less_count[i] != 0 and right_less_count[i] != 0:
                max_length = max(left_less_count[i] + right_less_count[i], max_length)
        
        return len(nums) - (max_length + 1)
            
            
        
sol = Solution()
nums = [2,1,1,5,6,2,3,1]
nums = [1,3,1]
nums = [100,92,89,77,74,66,64,66,64]
print(sol.minimumMountainRemovals(nums))
                 
        