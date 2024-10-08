"""
[3,1,4,2].  p=6. s=10 -> %p  -> 4 or -2.
Tìm subarray có độ dài ngắn nhất sao cho tổng chia 6 dư 4 (-2)

3,4,8,10
3,4,2,4

0 -> 4
1 -> 5 
2 -> 0
3 -> 1
4 -> 2
5 -> 3


2,1,4,4,0,3,3,1,4,5,2,1

2: [0,       (need 4)
1: [1,7.  => found 3 with idx 6, t = 7 - 6 =1        (need 3)
4: [2, 3, 8 => found 0 with idx 4, t = 8 - 4=4,     (need 0)
0: [4,       => found 2 with idx 0, t = 4-0=4   (need 2)
3: [5,6,        (need 5)
5: [9,    => found 1 with idx 7, t = 9 - 7=2.   (need 1
"""
from typing import List
class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        prefix_sum = [0]
        for i in range(len(nums)):
            prefix_sum.append((prefix_sum[-1] + nums[i])%p)
        
        k = prefix_sum[-1] % p # k: remainder of sum % p
        idx = {}
        t = 1e6
        for i, ele in enumerate(prefix_sum):
            idx[ele] = i
            need = (ele - k + p) % p 
            if need in idx:
                last_idx = idx[need]
                t = min(t, i - last_idx)
        if t == len(nums):
            return -1
        return t
        
sol = Solution()
nums = [3,1,4,2]
p = 6

nums = [6,3,5,2]
p = 9

nums = [1,2,3]
p = 3

print(sol.minSubarray(nums, p))
            
            
        
            