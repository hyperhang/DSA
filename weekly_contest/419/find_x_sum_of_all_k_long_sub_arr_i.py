from typing import List
from collections import defaultdict
from sortedcontainers import SortedDict

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        def is_in_top_k(sd, key, k):
            # Get the index of the key
            index = sd.index(key)

            # Check if it's in the top K
            return len(sd) - index <= k

        # find freq of first k elements
        freq = defaultdict(int)
        key_dict = dict()
        for i in range(k):
            freq[nums[i]] += 1
        for key, val in freq.items():
            key_dict[val] = key
        # build AVL tree (SortedDict) with k elements values: 
        # key-val, 
        
        # track top_x, and sum_x elements
        
        # for a new ele :
        # update freq, key_dict, AVL tree, top_x, sum_x
        
sol = Solution()
nums = [1,1,2,2,3,4,2,3]
k = 6
x = 2

nums = [3,8,7,8,7,5]
k = 2
x = 2

nums = [2,1]
k = 1
x = 1

print(sol.findXSum(nums, k, x))