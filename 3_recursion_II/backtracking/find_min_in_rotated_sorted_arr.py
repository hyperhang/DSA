from typing import List


class Solution:
    smallest = 0
    def findMin(self, nums: List[int]) -> int:
        def seek(left, right):
            if left + 1 == right or left == right:
                # self.smallest = min(nums[left], nums[right])
                return  min(nums[left], nums[right])
            mid = (right + left)//2
            if nums[mid] > nums[left] > nums[right]:
                return seek(mid+1, right)
            elif nums[mid] < nums[right] < nums[left]:
                return seek(left+1, mid)
            elif nums[left] < nums[mid] < nums[right]:
                # self.smallest = nums[left]
                return nums[left]
            
            """
            0 1 2 3 4
            4 0 1 2 3
            2 3 4 0 1 
            """
        # seek(0, len(nums) - 1)
        return seek(0, len(nums) - 1)
    
sol = Solution()
nums = [3,4,5,1,2]
# nums = [4,5,6,7,0,1,2]
# nums = [11,13,15,17]
# nums = [17, 11,13,15]
print(sol.findMin(nums))