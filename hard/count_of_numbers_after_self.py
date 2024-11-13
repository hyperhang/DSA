from typing import List
from sortedcontainers import SortedDict

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        nums = nums[::-1]
        new_nums = SortedDict()
        for ele in nums:
            new_nums[ele]
        