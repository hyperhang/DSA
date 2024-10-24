from typing import List
import bisect

# class Solution:
#     def smallestRange(self, nums: List[List[int]]) -> List[int]:
#         bottom_range = []
#         top_range = []
#         for element in nums[0]: # O(K)
#             for i in range(1, len(nums)): # O(N)
#                 x = bisect.bisect_left(nums[i], element)
#                 if x == 0: # all nums[i] are greater or equal to element
#                     if len(bottom_range) == 0 :
#                         bottom_range = [[element, nums[i][0]]]
#                     else:
#                         for i in range(len(bottom_range)):
#                             bottom_range[i] = [bottom_range[i][0], max(bottom_range[i][1], nums[i][0])]
                        
#                     if len(top_range) == 0:
#                         top_range = [[element, nums[i][0]]]
#                     else:
#                         for i in range(len(top_range)):
#                             top_range[i] = [top_range[i][0], max(top_range[i][1], nums[i][0])]
#                 elif x >= len(nums) - 1:
#                     temp = nums[i][-1]
#                     if bottom_range:
#                         for i in range(len(bottom_range)):
#                             bottom_range[i] = [min(bottom_range[i][0], temp), bottom_range[i][1]]
#                     else:
#                         bottom_range = [[temp, element]]
#                     if top_range:
#                         for i in range(len(top_range)):
#                             top_range[i] = [min(top_range[i][0], temp), top_range[i][1] ]
#                     else:
#                         top_range = [[temp, element]]
#                 else:
#                     mid = nums[x]
#                     left = nums[x-1]
#                     right = nums[x+1]
#                     if mid == element:
                        

from sortedcontainers import SortedDict
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        current = SortedDict()
        for i, ar in enumerate(nums):
            current[ar[0]] = [i, 0] # row, col
        
        min_range = [-1e6,1e6]
        while True:
            min_ele, min_idx = current.peekitem(0)
            max_ele, max_idx = current.peekitem(-1)
            print(f"New sd: ", current)
            if max_ele - min_ele < min_range[1] - min_range[0] or (max_ele - min_ele == min_range[1] - min_range[0] and min_ele < min_range[0]):
                min_range = [min_ele, max_ele]
                print(f"New range: {min_range}, rows: [{min_idx[0]} - {max_idx[0]}]")
                
            if min_idx[1]+1 < len(nums[min_idx[0]]):
                current.popitem(0)
                current[ nums[min_idx[0]][min_idx[1]+1] ] = [min_idx[0], min_idx[1]+1 ]
            else:
                break
        return min_range

sol = Solution()
nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
nums = [[1,2,3],[1,2,3],[1,2,3]]

nums = [[-89,1,69,89,90,98],
 [-43,-36,-24,-14,49,61,66,69],
 [73,94,94,96],
 [11,13,76,79,90],
 [-40,-20,1,9,12,12,14],
 [-91,-31,0,21,25,26,28,29,29,30],
 [23,88,89],
 [31,42,42,57],
 [-2,6,11,12,12,13,15],
 [-3,25,34,36,39],
 [-7,3,29,29,31,32,33],
 [4,11,14,15,15,18,19],
 [-34,9,12,19,19,19,19,20],
 [-26,4,47,53,64,64,64,64,64,65],
 [-51,-25,36,38,50,54],
 [17,25,38,38,38,38,40],
 [-30,12,15,19,19,20,22],
 [-14,-13,-10,68,69,69,72,74,75],
 [-39,42,70,70,70,71,72,72,73],
 [-67,-34,6,26,28,28,28,28,29,30,31]]


print(sol.smallestRange(nums))

        
        