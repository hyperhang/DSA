from typing import List


# class Solution:
#     def lexicalOrder(self, n: int) -> List[int]:
#         ans = []
        
#         def next_num(cur_num: int):
#             if cur_num > n:
#                 return
#             for i in range(10):
#                 _val = cur_num*10+i
#                 if _val == 0 :
#                     continue
#                 if _val <= n :
#                     ans.append(_val)
#                     next_num(_val)
#                 else:
#                     return

#         next_num(0)
#         print(ans)
#         return ans
    
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ans = [1]
        cur = 1
        while cur < n:
            if cur*10 <= n:
                cur = cur*10
                ans.append(cur)
                continue
            while cur % 10 == 9 and cur + 1 > n:
                cur = cur // 10
            if cur == 0:
                break
            cur = cur + 1
            ans.append(cur)
            
        print(ans)
        return ans
    
s = Solution()
n = 50
s.lexicalOrder(n)