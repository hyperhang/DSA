from typing import List
from sortedcontainers import SortedDict
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], __k: int) -> List[int]:
        ar = dict()
        for num in nums:
            if num in ar:
                ar[num] += 1
            else:
                ar[num] = 1
        reverse = SortedDict()
        for k, v in ar.items():
            if v in reverse.keys():
                reverse[v].append(k)
            else:
                reverse[v] = [k]
        ans = []
        for k, v in reverse.items()[::-1]:
            ans += v
            if len(ans) == __k:
                return ans
        
        heapq.nlargest(5, )
        
sol = Solution()
nums = [1,1,1,2,2,2,3]
k = 2
print(sol.topKFrequent(nums, k))
        
