class Solution:
    def merge(self, intervals: list) -> list:
        intervals.sort(key = lambda interval: interval[0])
        print(intervals)
        non_overlapping_intervals = [intervals[0]]
        for i in range(1, len(intervals)):
            print("--")
            print(f"{intervals[i-1][1]} >= {intervals[i][0]} >= {intervals[i-1][0]} ?")
            if non_overlapping_intervals[len(non_overlapping_intervals)-1][1] >= intervals[i][0] >= non_overlapping_intervals[len(non_overlapping_intervals)-1][0]:
                merged_interval = [non_overlapping_intervals[len(non_overlapping_intervals)-1][0], max(non_overlapping_intervals[len(non_overlapping_intervals)-1][1], intervals[i][1]) ]
                print("merge_interval: ", merged_interval)
                non_overlapping_intervals[len(non_overlapping_intervals)-1] = merged_interval
            else:
                non_overlapping_intervals.append(intervals[i])
            print("temp: ", non_overlapping_intervals)
        print(non_overlapping_intervals)
        return non_overlapping_intervals

s = Solution()
# s.merge(intervals = [[1,3],[2,6],[8,10],[15,18]])
# s.merge(intervals = [[1,4],[4,5]])
# s.merge(intervals = [[1,4]])
# s.merge(intervals = [[1,4], [2,3], [0,1]])
s.merge(intervals = [[1,2],  [0,1], [-3, -2], [20,31],])
