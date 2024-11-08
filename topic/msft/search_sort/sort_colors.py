from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 0 0 0 0 0 1 1 1 1 1 2 2 2
        # 0 0 0 0 0 1 1 1 1 1 2 2 2
        # 0 0 0 0 1 1 1 1 0 2 2 2 2
        start, end = 0, len(nums) - 1
        while nums[start] == 0:
            start += 1
        while nums[end] == 2:
            end -= 1
        i = start
        print(f"start: {start}, end: {end}")
        while i <= end:
            if nums[i] == 0:
                nums[i], nums[start] = nums[start], 0
                start += 1
                i += 1
            elif nums[i] == 2:
                nums[i], nums[end] = nums[end], 2
                end -= 1
            else:
                i += 1

        return nums

sol = Solution()
nums = [2,0,2,1,1,0]
nums = [0,0,2,1,1,2]
nums = [0,0,2,0,2,1,1,0,0,2,1,1]
# nums = [0,0,0,1,1,1,1,0,0,2,2,2]
print(sol.sortColors(nums))
                