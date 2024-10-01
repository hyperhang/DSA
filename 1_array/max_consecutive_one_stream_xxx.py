# 4 0 3 0 6  0 1 0 0 3 0 0 0 0 6 
#   5 8 4 10 7 8 2 1 4 4 1 1 1 7

class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        i = 0
        num_con_one = 0
        while i < len(nums) :
            if nums[i] == 1 :
                num_con_one += 1
            if nums[i] == 0 :
                
        # check có bnhieu số 1 liên tiếp tại vị trí i
        # update max_con_one tại i
        # update max one overall