from typing import List


class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        """
        2,3,4,6,8,16
        """
        longest = 0
        i = 0
        dup = [0]*(max(nums)+1)
        for ele in nums:
            dup[ele] = 1
        while i < len(dup):
            j = i
            max_length = 0
            if dup[j]:
                max_length += 1
                dup[j] = 0
                while j**2 < len(dup) and dup[j**2]:
                    j = j**2
                    dup[j] = 0
                    max_length += 1
            longest = max(longest, max_length)
            i += 1
        return longest if longest != 1 else -1
        # TC: O(max(nums))
        # SC: O(max(nums))
        
sol = Solution()
nums = [4,3,6,16,8,2]
nums = [2,3,5,6,7]
nums = [2]

print(sol.longestSquareStreak(nums))
                    