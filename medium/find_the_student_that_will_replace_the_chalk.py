from typing import List


class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        su = 0
        for c in chalk:
            su += c
        k = k%su
        i = 0
        print("init k = ", k)
        for i, c in enumerate(chalk):
            if k >= c:
                k = k - c
            else:
                break
        return i
    
s = Solution()

chalk = [5,1,5]
k = 22

chalk = [3,4,1,2]
k = 25

print(s.chalkReplacer(chalk, k))