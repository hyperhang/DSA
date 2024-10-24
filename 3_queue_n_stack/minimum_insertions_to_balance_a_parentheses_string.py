# class Solution:
#     def minInsertions(self, s: str) -> int:
#         stack = []
#         ans, i = 0, 0
#         while i < len(s):
#             print(f"\ns[{i}] = {s[i]}")
#             if s[i] == '(':
#                 if len(stack) == 1 and stack[-1] == ')':
#                     ans += 2
#                     stack.pop()
#                 elif len(stack) > 1 and stack[-1] == ')':
#                     ans += 1
#                     stack.pop()
#                     stack.pop()
#                 stack.append('(')
#             else: # s[i] == ')'
#                 if len(stack) >= 2:
#                     if stack[-1] == ')': # ())
#                         print("stack: ", stack)
#                         stack.pop()
#                         stack.pop()
#                         print("delete: ", stack)
#                     else:
#                         stack.append(')') # (()
#                 elif len(stack) == 1: 
#                     if stack[-1] == '(':
#                         stack.append(')')  # ()
#                     else: # )
#                         ans += 1 # ))
#                         stack.pop() 
#                 else:
#                     stack.append(')')
#             print(f"stack: {stack}, ans: {ans} ")
#             i += 1
        
#         if len(stack) >= 2 and stack[-1] == ')' and stack[-2] == '(':
#             ans += 1
#             stack.pop()
#             stack.pop()
#         elif len(stack) == 1 and stack[-1] == ')':
#             ans += 2
#             stack.pop()
            
        
#         ans += len(stack)*2
        
              
#         return ans

class Solution :
    def minInsertions(self, s: str) -> int:
        i, count, left = 0, 0, 0
        s = s + '$'
        while i < len(s) - 1:
            print("------"*5)
            print(f"Start : s = {s[:i]}, add: {s[i]}")
            if s[i] == '(':
                left += 1
            else:
                if s[i] == ')' and s[i+1] == ')':
                    if left:
                        left -= 1
                    else:
                        count += 1
                    i += 1
                elif s[i] == ')' and s[i+1] != ')':
                    if left:
                        count += 1
                        left -= 1
                    else:
                        count += 2
            i += 1
            print(f"left = {left}, count = {count}")
        
        return count + 2*left
                    
                        
                


sol = Solution()
s = "(()))"
# s = '())'
# s = "))())("
s = ")))((((()()()"
# s = "((())))))"
print(sol.minInsertions(s))


