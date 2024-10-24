from sortedcontainers import SortedDict
import bisect
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        k = len(num) - k
        ele_idx = SortedDict()
        for i, ele in enumerate(num):
            ele_idx[int(ele)] = ele_idx.get(int(ele), []) + [i]
        ans = ""
        current_idx = 0
        while k != 0:
            for i in range(10):
                if i in ele_idx.keys():
                    first_appear = bisect.bisect_left(ele_idx[i], current_idx)
                    if first_appear == len(ele_idx[i]):
                        continue
                    first_appear = ele_idx[i][first_appear]
                    if first_appear <= len(num) - k:
                        ans += str(i)
                        current_idx = first_appear + 1
                        break
            k -= 1
        
        i = 0
        while i<len(ans) and ans[i] == '0':
            i += 1
        ans = ans[i:]
        if len(ans) == 0:
            ans = '0'
        return ans

sol = Solution()
num = "1432219"
k = 3

num = "10200"
k = 1

# num = "10"
# k = 2
print(sol.removeKdigits(num, k))
            
        
        # 424552455522155, k = 6
        # 1: 1, 2: 
        # 2-2-4-1-5-5
        