from typing import List


class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        count_remainder = [0]*k
        for ele in arr:
            count_remainder[ele % k] += 1
        if count_remainder[0] % 2 == 1:
            return False
        for i in range(1,k):
            if count_remainder[i] != count_remainder[k-i]:
                return False
        return True
    
        