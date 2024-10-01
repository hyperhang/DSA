from typing import List


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        updated_time = []
        for t in timePoints:
            h = int(t[:2])
            m = int(t[3:])
            updated_time.append(h*60+m)
        updated_time.sort()
        add_time = []
        for t in updated_time:
            add_time.append(t+24*60)
        total_time = updated_time + add_time
        print("sorted:  ", updated_time)
        print("added :  ", total_time)
        min_diff = 300000
        for i in range(1,len(total_time)):
            min_diff = min(total_time[i]-total_time[i-1], min_diff)
        print("RES: ", min_diff)
        return min_diff

s = Solution()
timePoints = ["23:59","00:00"]
timePoints = ["00:00","23:59","00:00"]
s.findMinDifference(timePoints)