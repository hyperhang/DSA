from typing import List


class Solution:
    # def maxScoreSightseeingPair(self, values: List[int]) -> int:
    #     start = values[0]
    #     s_i = 0
    #     end = values[1]
        
    #     ma = start + end - 1
    #     for i in range(1, len(values)):
    #         val = values[i]
    #         ori_start = start
    #         ori_start_i = s_i
    #         if val + ori_start + ori_start_i - i > ma : # set new: end, max val
    #             ma = val + ori_start + ori_start_i - i
               
    #         if - i + s_i + start < val: # set new : start & its idx
    #             start = val
    #             s_i = i
    #     return ma
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        start = values[0]
        s_i = 0
        end = values[1]
        
        ma = start + end - 1
        for i in range(1, len(values)):
            val = values[i]
            if val + start + s_i - i > ma : # set new: end, max val
                ma = val + start + s_i - i
            if - i + s_i + start < val: # set new : start & its idx
                start = val
                s_i = i
        return ma

s = Solution()
values = [8,1,5,2,6] # 11
values = [1,2]  # 2
# values = [1,3,5] # 7
values = [1,3,5, 5] # 9
print(s.maxScoreSightseeingPair(values))