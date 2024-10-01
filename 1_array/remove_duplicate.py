class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        start = 0
        end = 1
        if len(nums) == 2 :
            if nums[start] == nums[end]:
                return 1
            else:
                return 2
        while end < len(nums):
            while end < len(nums) and nums[end] == nums[start]:
                end += 1
            if end == len(nums):
                print(start+1)
                return start+1
            # swap value at end and value at start+1
            nums[start+1], nums[end] = nums[end], nums[start+1]
            start += 1
            end += 1
        
        print(nums)
        print(start+1)
        return start+1
            
        
a = [0,0,0,1,1,1,2,2,3,3,4,5]
s= Solution()
s.removeDuplicates(a)