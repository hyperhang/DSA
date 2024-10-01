from math import sqrt

class Solution:
    def numSquares(self, n: int) -> int:
        if n <= 3:
            return n
        dp = [0] * (n+1)
        dp[1] = 1
        dp[2] = 2
        dp[3] = 3
        def fill_dp(i):
            if int(sqrt(i))*int(sqrt(i)) == i :
                dp[i] = 1 # i is a perfect square
                return
            mi = 1e8
            for k in range(1, int(sqrt(i))+1 ):
                mi = min(mi, dp[i - k*k] + 1)
            dp[i] = mi
        for i in range(4, n+1):
            fill_dp(i)
        for i in dp:
            print(i)
        return dp[n]
    
s = Solution()
n = 1
n = 4
n = 5
n = 12
n = 13
print("res = ", s.numSquares(n))