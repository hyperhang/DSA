from typing import List


class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        
        def get_no_set_bits(num:int):
            c = 0
            while num:
                if num & 1:
                    c += 1
                num = num >> 1
            return c
                
        sorted_nums = sorted(nums)
        ordered_set = []
        previous_setbits = 0
        for num in sorted_nums:
            no = get_no_set_bits(num)
            if no == previous_setbits:
                ordered_set[-1].add(num)
            else:
                ordered_set.append(set([num]))
                previous_setbits = no
        print(ordered_set)
        i = 0
        cur_set = ordered_set[i]
        for n in nums:
            if n not in cur_set:
                i += 1
                if i >= len(ordered_set):
                    return False
                cur_set = ordered_set[i]
                if n not in cur_set:
                    return False
        return True
        # TC: O(N.log N)
        # SC: O(N)

sol = Solution()
nums = [8,4,2,4,2,30,15]
nums = [1,2,3,4,5]
nums = [1,2,2,2,3,4,5]
# nums = [3,16,8,4,2]
# nums = [3,16,8,4,2,2]
# nums = [2,28,9]
print(sol.canSortArray(nums))            
        
        