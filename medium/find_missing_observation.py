from typing import List


class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        su = mean*(len(rolls) + n)
        left = su - sum(rolls)
        if 1*n <= left <= 6*n:
            avg = left//n
            remain = left - avg*n
            res = [avg]*n
            i = 0
            while remain != 0:
                remain -= 1
                res[i] += 1
                i += 1
            return res
        else:
            return []

s = Solution()
rolls = [3,2,4,3]
mean = 4
n = 2

rolls = [1,5,6]
mean = 3
n = 4

rolls = [1,2,3,4]
mean = 6
n = 4

rolls = [1,1,2,4]
mean = 4
n = 4
print(s.missingRolls(rolls, mean, n))