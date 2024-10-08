# class Solution:
#     def minSwaps(self, s: str) -> int:
#         count = 0
#         head = []
#         tail = []
#         i, j = 0, len(s)-1
#         while i < j :
#             if s[i] == ']' and len(head) == 0 and s[j] == '[' and len(tail) == 0:
#                 count += 1
#                 head.append('[')
#                 tail.append(']')
#                 i += 1
#                 j -= 1
#             else:
#                 if s[i] == ']' and len(head) != 0:
#                     head.pop()
#                     i += 1
#                 if  s[i] == '[':
#                     head.append('[')
#                     i += 1
                
#                 if s[j] == '[' and len(tail) != 0:
#                     tail.pop()
#                     j -= 1
#                 if  s[j] == ']':
#                     tail.append(']')
#                     j -= 1
#         return count


class Solution:
    def minSwaps(self, s: str) -> int:
        count = 0
        head = 0 # count of the number of [ 
        tail = 0 # count of the number of ]
        i, j = 0, len(s)-1
        while i < j :
            if s[i] == ']' and head == 0 and s[j] == '[' and tail == 0:
                count += 1
                head += 1
                tail += 1
                i += 1
                j -= 1
            else:
                if s[i] == ']' and head != 0:
                    head -= 1
                    i += 1
                if  s[i] == '[':
                    head += 1
                    i += 1
                
                if s[j] == '[' and tail != 0:
                    tail -= 1
                    j -= 1
                if  s[j] == ']':
                    tail += 1
                    j -= 1
        return count
    
sol = Solution()
# s = "][]["
# s = "]]][[["
# s = "]]]][[[["
s = '[[]]][][[]'
print(sol.minSwaps(s))

