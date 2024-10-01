from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m = len(points)
        n = len(points[0])
        dp = [ [0]*n for _ in range(m)]
        for i in range(n):
            dp[0][i] = points[0][i]
        for i in range(1, m):
            max_left = [0]*n
            max_right = [0]*n
            max_left[0] = dp[i-1][0]
            max_right[-1] = dp[i-1][-1]
            for k in range(1,n):
                max_left[k] = max(max_left[k-1] - 1, dp[i-1][k])
            for k in range(n-2, -1, -1):
                max_right[k] = max(max_right[k+1] - 1, dp[i-1][k])
            for j in range(n):
                dp[i][j] = points[i][j] + max(max_left[j], max_right[j])
                
        res = 0
        for i in range(m):
            print(dp[i])
        for i in range(n):
            res = max(res, dp[m-1][i])
        return res

s= Solution()
points = [[1,2,3],[1,5,1],[3,1,1]] #9
points = [[1,5],[2,3],[4,2]] # 11
print(s.maxPoints(points))

