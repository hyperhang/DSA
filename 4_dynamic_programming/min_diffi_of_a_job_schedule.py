class Solution:
    def minDifficulty(self, jobDifficulty: list[int], d: int) -> int:
        jobDifficulty = [6,5,4,3,2,1]
        d = 2
        
        jobDifficulty = [186,398,479,206,885,423,805,112,925,656,16,932,740,292,671,360]
        d = 4
        # dp[5, 1] -> dp[4,0] , dp [3,0], d[2,0], dp[1,0], dp[0][0]
        jD_len = len(jobDifficulty)
        # dp = [[0]*jD_len]*d # [jobDiffi_idx, day]
        dp = [[0 for _ in range(d)] for _ in range(jD_len)]
        print("Init: \n",dp)
        if jD_len < d:
            print("res: -1")
            return -1
        
        def find(idx, day_idx):
            print(f"------\nCALLING Find: {idx}, {day_idx}")
            # base case: 
            if day_idx == 0:
                print("dp :", dp)

                dp[idx][day_idx] = max(jobDifficulty[:idx+1])
                print("d = 0")
                print("dp :", dp)
                return
            if idx == day_idx:
                print("idx == day_idx == ", day_idx)
                s = 0
                for ele in jobDifficulty[:day_idx+1]:
                    s += ele
                dp[idx][day_idx] = s
                print("dp: ", dp)
                return 

            _min = 100000000
            print(f"i in range: {day_idx-1}, {idx}")
            for i in range(day_idx-1, idx):
                print("i: ", i)
                if dp[i][day_idx-1] == 0 :
                    find(i, day_idx-1)
                _tem = dp[i][day_idx-1] + max(jobDifficulty[i+1:jD_len])
                _min = min(_min, _tem)
            print(f"Assigning: dp[{idx}][{day_idx}] = {_min}")
            dp[idx][day_idx] = _min
            return        
        
        find(jD_len-1, d-1)
        print("---\nFinal dp: ", dp)
        print("RESULT: ", dp[jD_len-1][d-1])
        return dp[jD_len-1][d-1]
        
s = Solution()
k = s.minDifficulty(None, None)
print("final: ", k)