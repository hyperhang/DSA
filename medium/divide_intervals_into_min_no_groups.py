from typing import List
import heapq

class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals)
        last_idxes = [intervals[0][1]]
        for left, right in intervals[1:]:
            if left > last_idxes[0]:
                heapq.heappop(last_idxes)
            heapq.heappush(last_idxes, right)
        return len(last_idxes)
        
        
sol = Solution()
intervals = [[5,10],[6,8],[1,5],[2,3],[1,10]]
intervals = [[1,3],[5,6],[8,10],[11,13]]

print(sol.minGroups(intervals))