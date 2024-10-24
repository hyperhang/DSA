from typing import List
import heapq
import math

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        hq = []
        for ele in nums:
            heapq.heappush(hq, -ele)
        score = 0
        while k:
            t = -heapq.heappop(hq)
            score += t
            heapq.heappush(hq, -math.ceil(t/3))
            k -= 1
        return score
    
sol = Solution()
nums = [10,10,10,10,10]
k = 5

nums = [1,10,3,3,3]
k = 3

print(sol.maxKelements(nums, k))
            