class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        left_sum = [0]
        right_sum = [0]*len(nums)
        for i in range(1, len(nums)):
            left_sum.append( left_sum[len(left_sum)-1] + nums[i-1] )
        for i in range(len(nums)-2, -1, -1):
            right_sum[i] = right_sum[i+1] + nums[i+1]
        print("Left sum:  ", left_sum)
        print("Right sum: ", right_sum)
        for i in range(0, len(nums)):
            if left_sum[i] == right_sum[i] :
                return i
        return -1   
        
# nums = [1,7,3,6,5,6]
# nums = [1,2,3]
# nums = [2,1,-1]
# nums = [0]
# nums = [1]
nums = [ 1, 1]
s = Solution()
print(s.pivotIndex(nums))