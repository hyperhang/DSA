from typing import List


# class Solution:
#     def largestCombination(self, candidates: List[int]) -> int:
#         bin_list = []
#         max_length = len(bin(max(candidates))) - 2
#         print(max_length)
#         for num in candidates:
#             bin_list.append( "0"*(max_length - len(bin(num)[2:])) + bin(num)[2:])
#         print(bin_list)
#         max_com_length = 0
#         for i in range(max_length):
#             c = 0
#             for num in bin_list:
#                 if num[i] == '1':
#                     c += 1
#             max_com_length = max(max_com_length, c)
            
#         return max_com_length    
        
class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        count_bin = [0]*25
        for num in candidates:
            tem = bin(num)[2:]
            for i in range(len(tem)):
                count_bin[i] += tem[len(tem)-1 - i]== '1'
        
        return max(count_bin)    
        
sol = Solution()
candidates = [16,17,71,62,12,24,14]
# candidates = [8, 8]
print(sol.largestCombination(candidates))

# 11001