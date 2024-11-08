from typing import List
import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = [nums[0]]
        for ele in nums[1:]:
            if ele > sub[-1]:
                sub.append(ele)
            else:
                idx = bisect.bisect_left(sub, ele)  
                sub[idx] = ele
            print(sub)
        return len(sub)
    
sol = Solution()
nums = [2,2,7,8,3,7,4,1, 5,7]
print(sol.lengthOfLIS(nums))
