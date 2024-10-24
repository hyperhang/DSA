from typing import List
from collections import defaultdict
import heapq

class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        in_vertices = defaultdict(list)
        out_vertices = dict() 
        maxrange = 0
        for arrival, leave in times:
            out_vertices[arrival] = leave
            in_vertices[leave].append(arrival)
            maxrange = max(maxrange, leave)
        hq = []
        current = set()
        seat = defaultdict(int)
        
        for i in range(1, maxrange+1):
            if i in in_vertices :
                for arrive in in_vertices[i]:
                    current.remove(seat[arrive])
                    heapq.heappush(hq, seat[arrive])
            if i in out_vertices:
                if len(hq) == 0:
                    seat[i] = len(current)
                    current.add(seat[i])
                else:
                    seat[i] = hq[0]
                    current.add(seat[i])
                    heapq.heappop(hq)
                    
        return seat[times[targetFriend][0]]
    
    
class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        target_arrival = times[targetFriend][0]
        times = sorted(
            [
                (arrival, leave, index)
                for index, (arrival, leave) in enumerate(times)
            ]
        )
        next_chair = 0
        available_chairs = []
        leaving_queue = []

        for time in times:
            arrival, leave, index = time
            while leaving_queue and leaving_queue[0][0] <= arrival:
                _, chair = heapq.heappop(leaving_queue)
                heapq.heappush(available_chairs, chair)

            if available_chairs:
                current_chair = heapq.heappop(available_chairs)
            else:
                current_chair = next_chair
                next_chair += 1
            heapq.heappush(leaving_queue, (leave, current_chair))
            if index == targetFriend:
                return current_chair

        return 0    
    
    
    
sol = Solution()

times = [[1,4],[2,3],[4,6]]
targetFriend = 1

times = [[3,10],[1,5],[2,6]]
targetFriend = 0
print(sol.smallestChair(times, targetFriend))