from typing import List


class Solution:
    def maxGoodNumber(self, nums: List[int]) -> int:
        def to_bin(x:int):
            b = ""
            while x != 0:
                b = str(x&1) + b
                x = x >> 1
            return b
        def to_int(s: str):
            res = 0
            for c in s:
                res = res*2 + int(c)
            return res
                
        x1 = to_bin(nums[0])
        x2 = to_bin(nums[1])
        x3 = to_bin(nums[2])
        ma = max(x1+x2+x3, x1+x3+x2, x2+x1+x3, x2+x3+x1, x3+x2+x1, x3+x1+x2)
        print(ma)
        print(to_int(ma))
        return to_int(ma)

sol = Solution()
num = [2,8,16]
# num = [1,2,3]

sol.maxGoodNumber(num)