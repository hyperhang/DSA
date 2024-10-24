from typing import List

# # TLE
# class Solution:
#     def maxWidthRamp(self, nums: List[int]) -> int:
#         n = len(nums)
#         indices = [i for i in range(n)]

#         # Sort indices based on corresponding values in nums and ensure stability
#         indices.sort(key=lambda i: (nums[i], i))
#         print("sorted indices: ", indices)

#         min_index = n  # Minimum index encountered so far
#         max_width = 0

#         # Calculate maximum width ramp
#         for i in indices:
#             max_width = max(max_width, i - min_index)
#             min_index = min(min_index, i)

#         return max_width
    
    
    
class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = [0]
        for i in range(1, len(nums)):
            if nums[i] < nums[stack[-1]]:
                stack.append(i)
        print("stack: ", stack)
        max_ramp = 0
        for i in range(len(nums)-1,-1,-1):
            while len(stack) > 0 and nums[i] >= nums[stack[-1]]:
                max_ramp = max(max_ramp, i - stack[-1] )
                stack.pop()
        return max_ramp
            
    # TC
    # SC
    
sol = Solution()

nums = [7,4,9]
nums = [6,0,8,2,1,5,4,7,1,1]
# nums = [6,0,8,2,1,5]
print("ans = ", sol.maxWidthRamp(nums))

