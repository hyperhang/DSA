import copy
class Solution:
    max_substr = 0
    def maxUniqueSplit(self, s: str) -> int:        
        def select(idx:int, current_arr: list):
            if idx == len(s):
                if len(current_arr) == len(set(current_arr)):
                    self.max_substr = max(self.max_substr, len(current_arr))
                return
            for i in range(2):
                tem = copy.deepcopy(current_arr)
                if i == 0:
                    tem[-1] = tem[-1] + s[idx]
                else:
                    tem.append(s[idx])
                select(idx+1, tem)
        select(1, [s[0]])

        return self.max_substr
        # TC: O(2^n*n) -> can optimize to O(2^n)
        # SC: O(2^n) -> can optimize to O(n)
    
sol = Solution()
s = "ababccc" # 5
# s = "aba" # 2
# s = 'aa' # 1
# s = 'hq' # 2
print(sol.maxUniqueSplit(s))
            