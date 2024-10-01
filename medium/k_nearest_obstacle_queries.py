from typing import List
import heapq

class Solution:
    def resultsArray(self, queries: List[List[int]], k: int) -> List[int]:
        hq = []
        res = [-1]*len(queries)
        
        if k > len(queries) :
            return res
        
        for i in range(k):
            x, y = queries[i]
            heapq.heappush(hq, -(abs(x) + abs(y)))
            
        tem = -hq[0]
        res[k-1] = tem
        
        for i in range(k, len(queries)):
            current_max = -hq[0]
            x, y = queries[i]
            val = abs(x) + abs(y)
            print(f"i = {i}, current max = {current_max}, new val = {val}")
            if val < current_max:
                current_max = val
                heapq.heappop(hq)
                heapq.heappush(hq, -val)
            res[i] = -hq[0]
        return res
    
s = Solution()

queries = [[1,2],[3,4],[2,3],[-3,0]]
k = 2

queries = [[5,5],[4,4],[3,3]]
k = 1

queries = [[-7,-1]]
k = 3

queries = [[6,10],[0,-10],[2,-6]]
k = 2
print(s.resultsArray(queries, k))                
            