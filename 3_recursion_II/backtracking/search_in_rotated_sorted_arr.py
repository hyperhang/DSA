from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def seek(left, right):
            mid = (left+right)//2
            if left == right :
                if nums[left] == target:
                    return left
                else:
                    return -1
            if left + 1 == right:
                if nums[left] == target:
                    return left
                if nums[right] == target:
                    return right
                return -1
            if nums[left] > nums[right] > nums[mid]:
                # 6 7 0 1 2 3 4 5
                if nums[mid] <= target and nums[right] >= target:
                    return seek(mid, right)
                else:
                    return seek(left, mid)
            elif nums[mid] > nums[left] > nums[right]:
                # 2 3 4 5 6 7 0 1 
                if nums[left] <= target <= nums[mid]:
                    return seek(left, mid)
                else:
                    return seek(mid, right)
            else: # nums[left] < nums[mid] < nums[right]
                if nums[mid] <= target:
                    return seek(mid, right)
                else:
                    return seek(left, mid-1)
                
        return seek(0, len(nums)-1)
    
sol = Solution()

nums = [4,5,6,7,0,1,2]
target = 0

# nums = [4,5,6,7,0,1,2]
# target = 3

# nums = [1]
# target = 0

nums = [5,1,3]
target = 5
print(sol.search(nums, target))