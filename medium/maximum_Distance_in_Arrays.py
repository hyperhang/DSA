from typing import List

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        can = []
        rvrs = []
        for idx, ar in enumerate(arrays):
            can.append([ar[0], idx ])
        for idx, ar in enumerate(arrays):
            rvrs.append([ar[-1], idx ])
        can = sorted(can)
        rvrs = sorted(rvrs, reverse=True)
        min1, min_idx1 = can[0][0], can[0][1]
        min2, min_idx2 = can[1][0], can[1][1]
        max1, max_idx1 = rvrs[0][0], rvrs[0][1]
        max2, max_idx2 = rvrs[1][0], rvrs[1][1]
        if min_idx1 != max_idx1:
            return abs(max1 - min1)
        else:
            return max(abs(max2-min1), abs(max1-min2))
            
class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        ans = 0
        vmin, vmax = float('inf'), -float('inf')
        for arr in arrays:
            ans = max(ans, vmax - arr[0], arr[-1] - vmin)
            vmin = min(vmin, arr[0])
            vmax = max(vmax, arr[-1])
        return ans
    
# 3,7   4,9  4,11,   5, 8