from typing import List


# class Solution:

        
#     def largestNumber(self, nums: List[int]) -> str:
            
#         def is_greater(s1, s2):
#             if len(s1) == len(s2):
#                 return s1 > s2
            
#             x = s1 if len(s1) < len(s2) else s2
#             y = s1 if len(s1) > len(s2) else s2
            
#             flag = x == s1
#             # print("flag: ", flag)
#             if x == y[:len(x)]:
#                 # print(f"{y} contains {x}")
#                 if y[len(x)] < x[0]:
#                     return flag
#                 elif y[len(x)] > x[0]:
#                     return not flag
#                 else:
#                     if flag:
#                         return is_greater(x[1:], y[1:])    
#                     else:
#                         return is_greater(y[1:], x[1:])  
#             else:
#                 return x > y if flag else x < y
        
#         ar = [str(i) for i in nums]
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
#                 if not is_greater(ar[i], ar[j]):
#                     t = ar[i]
#                     ar[i] = ar[j]
#                     ar[j] = t
#         ans = ""
#         for e in ar:
#             ans += e
                    
#         # print(f"8347 is greater than 83472: ", is_greater("8347", "83472"))
#         # print(f"8347  is greater than 83479: ", is_greater("8347", "83479"))
#         # print(f"555591  is greater than 55559155: ", is_greater("555591", "55559155"))
#         # print(f"39  is greater than 9: ", is_greater("39", "9"))
#         # print(f"39  is greater than 9: ", is_greater("39", "9"))
#         print(ans)
#         return ans
        
        
from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if str(nums[i]) + str(nums[j]) < str(nums[j]) + str(nums[i]):
        #             t = nums[i]
        #             nums[i] = nums[j]
        #             nums[j] = t
                    

        nums.sort(key=cmp_to_key(lambda x, y: 1 if str(x)+str(y) > str(y)+str(x) else -1), reverse=True)

        print("Nums: ", nums)

        ans = ""
        flag = True
        for e in nums:
            if e != 0:
                flag = False
            ans += str(e)
        print(ans)
        if flag :
            return "0"
        return ans
        
        
s = Solution()
n = [3,30,34,5,9]
n = [10,2]
n = [10,2,9,39,17]
# n = [999999991,9]
# n = [0,0]
print(s.largestNumber(n))