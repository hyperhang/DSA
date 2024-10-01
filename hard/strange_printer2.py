class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        dp = [ [1]*n for _ in range(n)]
        if n == 1:
            return 1
        
        def fill_dp(start: int, windows: int, s: str):
            end = start+windows-1
            # print(f"---\nstart={start}, end={end}, windows={windows}")
            minn = dp[start][end-1]+1
            for i in range(start, end):
                if s[i] == s[end]:
                    if i == start :
                        if minn > dp[start][end-1]:
                            # print(f'min = {minn} > dp[{start}][{end}] = {dp[start][end]}')
                            minn = dp[start][end-1]
                            
                    elif minn > dp[start][i-1]+dp[i][end-1]:
                        # print(f'minn = {minn} > dp[{start}][{i-1}] + dp[{i}][{end-1}] = {dp[start][i-1]+dp[i][end-1]}')
                        minn = dp[start][i-1]+dp[i][end-1]
            dp[start][end] = minn
            # print(f"dp[{start}][{end}] = {dp[start][end]}")
                
        for windows in range(2, n+1):
            # print("===================")
            for start in range(0,n-windows+1):
                fill_dp(start, windows, s)
        # print("res: ", dp[0][n-1])
        return dp[0][n-1]        
            
        
s = Solution()
#      01234
input='aabbbbbb'

input='aaaab'
input='ab'
# input='a'

input='aaabbcddeadeabaa'

# #      01234
# input='ababc' # 4

input= "adbccbbcdddddcaccddddcbbccbbbbcdacbcbccdcbbdcddabb"
input= "adbccbbcdddddcaccddddcbbccbbbbcdacbcbccdcbbdcdda"
input= "adbccbbcdddddcaccddddcbbccbbbbcdacbcbccdcbbdcdd"
input= "adbccbbcdddddcaccddddcbbccbbbbcdacbcbccdcbbdcd"
# input ='adbccbbcdddddc'
print(s.strangePrinter(input))