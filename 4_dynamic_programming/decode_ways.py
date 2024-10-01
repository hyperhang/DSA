class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0]*len(s)
        if s[0] == "0":
            dp[0] = 0
        else:
            dp[0] = 1
        for i in range(1, len(s)):
            print("i: ", i)
            ways = 0
            # lay 1 chu so cuoi:
            if s[i] != "0" and dp[i-1] != 0:
                ways += dp[i-1]
                print("get last 1 digit")

            # lay 2 chu so cuoi
            _n = int(s[i-1:i+1])
            if 10 <= _n and _n <= 26 :
                if i-2 < 0 or dp[i-2] != 0:
                    ways = ways + dp[i-2] if i-2 >= 0 else ways + 1
                    print("get last 2 digits")
            dp[i] = ways 
        print(dp)   
        return dp[len(dp)-1] 
s = Solution()
st = "12"
s.numDecodings(st)                    
                    
        