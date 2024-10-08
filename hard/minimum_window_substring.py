from collections import Counter
class Solution:
    min_length = 1e6
    start, end = 0, 0
    def minWindow(self, s: str, t: str) -> str:
        count_t = Counter(t)
        
        def contain_t(count_x):
            for k, v in count_t.items():
                if count_x[k] < v :
                    return False
            return True
            
        i, j = 0, 0
        count_s = Counter()
        while i < len(s) and j < len(s):
            count_s[s[j]] += 1
            if contain_t(count_s):
                for k in range(i+1, j+2):
                    count_s[s[k-1]] -= 1
                    if not contain_t(count_s):
                        i = k-1
                        if -i + j + 1 < self.min_length:
                            self.min_length = j - i + 1
                            self.start, self.end = i, j
                        i = k
                        break
            j += 1
        if self.min_length == 1e6:
            return ""
        return s[self.start: self.end+1]
                    
            
    
sol = Solution()
# s = "ADOBECODEBANC"
# t = "ABC"

s = "a"
t = "a"

# s = "a"
# t = "aa"

s = 'nawednffewuasxsdxwe' 
t= 'andex'

print("res = ",sol.minWindow(s, t))
                    