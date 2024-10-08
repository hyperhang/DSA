class Solution:
    ans = 0
    def minLength(self, s: str) -> int:
        
        def rm(s):
            next_s = ''
            i = 0
            while i < len(s):
                if i+1 < len(s) and s[i:i+2] in ['AB', 'CD']:
                    i += 2
                else:
                    next_s += s[i]
                    i += 1
            print("Next_s : ", next_s)
            if len(next_s) == len(s):
                self.ans = len(s)
                return
            else:
                rm(next_s)
        rm(s)       
        return self.ans


class Solution:
    def minLength(self, s: str) -> int:
        stack = []
        for c in s:
            stack.append(c)
            print(stack)
            if len(stack) >=2 and stack[-2]+stack[-1] in ['AB', 'CD']:
                stack.pop()
                stack.pop()
        return len(stack)
        
sol = Solution()    
s = "ABFCACDB"
# s = 'ACBBD'
# s = 'AB'
print(sol.minLength(s))
            