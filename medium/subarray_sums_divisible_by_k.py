from typing import List
from collections import defaultdict

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix = [0]
        for ele in nums:
            prefix.append((prefix[-1] + ele)%k)
        freq = defaultdict(int)
        for ele in prefix:
            freq[ele] += 1
        s = 0
        for k,v in freq.items():
            if v > 1:
                s += v*(v-1)//2
        return s
        # TC: O(n+k). SC: O(k)
        
            
sol = Solution()
nums = [4,5,0,-2,-3,1]
k = 5

nums = [5]
k=9

print(sol.subarraysDivByK(nums, k)        )            