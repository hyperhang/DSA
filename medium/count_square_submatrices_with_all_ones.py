from typing import List

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        count = 0
        dp = [ [0]*n for _ in range(m)]
        for i in range(n):
            if matrix[0][i]:
                # count += 1
                dp[0][i] = 1
        for i in range(m):
            if matrix[i][0]:
                # count += 1
                dp[i][0] = 1
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] :
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
                    # count += dp[i][j]
        for i in range(m):
            for j in range(n):
                count += dp[i][j]
        return count
                    
"""
1 0 1 1 0 0
0 1 1 1 1 0
1 1 1 1 1 1
1 1 0 0 0 0


1 1 1 0 1 1 
1 1 1 1 1 1
1 1 0 1 1 1
1 1 1 1 1 1
1 1 1 1 1 1
1 1 1 1 1 1

"""
            
sol = Solution()
matrix = [
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
# matrix = [
#   [1,0,1],
#   [1,1,0],
#   [1,1,0]
# ]
print(sol.countSquares(matrix))