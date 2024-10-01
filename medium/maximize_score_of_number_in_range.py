from typing import List


class Solution:
    def maxPossibleScore(self, start: List[int], d: int) -> int:
        start = sorted(start)
        n = len(start)
        mi = start[0]
        ma = start[-1] + d
        avg = (ma - mi)//(n-1)
        default = [mi]
        for i in range(1,n):
            val = default[-1] + avg
            default.append(val)
        print("default: ", default)
        res = [0]*n
        res[0] = mi
        for i in range(1, n):
            last_val = start[i-1]
            exp = last_val + d
            for ele in range(start[i], start[i]+d+1):
                if ele >= exp:
                    res[i] = ele
        print("Res:", res)
        distance = res[1] - res[0]
        for i in range(1, len(res)):
            distance = min(distance, res[i]-res[i-1])
        print("OUTPUT: ", distance)
        return distance

s= Solution()
start = [6,0,3]
d = 2          

start = [2,6,13,13]
d = 5  

s.maxPossibleScore(start, d)

        
# [0, 3, 6]
# 0-2, 3-5, 6-8
# 0->8 chia lam 2 phan: avg = 4

# [2,6,13,13], d = 5
# 2 -> 18 chia lam 3 phan, avg = 5: 2 - 7 - 12 - 17

