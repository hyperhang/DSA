class Solution:
    def arrayPairSum(self, nums: list[int]) -> int:
        nums.sort(reverse=True)
        
        res = 0
        print(nums)
        for i in range(1,len(nums),2):
            res += nums[i]
        return res
    
s = Solution()
nums = [6,2,6,5,1,2]
nums = [1,4,3,2]
print(s.arrayPairSum(nums))