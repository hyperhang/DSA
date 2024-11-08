
import collections
from typing import List


class Solution(object):
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        dp = collections.Counter([0])
        for num in nums:
            temp = collections.Counter()
            for k, v in dp.items():
                temp[k | num] += v
            dp = dp + temp
            print("new temp: ")
            print(dp)
            print()
        return dp[max(dp)]
    

nums = [10, 5, 4, 6]
sol = Solution()
sol.countMaxOrSubsets(nums)
