from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        if target % 2 == 1:
            return False
        target = target // 2
        m = target+1
        n = len(nums)
        dp = [[0]*m for _ in range(n)]
        if nums[0] < m:
            dp[0][nums[0]] = 1
        for i in range(n):
            dp[i][0] = 1 # luon ton tai day con 0...i sao cho tong = 0
       
        for i in range(1,n):
            for j in range(1,m):
                # if dp[i][j] is 1 -> 
                # if nums[j] is taken or not taken:
                # print("j - nums[i] > 0 ? ", j - nums[i] , " > 0 ?")
                  
                if  dp[i-1][j] == 1 or (j - nums[i] > 0 and dp[i-1][j - nums[i]] == 1):
                    dp[i][j] = 1
                # else: dp = 0
        for i in range(n):
            print(dp[i])
        return dp[n-1][m-1] == 1
                    
                
        # dp[i][j]: True or False if there is a sub set from 0..i having sum = j (max_j=m, max_i=n)
        # 
    
s = Solution()
nums = [1,5,11,5]
nums = [1,2,3,5]
nums = [1,2,3]
nums = [1,2,1]
nums = [3,5,5,7,9,12,17,20] # true, 5,5,9,20
nums = [3,5,5,7,9,11] # True, 5,5,9,11
nums = [23,13,11,7,6,5,5] # True, 23,7,5
nums = [9,5]
# nums = [5,9]
print(sum(nums))
print(s.canPartition(nums))            