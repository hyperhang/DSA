from typing import List

class Solution:
    def print_matrix(self, m: list[list]):
        l = len(m)
        for i in range(l):
            print(m[i])
        print('\n')
            
    def maximumSubarrayXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        dp  =    [ [0]*n for _ in range(n) ]
        max_xor = [ [0]*n for _ in range(n) ]
        xor =  [ [0]*n for _ in range(n) ]
        
        for i in range(n):
            xor[i][i] = nums[i]
            # 1 2 3 4 5
            
        for window in range(2, n+1, 1):
            for i in range(0, n-window+1):
                j = i + window - 1 # e.g : i, j = 0, 1
                xor[i][j] = xor[i][j-1]^xor[i+1][j]
        print("xor: ")
        self.print_matrix(xor)
        
        for i in range(n-1,-1,-1):
            max_xor[i][i] = xor[i][i]
            for j in range(i-1, -1,-1): # i = 7, j : 6->0
                max_xor[j][i] = max(xor[j][i], max_xor[j+1][i])
        print("max xor: ")
        self.print_matrix(max_xor)      
          
        for i in range(n):
            dp[i][i] = nums[i]
            for j in range(i+1, n):
                dp[i][j] = max(dp[i][j-1], max_xor[i][j])       
        
        res = []
        for q in queries:
            res.append(dp[q[0]][q[1]])
        return res

s = Solution()

nums = [2,8,4,32,16,1]
queries = [[0,2],[1,4],[0,5]] # [12,60,60]

nums = [0,7,3,2,8,5,1]
queries = [[0,3],[1,5],[2,4],[2,6],[5,6]] # [7,14,11,14,5]


print(s.maximumSubarrayXor(nums, queries))
